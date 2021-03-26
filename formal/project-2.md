# Project 2, due Wednesday, March 24th by midnight

## Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)? Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? Provide justification for your selected penalty value. Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes

```
    penalty .metric .estimator  mean     n std_err .config              
      <dbl> <chr>   <chr>      <dbl> <int>   <dbl> <chr>                
 1 0.0001   roc_auc hand_till  0.592     1      NA Preprocessor1_Model01
 2 0.000127 roc_auc hand_till  0.592     1      NA Preprocessor1_Model02
 3 0.000853 roc_auc hand_till  0.592     1      NA Preprocessor1_Model10
 4 0.00108  roc_auc hand_till  0.592     1      NA Preprocessor1_Model11
 5 0.00137  roc_auc hand_till  0.593     1      NA Preprocessor1_Model12
 6 0.00174  roc_auc hand_till  0.593     1      NA Preprocessor1_Model13
 7 0.00221  roc_auc hand_till  0.593     1      NA Preprocessor1_Model14
 8 0.00281  roc_auc hand_till  0.593     1      NA Preprocessor1_Model15
 9 0.00356  roc_auc hand_till  0.593     1      NA Preprocessor1_Model16
10 0.00452  roc_auc hand_till  0.593     1      NA Preprocessor1_Model17
11 0.00574  roc_auc hand_till  0.593     1      NA Preprocessor1_Model18
12 0.00728  roc_auc hand_till  0.594     1      NA Preprocessor1_Model19
13 0.00924  roc_auc hand_till  0.596     1      NA Preprocessor1_Model20
14 0.0117   roc_auc hand_till  0.595     1      NA Preprocessor1_Model21
15 0.0149   roc_auc hand_till  0.594     1      NA Preprocessor1_Model22
```

According to `top_model`, `Preprocessor1_Model20` performed the best with a mean AUC of 0.596.

