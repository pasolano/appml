#!pip install -q sklearn
#!pip install -q -U tf-estimator-nightly
#!pip install -q -U tf-nightly

import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow as tf
import seaborn as sns

print(tf.__version__)

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
lin_reg = LinearRegression()

pns = pd.read_csv('DHSlbr.csv')

pns['wealth'].value_counts().plot(kind='barh')
plt.show()

#set for wealth = 5 vs all others
pns['wealth'] = np.where(pns['wealth'] == 1, 1, 0)

pns['wealth'].value_counts().plot(kind='barh')
plt.show()

X_train, X_test = train_test_split(pns, test_size=0.25)

# X_train = pd.DataFrame(pns[0:30000])
# X_test = pd.DataFrame(pns[30000:43929])
# X_test = X_test.reset_index(drop=True)
y_train = X_train.pop('wealth')
y_test = X_test.pop('wealth')

sns.pairplot(X_train[["size", "gender", "age", "edu"]], diag_kind="kde")
plt.show()

X_train.age.hist(bins=20)
plt.show()

X_train['edu'].value_counts().plot(kind='barh')
plt.show()

# pd.concat([X, y], axis=1).groupby('wealth').gender.mean().plot(kind='barh').set_xlabel('% survive')
# plt.show()

CATEGORICAL_COLUMNS = ["gender", "age", "edu"]
NUMERIC_COLUMNS = ["size"]

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = X_train[feature_name].unique()
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
    if shuffle:
      ds = ds.shuffle(1000)
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds
  return input_function

train_input_fn = make_input_fn(X_train, y_train)
eval_input_fn = make_input_fn(X_test, y_test, num_epochs=1, shuffle=False)

ds = make_input_fn(X_train, y_train, batch_size=10)()
for feature_batch, label_batch in ds.take(1):
  print('Some feature keys:', list(feature_batch.keys()))
  print()
  print('A batch of class:', feature_batch['edu'].numpy())
  print()
  print('A batch of Labels:', label_batch.numpy())

size_column = feature_columns[3]
tf.keras.layers.DenseFeatures([size_column])(feature_batch).numpy()

edu_column = feature_columns[2]
tf.keras.layers.DenseFeatures([tf.feature_column.indicator_column(edu_column)])(feature_batch).numpy()

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns, n_classes=10)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

clear_output()
print(result)

age_x_gender = tf.feature_column.crossed_column(['size', 'edu'], hash_bucket_size=100)

derived_feature_columns = [age_x_gender]
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns+derived_feature_columns, n_classes=10)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

clear_output()
print(result)

pred_dicts = list(linear_est.predict(eval_input_fn))
probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])

probs.plot(kind='hist', bins=20, title='predicted probabilities')

from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt

fpr, tpr, _ = roc_curve(y_test, probs)
plt.plot(fpr, tpr)
plt.title('ROC curve')
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.xlim(0,)
plt.ylim(0,)
plt.show()