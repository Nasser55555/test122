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
# Rename the columns
subset_df.columns = ['seqn','smoking','gender', 'age','education','weight','height','bmi']

# Display the updated DataFrame to confirm
print(subset_df.head())
# Check for duplicates
duplicates = subset_df.duplicated()

# Count how many duplicates exist
print("Number of duplicate rows:", duplicates.sum())

# Drop the 'seqn' column
subset_df = subset_df.drop(columns=['seqn'])

# Show the updated DataFrame
print(subset_df.head())

# Count missing (NaN) values in each column
missing_values = subset_df.isna().sum()

# Display the result
print("Missing values per column:")
print(missing_values)

# Replace missing values in 'education' with the median
subset_df['education'].fillna(subset_df['education'].median(), inplace=True)

# Replace missing values in 'weight', 'height', 'bmi' with their respective means
subset_df['weight'].fillna(subset_df['weight'].mean(), inplace=True)
subset_df['height'].fillna(subset_df['height'].mean(), inplace=True)
subset_df['bmi'].fillna(subset_df['bmi'].mean(), inplace=True)

# Display descriptive statistics
print(subset_df.describe())

# Define a function to detect outliers using IQR
def detect_outliers_iqr(df):
    outliers = {}
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outlier_rows = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        outliers[column] = outlier_rows_

# Function to remove outliers using IQR
def remove_outliers_iqr(df):
    df_clean = df.copy()
    for column in df_clean.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df_clean[column].quantile(0.25)
        Q3 = df_clean[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_clean = df_clean[(df_clean[column] >= lower_bound) & (df_clean[column] <= upper_bound)]
    return df_clean

# Apply the function to remove outliers
subset_df_clean = remove_outliers_iqr(subset_df)

# Show the new shape of the cleaned dataset
print("New dataset shape after removing outliers:", subset_df_clean.shape)


# Replace codes in 'smoking'
subset_df_clean['smoking'] = subset_df_clean['smoking'].replace({
    1: 'yes', 
    2: 'no', 
    7: pd.NA, 
    8: pd.NA
})

# Replace codes in 'gender'
subset_df_clean['gender'] = subset_df_clean['gender'].replace({
    1: 'male', 
    2: 'female'
})

# Replace codes in 'education'
subset_df_clean['education'] = subset_df_clean['education'].replace({
    1: '<9th grade', 
    2: '9-11th grade', 
    3: 'HS or GED', 
    4: 'Some college / AA', 
    5: 'College or above', 
    7: 'Other', 
    8: 'Other'
})

import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

# Pairplot for numeric columns only
numeric_cols = subset_df_clean.select_dtypes(include=['number']).columns
sns.pairplot(subset_df_clean[numeric_cols], diag_kind="kde", corner=True)
plt.suptitle("Pairwise Relationships Between Variables", y=1.02)
plt.show()

sns.histplot(subset_df_clean['bmi'], kde=True)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Count")
plt.show()

# Save the cleaned dataset as a CSV file
subset_df_clean.to_csv("cleaned_health_dataset.csv", index=False)
