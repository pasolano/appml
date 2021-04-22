# Project 3

For this project, I chose Costa Rica as my country. I've been wanting to do a project on it for some time now, since my dad is from there. Below is a map.

![Costa Rica](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/costa-rica.png)

And here is a map of the actual population of Costa Rica

![Costa Rica Pop](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/pop.png)

## Using two machine learning methods predict population values at 100 x 100 meter resolution throughout your selected country

### Linear Regression Predictions

![Lin Reg Pop Sums](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/lin-reg-pop-sums.png)

### Random Forest Predictions

![Random Forest Pop Sums](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/rf-pop-sums.png)

## Validate the two models using different methods presented in this class

### Linear Regression Validation

Plot of the difference between the real and the predicted population of Costa Rica:

![Lin Reg Diff Sums](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/lin-reg-diff-sums.png)

Plot of Mean Absolute Error:

![Lin Reg MAE](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/lin-reg-mae.png)

### Random Forest Validation

Plot of the difference between the real and the predicted population of Costa Rica:

![Random Forest Diff Sums](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/rf-diff-sums.png)

Plot of Mean Absolute Error:

![Random Forest MAE](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/rf-mae.png)

## Write a report assessing the two approaches and which of the two models was more accurate. Be sure to account for spatial variation throughout your selected location and provide substantive explanations for why those variations occurred

```R
# Real population
> cellStats(cri_pop15, sum)
[1] 4520671

# Linear regression predicted population
> cellStats(population_sums, sum)
[1] 4514702

# Linear regression error sum
> cellStats(abs(diff_sums), sum)
[1] 6324472

# Random forest predicted population
> cellStats(population_sums, sum)
[1] 4511925

# Random forest error sum
> cellStats(abs(diff_sums), sum)
[1] 4671728
```

As can be seen above, my linear regression model was slightly closer to estimating the total population of Costa Rica (being 5969 people away from the correct amount), while random forest was 8746 people away. Both of these estimates are very close to the total population, but linear regression got closer to the actual population. However, the sum of the differences between the actual population and the predicted populations in each area is much larger for the linear regression than for the random forest. For a final method of measuring the accuracy of each model, I plotted the mean absolute error for both. They performed similarly to each other to tell which one had a smaller error from these charts, but it looks like linear regression might have a color that is slightly higher on its scale than random forest's. Even though linear regression probably performed best during this project, both linear regression and random forest have the same problems when it comes to spatial variation. As can be seen from the "difference" plots, both models tend to have lots of negative error near areas with larger-than-average populations. This is probably because Costa Rica has such a stark contrast between areas with lots of people and areas with almost none -- the models can't accurately predict extreme cases with only a couple of factors, especially when predicting low numbers usually renders favorable results. The MAE plots also show that all the errors happen around populated areas, further confirming this theory.
