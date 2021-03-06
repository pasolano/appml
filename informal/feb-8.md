# Responses for 8 Feb 2020

## In the video, First steps in computer vision, Laurence Maroney introduces us to the Fashion MNIST data set and using it to train a neural network in order to teach a computer “how to see.” One of the first steps towards this goal is splitting the data into two groups, a set of training images and training labels and then also a set of test images and test labels. Why is this done? What is the purpose of splitting the data into a training set and a test set?

The purpose of splitting the data into two groups is two have enough data to create an accurate model, but to also have verified data two ensure the accuracy of our model with. If we used all of our data for training, we would not have any data to test our model with that was not used to create the model. It is important to test the data with data that was not used during the training process because the model will likely be more accurate with data it was trained with, but we want the model to work on all data. We also can not use all of our data for testing, because then we would not have any data to base our model on!

## The fashion MNIST example has increased the number of layers in our neural network from 1 in the past example, now to 3. The last two are Dense layers that have activation arguments using the relu and softmax functions. What is the purpose of each of these functions. Also, why are there 10 neurons in the third and last layer in the neural network

We use the `relu` function to set the output of a neuron to 0 if it is less than 0. We need to do this because negative outputs can skew the results of the model, canceling out other positive outputs.
We use the `softmax` function to help us find the most likely match out of all of the articles of clothing. It finds the highest value and sets it equal to 1 while setting all of the other values equal to 0, meaning that we only have to find the 1 while interpreting these results.
The last layer has 10 neurons because each category of clothing is assigned to one neuron, whose job it is to decide what the probability is that a piece of clothing belongs to its class.

## In the past example we used the optimizer and loss function, while in this one we are using the function adam in the optimizer argument and sparse_categorical- crossentropy for the loss argument. How do the optimizer and loss functions operate to produce model parameters (estimates) within the `model.compile()` function?

The optimizer chooses values to pass to each neuron based on the result of the loss function. The loss function in turn calculates how off a models guess was, which then influences the optimizer.

## Using the mnist drawings dataset (the dataset with the hand written numbers with corresponding labels) answer the following questions

### 1. What is the shape of the images training set (how many and the dimension of each)?

There are 60,000 images in the training set, each with a size of 28x28.

### 2. What is the length of the labels training set?

There are 60,000 labels in the training set.

### 3. What is the shape of the images test set?

There are 10,000 images in the test set, each with a size of 28x28.

### 4. Estimate a probability model and apply it to the test set in order to produce the array of probabilities that a randomly selected image is each of the possible numeric outcomes (look towards the end of the basic image classification exercises for how to do this — you can apply the same method applied to the Fashion MNIST dataset but now apply it to the hand written letters MNIST dataset)

### 5. Use `np.argmax()` with your predictions object to return the numeral with the highest probability from the test labels dataset

### 6. Produce a plot of your selected image and the accompanying histogram that illustrates the probability of that image being the selected number

![Histogram](https://github.com/pasolano/appml/blob/main/data/feb-8/feb-8-hist.png?raw=true)
![Plot](https://github.com/pasolano/appml/blob/main/data/feb-8/feb-8-plot.png?raw=true)
