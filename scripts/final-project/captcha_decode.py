import os
import random
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

directory = "C:\\Users\\pablo\\Documents\\classes\\appml\\data\\final-project\\captcha_images"
images = []
labels = []
class_names = []

demo_idx = random.randint(0, 9955) # hardcoded for number of files
counter = 0
for filename in os.listdir(directory):
    counter += 1
    img_obj = tf.io.decode_png(
        tf.io.read_file(directory + "\\" + filename), channels=1
    )
    chars = list(filename.split('.')[0])
    
    # check if demo element
    if counter == demo_idx:
        demo_img = img_obj
        demo_label = chars

    for i in chars:
        labels.append(i)
        if i not in class_names:
            class_names.append(i)
    for i in range(4):
        images.append(tf.image.crop_to_bounding_box(img_obj, 0, i * 18, 24, 18))
class_names.sort()

# convert labels to ints to avoid biasing model
for i in range(len(class_names)):
    labels = [i if j==class_names[i] else j for j in labels]

# create the dataset
dataset = tf.data.Dataset.from_tensor_slices((images, labels))

# set aside 20% for validation
shuffled  = dataset.shuffle(len(dataset))
twenty_percent = int(len(shuffled) * .2)
test_dataset = dataset.take(twenty_percent) 
train_dataset = dataset.skip(twenty_percent)

# get labels and images back
test_images = []
test_labels = []
train_images = []
train_labels = []
for image, label in test_dataset:
    test_images.append(image)
    test_labels.append(label)
for image, label in train_dataset:
    train_images.append(image)
    train_labels.append(label)
test_images = tf.convert_to_tensor(test_images, dtype=tf.float32)
test_labels = tf.convert_to_tensor(test_labels, dtype=tf.uint8)
train_images = tf.convert_to_tensor(train_images, dtype=tf.float32)
train_labels = tf.convert_to_tensor(train_labels, dtype=tf.uint8)

# normalize
test_images /= 255.0
train_images /= 255.0

# set up layers
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(24, 18)),
                                    tf.keras.layers.Dense(256, activation=tf.nn.relu), # originally 128
                                    tf.keras.layers.Dense(32, activation=tf.nn.softmax)])

# compile the model
model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# train the model
model.fit(train_images, train_labels, epochs=200) # originally 5

# predict
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
random_idx = np.random.randint(0, len(predictions))
random_prediction = predictions[random_idx]
np.argmax(random_prediction)

# plot image
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(img, cmap=plt.cm.binary)
  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(32))
  plt.yticks([])
  thisplot = plt.bar(range(32), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

plot_value_array(random_idx, random_prediction, test_labels)
_ = plt.xticks(range(32), class_names, rotation=45)
plt.show()

plot_image(random_idx, random_prediction, test_labels, test_images)
plt.show()

# demo
pred_text = ""
demo_img = tf.cast(demo_img, dtype=tf.float32)
demo_img /= 255.0
demo_img = [demo_img]
for i in range(4):
    crop_img = tf.image.crop_to_bounding_box(demo_img, 0, i * 18, 24, 18)
    crop_pred = probability_model.predict(crop_img)
    pred_text += class_names[np.argmax(crop_pred)]

# plot demo
plt.grid(False)
plt.xticks([])
plt.yticks([])
plt.imshow(demo_img[0], cmap=plt.cm.binary)
plt.xlabel("{}".format(pred_text), color="black")
plt.show()