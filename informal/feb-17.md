# Response for 17 February 2021

## Last time you did an exercise (convolutions and pooling) where you manually applied a 3x3 array as a filter to an image of two people ascending an outdoor staircase. Modify the existing filter and if needed the associated weight in order to apply your new filters to the image 3 times. Plot each result, upload them to your response, and describe how each filter transformed the existing image as it convolved through the original array and reduced the object size. What are you functionally accomplishing as you apply the filter to your original array (see the following snippet for reference)? Why is the application of a convolving filter to an image useful for computer vision? Stretch goal: instead of using the `misc.ascent()` image from `scipy`, can you apply three filters and weights to your own selected image? Again describe the results

For reference, I am including the source image (ascent from `scipy`) below:
![Ascent](https://github.com/pasolano/appml/blob/main/data/feb-17/ascent.png?raw=true)

Some of my convolutions filtered the given images in similar ways, but all of the resulting images are unique in some way.

![Convolution 1](https://github.com/pasolano/appml/blob/main/data/feb-17/feb-17-conv-1.png?raw=true)

```python
filter1 = [ [-4, -6, -3], [1, 1, 1], [3, 4, 3] ]
```

The convolution above strongly highlighted the vertical lines in the original image. All of the vertical bars on the staircase are white, including the half-vertical diagonal lines in the top left corner of the image. The person on the right has the vertical shadows the folds in his shirt created highlighted as well. This filter also slightly highlights most horizontal lines in the image, including some lines in the sky that can barely be seen in the original image.

![Convolution 2](https://github.com/pasolano/appml/blob/main/data/feb-17/feb-17-conv-2.png?raw=true)

```python
filter2 = [ [-4, 1, 3], [-6, 1, 4], [-3, 1, 3] ]
```

This convolution also highlights lines, but does not emphasize vertical lines as strongly as the first convolution does. Instead, it seems to highlight horizontal lines more strongly. This effect can be seen in the bars in the middle of the roof of the staircase and in the crease between the person-on-the-right's sweater and backpack. As expected, the diagonal lines in the top left are about as white as those in the previous convolution, as they are as horizontal as they are vertical. It is important to note that some vertical lines are strongly emphasized, such as the frame on the right side of the image and the bars in the bottom right. Some clusters of lines are highlighted such as the tree in the bottom left, and the bars on the middle left of the image. Finally, the mostly-horizontal lines in the sky are highlighted more strongly than they were in the previous image.

![Convolution 3](https://github.com/pasolano/appml/blob/main/data/feb-17/feb-17-conv-3.png?raw=true)

```python
filter3 = [ [ -4, 4, -4], [4, 0, 4], [-4, 4, -4] ]
```

Our final convolution highlights some lines, but definitely prioritizes them less than the previous two examples. For instance, the vertical bars on the bottom of the staircase are white, as well as the diagonal lines in the top left of the image. What makes this filter unique, though, is it's attention to squares in the image. For example, the tree at the bottom of the photo is represented as a tight cluster of small squares, and the backpack of the person on the right of the image also has squares. The cluster of bars on the left side of the image is also more rectangular than in the last two convolutions. My eyes did not see any squares in the tree of the the original image, but our filter picks up on shapes there that are closer to squares than in other places in our image.

As for what the convolution is functionally accomplishing, it is essentially comparing each pixel to its neighbors, and changing its values based on what it is surrounded by. The filter used for the convolution is important because it is used to change the "meaning" of the neighboring pixels. For instance, a 6 for a neighboring pixel in the filter array would mean that that pixel should make the new value of the center pixel 6 times brighter than it would if that neighboring pixel had a filter array value of 1.

The application of a convolving filter to an image is useful for computer vision because it can be used to make images easier for computers to interpret. For instance, if we made a filter that was able to highlight floppy ears in an image, we could use it to detect images that contain dogs vs. cats by making another program that looks for clusters of white that surpass a given threshold (or we could let machine learning determine that threshold for us and have it perform the categorization).

## Another useful method is pooling. Apply a 2x2 filter to one of your convolved images, and plot the result. In effect what have you accomplished by applying this filter? Does there seem to be a logic (i.e. maximizing, averaging or minimizing values?) associated with the pooling filter provided in the example exercise (convolutions & pooling)? Did the resulting image increase in size or decrease? Why would this method be useful? Stretch goal: again, instead of using `misc.ascent()`, apply the pooling filter to one of your transformed images

The original image:
![Ascent](https://github.com/pasolano/appml/blob/main/data/feb-17/ascent.png?raw=true)

The convolution:
![Convolution 1](https://github.com/pasolano/appml/blob/main/data/feb-17/feb-17-conv-1.png?raw=true)

The pooling:
![Pooling](https://github.com/pasolano/appml/blob/main/data/feb-17/pool.png?raw=true)

By applying this filter, I have basically lowered the resolution of the image while attempting to lose as little important information from the image as possible. The way the pooling algorithm does this is it looks at a grid of 4 pixels, chooses the largest value, and has that value represent those 4 pixels as one pixel in the transformed image.

The logic associated with this filter is maximizing, as that's the way this specific pooling algorithm preserves the most important information from the image.

The resulting image is smaller than the original image, being exactly 1/4th the original size.

This method is useful for machine vision because, again, it makes images easier for computers to process and understand. When there are fewer pixels, a computer has less information to look through and compare with other data. Having more pixels does not only make machine learning take longer to process the images, but it also might cause the algorithm to focus on irrelevant details that pooling would get rid of.

## Bonus: Convolve the 3x3 filter over the 9x9 matrix and provide the resulting matrix.