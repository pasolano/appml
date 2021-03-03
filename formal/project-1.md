# Project 1

## Describe the housing data you scraped from Zillow

In order to collect data to train my housing model, I used a Python script to scrape Zillow. This proved to be more challenging than I initially assumed. I began scraping the data from their site after they had already changed their site structure, so I had to change how the script manipulated the HTML it received. I also found that the script was unable to handle lots of different edge cases, including empty lots, houses with over 9 bathrooms or bedrooms, and listings that were missing the price, number of bedrooms, bathrooms, or square footage. I also ended up significantly refactoring my script to make it much shorter and readable, which also conveniently fixed an issue where clusters of numbers were getting repeated in my features columns. After trying a number of different cities and manually cleaning the data by removing incomplete listings and the double-digit issue I mentioned earlier, I ended up with 431 complete listings, each with a price, address, number of bedrooms, number of bathrooms, and square footage. All of the houses are located in Austin, Texas, which has far fewer mansions for sale than Los Angeles, which not only made the data set easier to clean, but also means that zipcode is not as significant of a variable as it is in the home of Beverly Hills. To conclude my description of the scraping process and the data, I have included a table below summarizing a number of statistics that provide extra insight into the data.

![Description](https://github.com/pasolano/appml/blob/main/data/project-1/describe.png?raw=true)

## Describe your model architecture

My model is comprised of one densely-connected layer that takes three features as input. It is also sequential, but that is not relevant as the model only has one layer. The model uses SGD as its optimizer, which stands for "stochastic gradient descent." This is the function that tells the model how it should adjust its guess for the next epoch to get a smaller calculated loss. The model uses mean squared error to calculate loss, which is the average of the distance between the guess and the true value squared. For this project, the model is given the number of beds, number of baths, and square footage of each house in the Austin dataset as input. The model is also passed the price of each home as labels, or the thing the model is trying to predict as accurately as possible. Since the size of the values in each of these columns varies dramatically, the model is passed these models after they are standardized using a standard scaler, which can be easily scaled back proportionally once the model has made its guess. When I fit the model, I used 1,000 epochs, which gives the model 1000 tries to minimize the loss function. I settled on 1,000 epochs because the results the model put out were better than they were for 500 epochs, but decided not to go any higher to avoid overfitting my model (which was a danger for this project, as I trained and tested my model with the same dataset).

## Analyze your model output

The output of this model proves that it is by no means perfect. While the loss function remained minimal during the fitting process, the MSE of the predictions is massive. This is partially due to the fact that some of the values in the base set are large and any difference would look large (especially squared), but especially when it comes to finances, the mean squared errors are hard to ignore. However, they are an improvement over my model that had a six-digit loss at every epoch. An important detail to note is that the MSE for the under-predictions is larger than that of the over-predictions:

```
The MSE for the 10 biggest over-predictions:   2732297816968.2905
The MSE for the 10 biggest under-predictions:  15699231253824.707
The MSE for the 10 closes predictions:         53504804.919238284
```

I also calculated the percentiles of the ten closest predictions, from left to right:

`[41.9953596287703, 35.96287703016241, 35.03480278422274, 22.505800464037122, 25.986078886310906, 62.87703016241299, 43.851508120649655, 39.675174013921115, 38.51508120649652, 57.07656612529002]`

Most of the closest predictions were below the median of the predictions, which makes sense since the MSE hinted that this model tends to under-predict. If both the larger MSE for under-predictions and the percentiles are not enough evidence, though, the script also says that the model over-predicted 203 times and under-predicted 228 times, confirming that the model has a small tendency to under-predict.

The output of the script also informs us which features the model found to be the most important for predicting the value of a house:

```py
no_beds = -0.2071016,
baths = 0.56377375,
sqft = 0.4089439
```

The largest weight is baths, meaning that it is the weight that affects predictions the most, while the number of bedrooms matters the least. This does not make intuitive sense as bedrooms tend to increase the value of a house, but the model determined that the other features were more important for predicting a house's price.

Finally, I plotted the real prices listed on Zillow against the predictions my model came up with for each property.

![Pred_vs_Real](https://github.com/pasolano/appml/blob/main/data/project-1/pred_vs_real.png?raw=true)

The line in the graph shows where on the graph the predicted price and real price would be equal if the trend of the data continued. This line shows that the real price grows faster than the predicted price, confirming that our model was under-predicting. However, as can be seen in the cluster on the left of the image, many of the predictions made were within the realm of possibility.

![Pred_vs_Real_Zoom](https://github.com/pasolano/appml/blob/main/data/project-1/pred_vs_real_zoom.png?raw=true)

When we zoom in, we can also see that all of the dots in this cluster are in the ballpark of what they are supposed to cost, which is pretty amazing output for such a simple model.

## Analyze the output that assesses and ranks all homes from best to worst deal

We can also look at the predictions as a source of truth. If we trust our model, it can expose house listings that are not listed for their actual values -- either because they are being listed for too much, or for too little.

![Diff_vs_Real](https://github.com/pasolano/appml/blob/main/data/project-1/diff_vs_real.png?raw=true)

Here we can see the difference between the predicted value of the house minus the actual value. We can view positive differences as houses the model says are worth more than they are being sold for, negative values as houses being sold for too much, and values close to zero as houses being sold for around their worth. According to this plot, many of the cheaper houses are being sold for fair prices (as they are hovering around zero), but as houses get more expensive, the prices get more unfair. It is important to consider if this is really the case, though, or if affordable houses should not be used as the metric for whether mansions are worth the pricetag or not. The line in this case shows a downward trend, meaning that the houses in our data get more overpriced as they get more expensive.

![Diff_vs_Real_Zoom](https://github.com/pasolano/appml/blob/main/data/project-1/diff_vs_real_zoom.png?raw=true)

However, it is also important to zoom in on the cluster on the left, as that is where most of our data resides. We can see that there is about an equal amount of houses being sold for too much and for too little.

![Deal](https://github.com/pasolano/appml/blob/main/data/project-1/deal.png?raw=true)

![Ripoff](https://github.com/pasolano/appml/blob/main/data/project-1/ripoff.png?raw=true)

Finally, I have logged the five best deals (or five biggest over-predictions), and five worst deals respectively, just to be able to see in detail what the outliers of the model's output are. While these charts do not show it, the best deals do have high numbers of bedrooms, bathrooms, and square footage for houses in their prices range, while the worst deals are expensive houses that this model did not have enough data to predict accurately (and some houses that are just genuinely not worth it for the features they have). If I were to continue developing this model, a good next step would be to add location as a feature somehow, so that the area the house is being sold in is not ignored by the model completely. That might explain why some smaller houses are being sold for more than larger houses, or why mansions are more than double the price of a house half the size.
