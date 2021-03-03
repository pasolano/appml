import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import dataframe_image as dfi


def mse(xs, ys):
  summation = 0  #variable to store the summation of differences
  n = len(ys) #finding total number of items in list
  for i in range (0,n):  #looping through each element of the list
    difference = xs[i] - ys[i]  #calculating the difference between observed and predicted value
    squared_difference = difference**2  #taking square of the differene
    summation = summation + squared_difference  #taking a sum of all the differences
  mse = summation/n  #dividing summation by total values to obtain average
  print ("The Mean Squared Error is: ", mse[0])

# import data
df = pd.read_csv('../../data/project-1/austin.csv')

# cast columns
df['prices'] = pd.to_numeric(df['prices'])
df['no_beds'] = pd.to_numeric(df['no_beds'])
df['baths'] = pd.to_numeric(df['baths'])
df['sqft'] = pd.to_numeric(df['sqft'])

# standardize data
ss = StandardScaler()
# train model
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer = 'sgd', loss='mean_squared_error')

x_cols = ['no_beds', 'baths', 'sqft']

xs = np.stack([np.array(df[name], dtype=float) for name in x_cols], axis=1)
ys = np.array(df['prices'], dtype=float).reshape(-1, 1)

xss = ss.fit_transform(xs)
yss = ss.fit_transform(ys)

model.fit(xss, yss, epochs=1000)

# get predictions
preds = model.predict(xss).reshape(1,-1)[0]
preds = ss.inverse_transform(preds)

# calculate difference
x = np.array(df['prices'])
# y = ss.inverse_transform(preds)
diff = preds - x

# convert to dictionary { diff : index }
diff_dict = {}
for i in range(0, len(diff)):
  diff_dict[diff[i]] = i

# sort differences
diff_sort = sorted(list(diff_dict.keys()))

# 10 biggest over-predictions
diff_rev = sorted(diff_sort, reverse=True)
over_diff = diff_rev[:10]
over_preds = [preds[diff_dict[i]] for i in over_diff]
over_real = [ys[diff_dict[i]] for i in over_diff]
mse(over_preds, over_real)

# print 10 biggest under-predictions
under_diff = diff_sort[:10]
under_preds = [preds[diff_dict[i]] for i in under_diff]
under_real = [ys[diff_dict[i]] for i in under_diff]
mse(under_preds, under_real)

# 10 closest predictions
diff_abs = np.copy(diff)
diff_abs = np.abs(diff_abs)
diff_abs_dict = {}
for i in range(0, len(diff_abs)):
  diff_abs_dict[diff_abs[i]] = i

# sort differences
diff_abs_sort = sorted(list(diff_abs_dict.keys()))

close_diff = diff_abs_sort[:10]
close_preds = [preds[diff_abs_dict[i]] for i in close_diff]
close_real = [ys[diff_abs_dict[i]] for i in close_diff]
mse(close_preds, close_real)

# quartiles
print([stats.percentileofscore(preds, pred) for pred in close_preds])

# count number of over vs under predicted values
over = 0
under = 0
for i in diff:
  if i > 0:
    over += 1
  else:
    under += 1
print("Over-predicted", over, "times")
print("Under-predicted", under, "times")

# get weights of model
print(model.weights)

# plot actual vs predicted
compare = pd.DataFrame({"real" : df['prices'], "pred" : preds})
g = sns.lmplot(
    data=compare,
    x="real", y="pred"
    # height=5
)
g.set_axis_labels("Real Listed Prices", "Predicted Listed Prices")
plt.show()

# plot difference vs actual
diff = preds - df['prices']
compare = pd.DataFrame({"diff" : diff, "real" : df['prices']})
g = sns.lmplot(
  data=compare,
  x="real", y="diff"
)
g.set_axis_labels("Real Listed Prices", "Diff. Between. Pred. and Real Price")
plt.show()

# chart top and bottom 5 guesses
compare["predicted"] = preds
compare = compare.sort_values("diff")
dfi.export(compare[:5], '../../data/project-1/ripoff.png', table_conversion='matplotlib')
dfi.export(compare[len(compare)-5:len(compare)], '../../data/project-1/deal.png', table_conversion='matplotlib')