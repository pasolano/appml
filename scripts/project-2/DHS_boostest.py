import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow as tf
import seaborn as sns

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

tf.get_logger().setLevel('WARNING')

pns = pd.read_csv('C:/Users/pablo/Documents/classes/appml/data/project-2/pns.csv')

pns['gender'] = np.where(pns['wealth'] == 1, "male", "female")

#set for wealth = 5 vs all others
pns['wealth'] = np.where(pns['wealth'] == 1, 1, 0)
# pns['wealth'] = np.where(pns['wealth'] == 2, 1, 0)
# pns['wealth'] = np.where(pns['wealth'] == 3, 1, 0)
# pns['wealth'] = np.where(pns['wealth'] == 4, 1, 0)
# pns['wealth'] = np.where(pns['wealth'] == 5, 1, 0)

pns['gender'].value_counts().plot(kind='barh')
plt.show()

X_train, X_test = train_test_split(pns, test_size=0.25)
y_train = X_train.pop('wealth')
y_test = X_test.pop('wealth')

CATEGORICAL_COLUMNS = ["gender", "age", "edu"]
NUMERIC_COLUMNS = ["size"]

def one_hot_cat_column(feature_name, vocab):
  return tf.feature_column.indicator_column(
      tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocab))

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  # Need to one-hot encode categorical features.
  vocabulary = X_train[feature_name].unique()
  feature_columns.append(one_hot_cat_column(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
      feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

example = dict(X_train.head(1))
example = dict(X_train.head())
example = dict(X_train)
class_fc = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_vocabulary_list('gender', ('male', 'female')))
print('Feature value: "{}"'.format(example['gender'].iloc[0])) # Feature value: "female"
print('One-hot encoded: ', tf.keras.layers.DenseFeatures([class_fc])(example).numpy())
# One-hot encoded:  [[0. 1.]
#  [0. 1.]
#  [0. 1.]
#  ...
#  [0. 1.]
#  [0. 1.]
#  [1. 0.]]

tf.keras.layers.DenseFeatures(feature_columns)(example).numpy()

NUM_EXAMPLES = len(y_train)

def make_input_fn(X, y, n_epochs=None, shuffle=True):
  def input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((dict(X), y))
    if shuffle:
      dataset = dataset.shuffle(NUM_EXAMPLES)
    # For training, cycle thru dataset as many times as need (n_epochs=None).
    dataset = dataset.repeat(n_epochs)
    # In memory training doesn't use batching.
    dataset = dataset.batch(NUM_EXAMPLES)
    return dataset
  return input_fn

train_input_fn = make_input_fn(X_train, y_train)
eval_input_fn = make_input_fn(X_test, y_test, shuffle=False, n_epochs=1)

linear_est = tf.estimator.LinearClassifier(feature_columns) #logistic regression model

linear_est.train(train_input_fn, max_steps=100)

# Evaluation.
result = linear_est.evaluate(eval_input_fn)
clear_output()
print(pd.Series(result))
# accuracy                  0.851830
# accuracy_baseline         0.851830
# auc                       0.715795
# auc_precision_recall      0.359984
# average_loss              0.371417
# label/mean                0.148170
# loss                      0.371417
# precision                 0.000000
# prediction/mean           0.166059
# recall                    0.000000
# global_step             100.000000
# dtype: float64

# Since data fits into memory, use entire dataset per layer. It will be faster.
# Above one batch is defined as the entire dataset.
n_batches = 1
est = tf.estimator.BoostedTreesClassifier(feature_columns, n_batches_per_layer=n_batches)

# The model will stop training once the specified number of trees is built, not
# based on the number of steps.
est.train(train_input_fn, max_steps=100)

# Eval.
result = est.evaluate(eval_input_fn)
clear_output()
print(pd.Series(result))
# accuracy                  0.861708
# accuracy_baseline         0.851830
# auc                       0.742146
# auc_precision_recall      0.383084
# average_loss              0.347584
# label/mean                0.148170
# loss                      0.347584
# precision                 0.623188
# prediction/mean           0.153494
# recall                    0.168627
# global_step             100.000000
# dtype: float64

# logistic regression
pred_dicts = list(linear_est.predict(eval_input_fn))
probs_l = pd.Series([pred['probabilities'][1] for pred in pred_dicts])

probs_l.plot(kind='hist', bins=20, title='predicted probabilities')

# boosted tree
pred_dicts = list(est.predict(eval_input_fn))
probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])

probs.plot(kind='hist', bins=20, title='predicted probabilities')

# pdfs
probs_l.plot(kind='kde')
probs.plot(kind='kde', title='predicted probabilities')

from sklearn.metrics import roc_curve

fpr, tpr, _ = roc_curve(y_test, probs)
plt.plot(fpr, tpr)
plt.title('ROC curve')
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.xlim(0,)
plt.ylim(0,)
plt.show()