![LR Plot](https://github.com/pasolano/appml/blob/main/data/project-2/images/lr_plot.png?raw=true)

Yes, the feature selection penalty is able to tune the hyperparameter and remove potentially irrelevant predictors. As can be seen in the plot above, increasing the penalty leads the model to reaching its peak AUC - ROC. However, the penalty can also cause the AUC - ROC to become smaller, as can be seen in the later models. I selected a penalty value of 0.00924 because that's the penalty value the model with the largest mean AUC uses. As can be seen above, `Preprocessor1_Model20` is the model with the highest AUC.

![LR AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/lr_auc.png?raw=true)

The penalized logistic regression model is best at predicting the wealth outcomes in the following order: 5, 1, 2, 4, 3. This is because they have the most to least AUC between the curve and the dotted line in the middle of the graph.

## Using the R script provided, set up your random forest model and produce the AUC - ROC values for the randomly selected predictors, and the minimal node size, again with wealth as the target. How did your random forest model fare when compared to the penalized logistic regression? Provide your ROC plots and interpret them. Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?

![RF Res](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_res.png?raw=true)

Above is a plot showing the number of randomly selected predictors versus minimal node size.

![RF LR AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_lr_auc.png?raw=true)

Above is a plot comparing the ROC of the random forest models versus the penalized logistic regression models. The models performed similarly to each other, but it is important to note that the largest AUC looks like it belongs to random forest models, while the smallest belongs to a penalized logistic regression model. However, the models performed so similarly to each other that it is hard to tell.

![RF AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_auc.png?raw=true)

Similarly to the penalized logistic regression, the randomized forest model is best at predicting wealth outcomes 1 and 5, but confuses 2, 3, and 4 more often.

![Last RF Fit](https://github.com/pasolano/appml/blob/main/data/project-2/images/last_rf_fit.png?raw=true)

Above is a plot that shows the predictive importance of each feature in the randomized forest model, with `age` being the most important feature for predicting wealth, and with `gender` being the least.

## Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target. Apply the linear classifier to the feature columns and determine the accuracy, AUC and other evaluative metrics towards each of the different wealth outcomes. Then continue with your linear classifier adding the derived feature columns you have selected in order to extend capturing combinations of correlations (instead of learning on single model weights for each outcome). Again produce your ROC curves and interpret the results

### Wealth Group 1

Logistic regression model
```
accuracy           0.785590
average_loss       0.500734
loss               0.500711
global_step     1620.000000
AUC                0.642719
```

Added the derived feature columns
```
accuracy           0.783266
average_loss       0.496173
loss               0.496035
global_step     1620.000000
AUC                0.642719
```

![ROC Wealth 1](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth1.png?raw=true)

### Wealth Group 2

Logistic regression model
```
accuracy           0.819872
average_loss       0.470401
loss               0.470048
global_step     1620.000000
AUC                0.558661
```

Added the derived feature columns
```
accuracy           0.819872
average_loss       0.469791
loss               0.469299
global_step     1620.000000
AUC                0.558661
```

![ROC Wealth 2](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth2.png?raw=true)

### Wealth Group 3

Logistic regression model
```
accuracy           0.769901
average_loss       0.536287
loss               0.535911
global_step     1620.000000
AUC                0.569424
```

Added the derived feature columns
```
accuracy           0.772807
average_loss       0.534730
loss               0.534103
global_step     1620.000000
AUC                0.569424
```

![ROC Wealth 3](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth3.png?raw=true)

### Wealth Group 4

Logistic regression model
```
accuracy           0.798954
average_loss       0.489845
loss               0.489800
global_step     1620.000000
AUC                0.612979
```

Added the derived feature columns
```
accuracy           0.801278
average_loss       0.484694
loss               0.484545
global_step     1620.000000
AUC                0.612979
```

![ROC Wealth 4](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth4.png?raw=true)

### Wealth Group 5

Logistic regression model
```
accuracy           0.837304
average_loss       0.446023
loss               0.445456
global_step     1620.000000
AUC                0.585504
```

Added the derived feature columns
```
accuracy           0.839047
average_loss       0.442439
loss               0.441955
global_step     1620.000000
AUC                0.585504
```

![ROC Wealth 5](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth5.png?raw=true)

These ROC show that the model performed similarly for all of the wealth groups. While it's clear that the model is much better at predicting wealth group 1 correctly than wealth group 2 (since the difference in area is noticeably different), each ROC looks similar to the curve with an AUC smaller than it. So, while the model definitely predicts wealth group 1 better than wealth group 2, all of the groups are predicted with similar amounts of accuracy.

## Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. Provide evaluative metrics including a measure of accuracy and AUC. Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results

### Wealth Group 1

Gradient boosting model
```
accuracy                  0.782685
accuracy_baseline         0.785009
auc                       0.647277
auc_precision_recall      0.299709
average_loss              0.491391
label/mean                0.214991
loss                      0.491391
precision                 0.000000
prediction/mean           0.233556
recall                    0.000000
global_step             100.000000
```

![Pred Prob 1](https://github.com/pasolano/appml/blob/main/data/project-2/images/pred_prob_1.png?raw=true)

![ROC Wealth 1](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_1.png?raw=true)

### Wealth Group 2

Gradient boosting model
```
accuracy                  0.819291
accuracy_baseline         0.822196
auc                       0.606102
auc_precision_recall      0.221756
average_loss              0.455014
label/mean                0.177804
loss                      0.455014
precision                 0.000000
prediction/mean           0.182329
recall                    0.000000
global_step             100.000000
```

![Pred Prob 2](https://github.com/pasolano/appml/blob/main/data/project-2/images/pred_prob_2.png?raw=true)

![ROC Wealth 2](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_2.png?raw=true)

### Wealth Group 3

Gradient boosting model
```
accuracy                  0.775131
accuracy_baseline         0.780360
auc                       0.552362
auc_precision_recall      0.252759
average_loss              0.528785
label/mean                0.219640
loss                      0.528785
precision                 0.090909
prediction/mean           0.213195
recall                    0.002646
global_step             100.000000
```

![Pred Prob 3](https://github.com/pasolano/appml/blob/main/data/project-2/images/pred_prob_3.png?raw=true)

![ROC Wealth 3](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_3.png?raw=true)

### Wealth Group 4

Gradient boosting model
```
accuracy                  0.787914
accuracy_baseline         0.780941
auc                       0.596702
auc_precision_recall      0.339208
average_loss              0.511209
label/mean                0.219059
loss                      0.511209
precision                 0.650000
prediction/mean           0.217945
recall                    0.068966
global_step             100.000000
```

![Pred Prob 4](https://github.com/pasolano/appml/blob/main/data/project-2/images/pred_prob_4.png?raw=true)

![ROC Wealth 4](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_4.png?raw=true)

### Wealth Group 5

Gradient boosting model
```
accuracy                  0.842533
accuracy_baseline         0.837885
auc                       0.629992
auc_precision_recall      0.326081
average_loss              0.415161
label/mean                0.162115
loss                      0.415161
precision                 0.558824
prediction/mean           0.150446
recall                    0.136201
global_step             100.000000
```

![Pred Prob 5](https://github.com/pasolano/appml/blob/main/data/project-2/images/pred_prob_5.png?raw=true)

![ROC Wealth 5](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_5.png?raw=true)

The ROC - AUC for all of these wealth groups are approximately the same. As usual, the model predicts wealth outcomes 1 and 5 the best, but wealth outcome 4 is almost predicted just as accurately, and the others are not far off either. As for the predicted probabilities, the average value is the greatest in wealth group 1, steadily decreasing to being at its lowest for wealth group 5. This is because more people in Nepal belong to wealth group 1, then group 2, and so on.

## Analyze all four models. According to the evaluation metrics, which model produced the best results? Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?

The main discrepancy is that all of the models were able to predict the extreme wealth outcomes (1 and 5) more accurately than they could predict the middle outcomes. As for which model performed the best, the gradient boosted model and the logistic regression model performed very similarly

```
                                  Logistic Regression

         | Group 1     | Group 2     | Group 3     | Group 4     | Group 5     |
         | ----------- | ----------- | ----------- | ----------- | ----------- |
Accuracy | 0.785590    | 0.819872    | 0.769901    | 0.798954    | 0.837304    |
AUC      | 0.642719    | 0.558661    | 0.569424    | 0.612979    | 0.585504    |
```

```
                                    Boosted Gradient

         | Group 1     | Group 2     | Group 3     | Group 4     | Group 5     |
         | ----------- | ----------- | ----------- | ----------- | ----------- |
Accuracy | 0.782685    | 0.819291    | 0.775131    | 0.787914    | 0.842533    |
AUC      | 0.647277    | 0.606102    | 0.552362    | 0.596702    | 0.629992    |
```

Logistic regression has better accuracy on groups 1, 2, and 4, whereas boosted gradient has a better accuracy on groups 3 and 5. Logistic regression has a larger AUC for groups 3 and 4, while boosted gradient has a greater AUC on groups 1, 2, and 5, but these are so close to each other that they could change just by retraining the models. I expected boosted gradient to be the best performing, but my models don't seem to lead to that result