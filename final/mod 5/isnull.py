import pandas as pd

# Create a DataFrame with some missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Check for missing values
print("\nDataFrame with isnull():")
print(df.isnull())
