import pandas as pd
import numpy as np
import dataframe_image as dfi

pd.set_option('display.float_format', lambda x: '%.5f' % x)

filename = "../../data/project-1/austin.csv"

df = pd.read_csv(filename)

# save dataframe describing features and labels to dataframe
dfi.export(df.describe(), '../../data/project-1/describe.png', table_conversion='matplotlib')