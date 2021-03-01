# Response for 24 February 2021

- Convolutions:
  - Convolve the two 3x3 matrices that were assigned to you with your 9x9 matrix and calculate the resulting two matrices

  Original matrices:</br>
  ![Original matrices](https://github.com/pasolano/appml/blob/main/data/feb-24/matrices.png?raw=true)

  Convolutions:</br>
  ![Convolutions](https://github.com/pasolano/appml/blob/main/data/feb-24/convolutions.png?raw=true)

  - What is the purpose of using a 3x3 filter to convolve across a 2D image matrix?

  Using a 3x3 filter on a 2D image matrix is useful when trying to find certain features about that image. For example, in the last informal response, my filters were able to find lines and squares in an image. Using a small filter on a larger image is useful when trying to find a small feature that might appear multiple times in an image, or even if it might appear just once. It would not be as useful to use a 9x9 filter for a 9x9 image as the convolution would only have 1 pixel of output.

  - Why would we include more than one filter? How many filters did you assign as part of your architecture when training a model to learn images of numbers from the mnist dataset?

  Applying more than one filter could be helpful when trying to find more than one identifying characteristic in an image, since it is likely one filter would not be able to highlight two distinct characteristics. I did not use any filters while doing training my model for the mnist dataset, but it did not need them because the numbers are similar enough to each other without needing any features highlighted.

- MSE: From your 400+ observations of homes for sale, calculate the MSE for the following.
  - The 10 biggest over-predictions

  `The Mean Squared Error is:  2684870383784.711`

  - The 10 biggest under-predictions

  `The Mean Squared Error is:  15852507295248.031`

  - The 10 most accurate results (use absolute value)

  `The Mean Squared Error is:  49274359.067871094`

  - In which percentile do the 10 most accurate predictions reside? Did your model trend towards over or under predicting home values?

  `[38.51508120649652, 39.675174013921115, 47.56380510440835, 32.25058004640371, 44.54756380510441, 62.41299303944316, 35.96287703016241, 35.03480278422274, 32.01856148491879, 57.30858468677494]`

  These are the percentiles of the closest matching predictions, in order from closest to least close.

  ```
  Over-predicted 206 times
  Under-predicted 225 times
  ```

  This model tends to over-predict about as often as it under-predicts, but slightly trends toward under-predicting.
  - Which feature appears to be the most significant predictor in the above cases?

  `[-0.21271023], [ 0.55587214], [ 0.41551423]`
  
  These are the weights of the model (corresponding to number of beds, number of bathrooms, and square footage). Since the weight for number of bathrooms is the largest, it tends to be the most significant feature for predictions.
  
  - Stretch goal: calculate the MAE and compare with your MSE results