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

Plot of Mean Error:

![Lin Reg ME](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/lin-reg-me.png)

### Random Forest Validation

Plot of the difference between the real and the predicted population of Costa Rica:

![Random Forest Diff Sums](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/rf-diff-sums.png)

Plot of Mean Error:

![Random Forest ME](https://raw.githubusercontent.com/pasolano/appml/main/data/project-3/images/rf-me.png)

## Write a report assessing the two approaches and which of the two models was more accurate. Be sure to account for spatial variation throughout your selected location and provide substantive explanations for why those variations occurred

```R
# Real population
> cellStats(cri_pop15, sum)
[1] 4520671

# Linear regression predicted population
> lin_reg_pop_sums <- cellStats(population_sums, sum)
> lin_reg_pop_sums
[1] 4514702

# Linear regression error sum
> lin_reg_diff_sums <- cellStats(diff_sums, sum)
> lin_reg_diff_sums
[1] -11821.27

# Random forest predicted population
> rf_pop_sums <- cellStats(population_sums, sum)
> rf_pop_sums
[1] 4511925

# Random forest error sum
> rf_diff_sums <- cellStats(diff_sums, sum)
> rf_diff_sums
[1] -308.873
```
