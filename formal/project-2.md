# Project 2, due Wednesday, March 24th by midnight

## Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)? Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? Provide justification for your selected penalty value? Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes

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

![LR AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/lr_auc.png?raw=true)

## Using the R script provided, set up your random forest model and produce the AUC - ROC values for the randomly selected predictors, and the minimal node size, again with wealth as the target. How did your random forest model fare when compared to the penalized logistic regression? Provide your ROC plots and interpret them. Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?

![RF Res](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_res.png?raw=true)

![RF LR AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_lr_auc.png?raw=true)

![RF AUC](https://github.com/pasolano/appml/blob/main/data/project-2/images/rf_auc.png?raw=true)

![Last RF Fit](https://github.com/pasolano/appml/blob/main/data/project-2/images/last_rf_fit.png?raw=true)

## Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target. Apply the linear classifier to the feature columns and determine the accuracy, AUC and other evaluative metrics towards each of the different wealth outcomes. Then continue with your linear classifier adding the derived feature columns you have selected in order to extend capturing combinations of correlations (instead of learning on single model weights for each outcome). Again produce your ROC curves and interpret the results

## Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. Provide evaluative metrics including a measure of accuracy and AUC. Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results

## Analyze all four models. According to the evaluation metrics, which model produced the best results? Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?
