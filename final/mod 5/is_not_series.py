import pandas as pd
# Create a Series with some missing values
s = pd.Series([1, None, 3, None, 5])
print("\nOriginal Series:")
print(s)

# Check for missing values in the Series
print("\nSeries with isnull():")
print(s.isnull())

# Check for non-missing values in the Series
print("\nSeries with notnull():")
print(s.notnull())
