# Response for 3/10

## Import the households dataset for your selected country and create a data frame with a variable that describes each of the following

- household ID
- unit
- weights
- location
- size
- gender
- age
- education
- wealth

```
hv104 == sex
hv105 == age
hv106 == education

> print(hhs)
          hhid unit  weights location size hv104_06 hv104_07 hv104_08 hv104_09 hv104_10 hv104_11 hv104_12 hv104_13 hv104_14 hv104_15
1        1   1    1 1.084696     ilam    2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2        1   5    1 1.084696     ilam    2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3        1   9    1 1.084696     ilam    3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4        1  13    1 1.084696     ilam    3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5        1  17    1 1.084696     ilam    7        2        2       NA       NA       NA       NA       NA       NA       NA       NA
6        1  21    1 1.084696     ilam    4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7        1  25    1 1.084696     ilam    3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8        1  29    1 1.084696     ilam    4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv104_16 hv104_17 hv104_18 hv104_19 hv104_20 hv104_21 hv104_22 hv104_23 hv104_24 hv104_25 hv104_26 hv104_27 hv104_28 hv104_29
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv104_30 hv104_31 hv104_32 hv104_33 hv104_34 hv104_35 hv104_36 hv104_37 hv104_38 hv105_01 hv105_02 hv105_03 hv105_04 hv105_05
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       90       89       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       50       47       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       54       47       22       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       55       55       15       NA       NA
5       NA       NA       NA       NA       NA       NA       NA       NA       NA       71       65       36       31        8
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       51       43       24       20       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       52       50       20       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       39       33        7        6       NA
  hv105_06 hv105_07 hv105_08 hv105_09 hv105_10 hv105_11 hv105_12 hv105_13 hv105_14 hv105_15 hv105_16 hv105_17 hv105_18 hv105_19
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5        4       33       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv105_20 hv105_21 hv105_22 hv105_23 hv105_24 hv105_25 hv105_26 hv105_27 hv105_28 hv105_29 hv105_30 hv105_31 hv105_32 hv105_33
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv105_34 hv105_35 hv105_36 hv105_37 hv105_38 hv106_01 hv106_02 hv106_03 hv106_04 hv106_05 hv106_06 hv106_07 hv106_08 hv106_09
1       NA       NA       NA       NA       NA        0        0       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA        2        0       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA        1        1        3       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA        2        1        2       NA       NA       NA       NA       NA       NA
5       NA       NA       NA       NA       NA        0        0        3        3        1        0        3       NA       NA
6       NA       NA       NA       NA       NA        1        0        2        3       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA        2        0        2       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA        3        2        0        0       NA       NA       NA       NA       NA
  hv106_10 hv106_11 hv106_12 hv106_13 hv106_14 hv106_15 hv106_16 hv106_17 hv106_18 hv106_19 hv106_20 hv106_21 hv106_22 hv106_23
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv106_24 hv106_25 hv106_26 hv106_27 hv106_28 hv106_29 hv106_30 hv106_31 hv106_32 hv106_33 hv106_34 hv106_35 hv106_36 hv106_37
1       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
2       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
3       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
4       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
5       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
6       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
7       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
8       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA       NA
  hv106_38 wealth
1       NA      2
2       NA      4
3       NA      3
4       NA      3
5       NA      3
6       NA      3
7       NA      2
8       NA      3
 [ reached 'max' / getOption("max.print") -- omitted 11032 rows ]
```

## Pivot the persons columns within your households data to a long format in order to produce a similarly specified dataset that describes all persons residing within all households

```
# A tibble: 6,883 x 5
    size gender   age edu   wealth
   <dbl> <fct>  <dbl> <fct> <fct> 
 1     7 2          4 0     3     
 2     7 2         33 3     3     
 3     7 2         21 3     3     
 4     7 1         75 0     3     
 5     6 2         64 0     2     
 6     8 2          9 1     1     
 7     8 1          7 1     1     
 8     8 2         73 0     1     
 9     6 1          0 0     1     
10     7 1          1 0     3     
# ... with 6,873 more rows
```

## Using this data frame describing all persons standardize, normalize and percentize your variables and visualize each post transformed dataset as a heatmap that illustrates the heterogeneity of the combination of patterns

### Raw Data

![Raw Data](https://github.com/pasolano/appml/blob/main/data/mar-10/raw.png?raw=true)

### Standardized Data

![Standardized Data](https://github.com/pasolano/appml/blob/main/data/mar-10/scale.png?raw=true)

### Normalized Data

![Normalized Data](https://github.com/pasolano/appml/blob/main/data/mar-10/normal.png?raw=true)

### Percentized Data

![Percentalized Data](https://github.com/pasolano/appml/blob/main/data/mar-10/percent.png?raw=true)
