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
accuracy           0.778617
average_loss       0.506625
loss               0.506728
global_step     1620.000000
AUC                0.657179
```

Added the derived feature columns
```
accuracy           0.779198
average_loss       0.501730
loss               0.501896
global_step     1620.000000
AUC                0.657179
```

![ROC Wealth 1](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth1.png?raw=true)

### Wealth Group 2

Logistic regression model
```
accuracy           0.806508
average_loss       0.488187
loss               0.488976
global_step     1620.000000
AUC                0.560684
```

Added the derived feature columns
```
accuracy           0.806508
average_loss       0.487599
loss               0.488320
global_step     1620.000000
AUC                0.560684
```

![ROC Wealth 2](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth2.png?raw=true)

### Wealth Group 3

Logistic regression model
```
accuracy           0.787333
average_loss       0.521808
loss               0.521463
global_step     1620.000000
AUC                0.524986
```

Added the derived feature columns
```
accuracy           0.785009
average_loss       0.526242
loss               0.525871
global_step     1620.000000
AUC                0.524986
```

![ROC Wealth 3](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth3.png?raw=true)

### Wealth Group 4

Logistic regression model
```
accuracy           0.776293
average_loss       0.530631
loss               0.530994
global_step     1620.000000
AUC                0.586630
```

Added the derived feature columns
```
accuracy           0.779779
average_loss       0.520418
loss               0.520858
global_step     1620.000000
AUC                0.586630
```

![ROC Wealth 4](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth4.png?raw=true)

### Wealth Group 5

Logistic regression model
```
accuracy           0.851249
average_loss       0.403903
loss               0.403707
global_step     1620.000000
AUC                0.619105
```

Added the derived feature columns
```
accuracy           0.849506
average_loss       0.394308
loss               0.394267
global_step     1620.000000
AUC                0.619105
```

![ROC Wealth 5](https://github.com/pasolano/appml/blob/main/data/project-2/images/roc_wealth5.png?raw=true)

## Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. Provide evaluative metrics including a measure of accuracy and AUC. Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results

## Analyze all four models. According to the evaluation metrics, which model produced the best results? Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?