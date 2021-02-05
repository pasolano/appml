import tensorflow as tf
import numpy as np
from tensorflow import keras

# question 2

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer = 'sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([7.0]))

# question 3

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer = 'sgd', loss='mean_squared_error')

xs = np.array([4.0, 3.0, 5.0, 4.0, 2.0, 3.0], dtype=float)
ys = np.array([399.0, 97.0, 577.0, 289.0, 250.0, 229.0], dtype=float)

model.fit(xs, ys, epochs=500)

house_names = ["Church", "Hudgins", "Mathews", "Mobjack", "Moon", "New Point Comfort"]
savings = []
for i in range(0, len(xs)):
    savings.append(model.predict([float(xs[i])])[0][0] - ys[i])
for i in range(0, len(savings)):
    print("The \"%s\" house is worth $%s more than what it's being sold for." % (house_names[i], savings[i]))