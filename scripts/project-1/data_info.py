import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.5f' % x)

filename = "../../data/project-1/austin.csv"

df = pd.read_csv(filename)

print(df.describe().to_markdown(tablefmt="grid"))

# print(df.describe().apply(lambda s: s.apply(lambda x: format(x, 'g'))))

# prices = df['prices']
# no_beds = df['no_beds']
# baths = df['baths']
# sqft = df['sqft']

# def info(col_name, col):
#     print(col_name.title() + ":")
#     mean = np.mean(col)
#     median = np.median(col)
#     std = np.std(col)
#     print("Mean: ",mean)
#     print("Median: ",median)
#     print("Standard Deviation: ",std,'\n')

# info('prices',prices)
# info('bedrooms',no_beds)
# info('baths',baths)
# info('square footage',sqft)