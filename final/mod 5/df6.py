#Filling missing values using fillna(), replace() and interpolate()
import pandas as pd
import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
print("fillna")# filling missing value using fillna()
print(df.fillna(0))
print("interpolation")#filling the NaN values by interpolation
print(df.interpolate())
print("replacing nan with -1")#replacing the nan values with -1
print(df.replace(np.nan,-1))
print("dropping the rows containing null values")#dropping the rows containing null values
print(df.dropna())