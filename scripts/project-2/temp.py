import pandas as pd

filepath = "../../data/project-2/NPHR7HFL.DTA"
df = pd.read_stata(filepath)
# df.to_csv("temp.csv")
print(df.tail())