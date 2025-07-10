import pandas as pd
df = pd.read_csv('/Users/zakaria/Desktop/ sas/DataSet.csv')
df.head()

# List of columns to keep
columns_to_keep = ['SEQN','SMQ020', 'RIAGENDR', 'RIDAGEYR','DMDEDUC2','BMXWT', 'BMXHT', 'BMXBMI']

# Create a new subset DataFrame
subset_df = df[columns_to_keep]

# Display the first few rows to confirm
print(subset_df.head())
# Display general info about the subset DataFrame
subset_df.info()
