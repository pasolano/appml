# Project 3

## UNDER CONSTRUCTION

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

As can be seen above, my linear regression model was slightly closer to estimating the total population of Costa Rica (being 5969 people away from the correct amount), while random forest was 8746 people away. Both of these estimates are very close to the total population, but linear regression got closer to the actual population. However, the sum of the differences between the actual population and the predicted populations in each area is much larger for the linear regression than for the random forest. For a final method of measuring the accuracy of each model, I plotted the mean error for both. The coloring for both of them is a little misleading, but they performed similarly to each other.
