import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def convolve(img, filter, weight=1):
    img_copy = np.copy(img)
    size_x = img.shape[0]
    size_y = img.shape[1]
    for x in range(1,size_x-1):
        for y in range(1,size_y-1):
            convolution = 0.0
            convolution += (img[x - 1, y-1] * filter[0][0])
            convolution += (img[x, y-1] * filter[0][1])
            convolution += (img[x + 1, y-1] * filter[0][2])
            convolution += (img[x-1, y] * filter[1][0])
            convolution += (img[x, y] * filter[1][1])
            convolution += (img[x+1, y] * filter[1][2])
            convolution += (img[x-1, y+1] * filter[2][0])
            convolution += (img[x, y+1] * filter[2][1])
            convolution += (img[x+1, y+1] * filter[2][2])
            convolution *= weight
            if(convolution<0):
                convolution=0
            if(convolution>255):
                convolution=255
            img_copy[x, y] = convolution
    return img_copy

def pool(img):
    size_x = img.shape[0]
    size_y = img.shape[1]
    new_x = int(size_x/2)
    new_y = int(size_y/2)
    newImage = np.zeros((new_x, new_y))
    for x in range(0, size_x, 2):
        for y in range(0, size_y, 2):
            pixels = []
            pixels.append(img[x, y])
            pixels.append(img[x+1, y])
            pixels.append(img[x, y+1])
            pixels.append(img[x+1, y+1])
            newImage[int(x/2),int(y/2)] = pixels[len(pixels)-1]
    return newImage

def plot_image(image):
    plt.gray()
    plt.grid(False)
    plt.imshow(image)
    #plt.axis('off')
    plt.show()

# get image
img = misc.ascent()
print(type(img))

# define filters
# 9 numbers that add to 0
filter1 = [ [-4, -6, -3], [1, 1, 1], [3, 4, 3] ]
filter2 = [ [-4, 1, 3], [-6, 1, 4], [-3, 1, 3] ]
filter3 = [ [ -4, 4, -4], [4, 0, 4], [-4, 4, -4] ]
filters = [filter1, filter2, filter3]

# perform and display convolutions
for filter in filters:
    img_copy = convolve(img, filter)
    plot_image(img_copy)

# perform and display pooling
img_copy = convolve(img, filter1)
img_copy = pool(img_copy)
plot_image(img_copy)