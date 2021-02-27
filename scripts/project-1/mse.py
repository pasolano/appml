import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import collections
from scipy import stats

def mse(xs, ys):
  summation = 0  #variable to store the summation of differences
  n = len(ys) #finding total number of items in list
  for i in range (0,n):  #looping through each element of the list
    difference = xs[i] - ys[i]  #calculating the difference between observed and predicted value
    squared_difference = difference**2  #taking square of the differene
    summation = summation + squared_difference  #taking a sum of all the differences
  mse = summation/n  #dividing summation by total values to obtain average
  print ("The Mean Squared Error is: ", mse)

# import data
df = pd.read_csv('out.csv')

# cast columns
df['prices'] = pd.to_numeric(df['prices'])
df['no_beds'] = pd.to_numeric(df['no_beds'])
df['baths'] = pd.to_numeric(df['baths'])
df['sqft'] = pd.to_numeric(df['sqft'])

# standardize data
df['prices'] = df['prices']/100000
df['sqft'] = df['sqft']/1000

# train model
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer = 'sgd', loss='mean_squared_error')

x_cols = ['no_beds', 'baths', 'sqft']

xs = np.stack([np.array(df[name], dtype=float) for name in x_cols], axis=1)
ys = np.array(df['prices'], dtype=float)

model.fit(xs, ys, epochs=1000)

# get predictions
predictions = model.predict(xs)

diffs = {}

for index, value in df.iterrows():
  diff = predictions[index][0] - value['prices']
  diffs[diff] = [value['prices'], predictions[index][0]]
  
od = collections.OrderedDict(sorted(diffs.items()))

# 10 biggest over-predictions
over_pred = list(reversed(od))[0:10]
over_real = [diffs[i][0] for i in over_pred]
mse(over_real, over_pred)

# print 10 biggest under-predictions
under_pred = list(od.keys())[0:10]
under_real = [diffs[i][0] for i in under_pred]
mse(under_real, under_pred)

# calculate difference between prediction and price (abs)
diffs = {}
for index, value in df.iterrows():
  diff = abs(predictions[index][0] - value['prices'])
  diffs[diff] = [value['prices'], predictions[index][0]]

od = collections.OrderedDict(sorted(diffs.items()))

close_pred = list(od.keys())[0:10]
close_real = [diffs[i][0] for i in close_pred]
mse(close_real, close_pred)

# quartiles
print([stats.percentileofscore(predictions, pred) for pred in close_pred])