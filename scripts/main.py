# # class on 2/3
# # starting with NN

# import tensorflow as tf
# import numpy as np
# from tensorflow import keras

# model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# model.compile(optimizer = 'sgd', loss='mean_squared_error')

# xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# model.fit(xs, ys, epochs=500)

# print(model.predict([18.0]))

# # episode 1 -- The "Hello World" of ML
# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer = 'sgd', loss='mean_squared_error')

# xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# model.fit(xs, ys, epochs=500)

# print(model.predict([10.0]))

# # exercise from episode 1

# # In this exercise you'll try to build a neural network that predicts the price of a house according to a simple formula.
# # So, imagine if house pricing was as easy as a house costs 50k + 50k per bedroom, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k etc.
# # How would you create a neural network that learns this relationship so that it would predict a 7 bedroom house as costing close to 400k etc.
# # Hint: Your network might work better if you scale the house price down. You don't have to give the answer 400...it might be better to create something that predicts the number 4, and then your answer is in the 'hundreds of thousands' etc.

# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer = 'sgd', loss='mean_squared_error')
# xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
# ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
# model.fit(xs, ys, epochs=500)
# print(model.predict([7.0]))

# # response 2/5 question 2

# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer = 'sgd', loss='mean_squared_error')

# xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# model.fit(xs, ys, epochs=500)

# print(model.predict([7.0]))

# # housing exercise with extra variable
# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[2])])
# model.compile(optimizer = 'sgd', loss='mean_squared_error')
# x1 = np.array([4.0, 3.0, 4.0, 5.0, 2.0, 3.0], dtype=float)
# x2 = np.array([3.524, 2.840, 3.680, 3.051, 1.479, 1.238], dtype=float)

# xs = np.stack([x1, x2], axis=1)
# ys = np.array([2.89, 2.29, 3.99, 3.475, 2.5, 0.97], dtype=float)

# model.fit(xs, ys, epochs=1000)

# a = np.array([5.0], dtype=float)
# b = np.array([3.680], dtype=float)
# c = np.stack([a, b], axis=1)

# print(model.predict([c]))

# fashion mnist

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Bag', 'Ankleboot']

train_images.shape
len(train_labels)
train_labels
test_images.shape
len(test_labels)

plt.imshow(train_images[0])
print(train_labels[0])
print(train_images[0])
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0 # compare w/ - w/o normalization
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

model = tf.keras.models.Sequential(tf.keras.layers.Flatten(input_shape=(28,28)),
        # tf.keras.layers.Dense(512, activation=tf.nn.relu),
        # tf.keras.layers.Dense(256, activation=tf.nn.relu),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        # tf.keras.layers.Dense(64, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10) #epochs = 30

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# too much, didn't get rest