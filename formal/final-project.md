# Compromising Captcha with Computer Vision

## Abstract

CAPTCHA is an essential component of internet security. Serving as a speed bump for brute force attacks, CAPTCHA is usually used to protect authentication processes. For example, it might prevent a bot attempting to guess someone’s password by asking them to answer a question only humans can answer before they can attempt to login again. For my project, I made a model that attempted to read CAPTCHA messages by reading the individual characters composing the image, and then combining the results to read the entire message. This was my approach to answering my question of whether I could leverage computer vision to read a simple version of a system designed to be unreadable for computers.

This process involved a couple core steps. First, I had to collect a large amount of data to train my model. To do this, I used a dataset from Kaggle. This dataset was composed of ~10,000 images with the same dimensions. Each image had 4 characters, increasing the amount we could learn from each image. Each image was also labelled in the filename. After getting this data, I had to prepare it. This involved normalizing, splitting into training and testing sets, setting the images to be greyscale, and splitting the images to have the images be roughly of one character each. Once this was done, I made my model – a sequential model from Keras that flattened the images, had a dense layer with 256 nodes using relu, and a layer that used 32 nodes for softmax. I then compiled it with the Adam optimizer and the Sparse Categorical Cross entropy loss function. While this was similar to the model we made for the Fashion MNIST dataset earlier in the year, it required modification. The difference in the number of classes and the off-center images required me to change the number of epochs and the number of nodes in the dense relu layer. After this, I finished by designing the validation process, which involved identifying a single letter that was randomly chosen, and then expanding this process to entire CAPTCHA. We will look at the results below.

This model ended up performing with 30%-70% accuracy, and occasionally getting stuck on 3% accuracy while training. While this is a large range, my model still produced results (and some garbage). Here are some failures:\
![Failure 1](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/failed-classification.PNG)
![Failure 2](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/failed-2.PNG)

And here are some successes:\
![Success 1](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/correct.PNG)
![Success 2](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/correct-2.PNG)
![Success 3](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/correct-3.PNG)

The 50-50 split makes sense when considering the wide range of the accuracy the model performed with, and can continue to be seen in its results. Here are examples of the model partially identifying CAPTCHAS:\
![Partial 1](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/full-text-semi.PNG)
![Partial 2](https://raw.githubusercontent.com/pasolano/appml/main/data/final-project/full-text-semi-2.PNG)

While this model may seem wildly inconsistent, it performs surprisingly well against a system designed to stump it. If a simple model can perform this well against simple CAPTCHAS, it might suggest that the CAPTCHAS of today are already vulnerable to computer vision models. Additionally, there are some additions that could be made to this model that would improve its success rate with little extra knowledge needed. For one, the model could be fed more examples of characters that are visually similar to each other, so the model has more data to base its most difficult decisions on. Finally, the data could be prepared so that the characters are split where space between characters are detected, and then the images could be stitched with more of their background color to maintain the standard shape models expect. Of course, preparing the data in this way might require another model with its own challenges.

## Final Presentation Link

[Presentation Video](https://drive.google.com/file/d/16uy4PyMXPKcwjxL9a8sO1pRDlqhUJzeG/view?usp=sharing)

## Final Slides Link

[Presentation Slides](https://docs.google.com/presentation/d/1vOmETxY3S1nfvUbDv-W2HXUUYfLDZoVyAAm6itk7ZZ8/edit?usp=sharing)

## Script Link

[Model Script](https://github.com/pasolano/appml/blob/main/scripts/final-project/captcha_decode.py)
