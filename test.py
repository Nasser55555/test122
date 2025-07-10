import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/zakaria/Desktop/ sas/DataSet.csv')

# Display the shape (number of rows, number of columns)
print("Dataset dimensions:", df.shape)
# List all column names
print("Available columns:")
print(df.columns)
