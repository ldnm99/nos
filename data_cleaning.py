import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_dataset(df):
    """
    Analyze the dataset and return a summary of the dataset.
    """
    summary = {
        'shape': df.shape,
        'info': df.info(),        # This directly prints the info
        'head': df.head(),        # Preview the first few rows of the dataset
        'describe': df.describe() # Summary statistics of the dataset
    }
    print("Dataset Summary:")
    print(f"Shape of dataset: {summary['shape']}")
    print("\nFirst few rows of the dataset:")
    print(summary['head'])
    print("\nSummary statistics of the dataset:")
    print(summary['describe'])
    #  using info(), head() and shape to get a summary of the dataset and its columns we find there are:
    #    - 205 rows and 26 columns,
    #    - missing values in 7 columns,
    #    - columns with dtype as 'object' which is pandas default for text data but for the purpose of demonstrating data cleaning it will be converted to string dtype.
    #    - columns num-of-doors and num-of-cylinders have values that are strings but can and should be int dtype.
    #    - missing data is represented by '?' 
   
def analyze_missing_values(df):
    """
    Analyze missing values in the dataset and return a summary.
    """
    # replaced the '?' with NaN 
    df.replace('?', pd.NA, inplace=True)

    # counted the missing values in each column using the isnull() method and verified most missing values are in the 'normalized-losses' column
    number_missing_values = df.isnull().sum()
    # calculated percentage of missing values
    missing_percentage = (number_missing_values / len(df)) * 100
    
    # summary dataframe
    missing_summary = pd.DataFrame({
        'Missing Count':      number_missing_values,
        'Missing Percentage': missing_percentage
    })
    print(missing_summary)
    
    # view missing data with a heatmap for better analysis
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Missing Values Heatmap')
    plt.show()

def mapping_columns(df):
    """
    Mapping the 2 columns to the correct data.
    """
    # first i converted 'num-of-doors' and 'num-of-cylinders' to int dtype by mapping the string values to the int values 
    df['num-of-doors']     = df['num-of-doors'].map({'two': 2,
                                                      'four': 4})
    df['num-of-cylinders'] = df['num-of-cylinders'].map({'two': 2,
                                                          'three': 3,
                                                            'four': 4,
                                                              'five': 5,
                                                                'six': 6,
                                                                  'eight': 8,
                                                                    'twelve': 12})
    return df

def convert_columns_dtype(df, dtype, *columns):
    """
    Convert columns to specified dtype
    """
    for column in columns:
            df[column] = df[column].astype(dtype)
    return df

def to_numeric(df, *columns):
    """
    Convert specified columns to numeric, coercing errors to NaN.
    """
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def converter(df):
    # converted the columns with dtype as 'object' to string dtype
    string_columns = ['make', 'fuel-type', 'aspiration', 'body-style', 'drive-wheels', 'engine-location', 'engine-type', 'fuel-system']
    df = convert_columns_dtype(df, 'string', string_columns)

    # columns with continuous values (no missing values) to float dtype
    float_columns = ['curb-weight', 'engine-size', 'compression-ratio', 'city-mpg', 'highway-mpg']
    df = convert_columns_dtype(df, 'float', float_columns)

    # converted the columns to numeric using the to_numeric function
    df = to_numeric(df,'normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price')
    return df

def fill_missing_values(df, *columns):
    """
    Fill missing values with the median of each column.
    """
    for column in columns:
        median = df[column].median()
        df[column] = df[column].fillna(median)
    return df

def find_outliers_zscore(df, columns, threshold = 3):
    outliers = {}
    for column in columns:
        z_scores = stats.zscore(df[column])  
        data     = df[(z_scores > threshold) | (z_scores < -threshold)]
        if not data.empty:  
            outliers[column] = data
    return outliers

def report_outliers(outliers_zscore, df):
    """
    Report the number of outliers and their percentage for each column with outliers.
    """
    for column, outlier_data in outliers_zscore.items():
        num_outliers = len(outlier_data)  # Count the number of outliers
        total_rows = len(df)  # Total number of rows in the dataset
        outlier_percentage = (num_outliers / total_rows) * 100  # Calculate percentage of outliers
        print(f"Number of outliers in {column}: {num_outliers} ({outlier_percentage:.2f}%)")
        
        # Optionally: Boxplot to visualize outliers
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot for {column}')
        plt.show()

def correlation_matrix(df, numerical_columns):
    """
    Compute the correlation matrix using Pearson correlation.
    """
    correlation_matrix = df[numerical_columns].corr(method='pearson')
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # plot the correlation matrix using a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Pearson Correlation Matrix')
    plt.show()
    
def main():
    # the file imports-85.names contains the names of the columns in the dataset
    # the file imports-85.data contains the data in the dataset
    # File path
    data_file  = r"C:\Users\lourencomarvao\nos\data\imports-85.data"

    column_names = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
     'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
     'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
     'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
     'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

    # read the dataset 
    df = pd.read_csv(data_file, names=column_names)

    # analyze the dataset
    analyze_dataset(df)

    # analyze missing values in the dataset
    print('----------------------------Missing Values----------------------------------------')  
    analyze_missing_values(df)

    # Assumption:
    # 1. The missing values are just unknown values and not errors in the dataset.

    # mapping the columns to the correct data
    df = mapping_columns(df)

    # convert the columns to the correct dtype
    df = converter(df)

    # now the data is ready to deal with the missing values
    # there are different ways to handle missing values such as:
    #   - deleting the column with missing values, 
    #   - deleting the rows   with missing values, 
    #   - filling the missing values with the mean, median or frequency of values in the column
    #   - using a model like knn to predict the missing values

    # fill the missing values with the mean of the column using the fill_missing_values function
    df = fill_missing_values(df, 'normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price')

    # all that remains is handle the 2 missing values in the 'num-of-doors' column
    # i used the frequency of the column to fill the missing values and changed the dtype to int from float
    frequency_result   = stats.mode(df['num-of-doors'], nan_policy='omit') 
    df['num-of-doors'] = df['num-of-doors'].fillna(frequency_result[0])
    df['num-of-doors'] = df['num-of-doors'].astype('int')

    # count the new missing values
    print('----------------------------New Missing Values----------------------------------------')  
    analyze_missing_values(df)
    print('----------------------------Data Cleaning Done!---------------------------------------')

    # find outliers using the z-score method
    # using the numerical columns
    numerical_columns = df.select_dtypes(include=['float', 'int']).columns
    outliers_zscore   = find_outliers_zscore(df, numerical_columns)

    report_outliers(outliers_zscore, df)

    # Assumption:
    # 2. The outliers are valid data points and not errors in the dataset.
    # 3. The outliers are in the data range given in imports-85.names.
    # 4. The outliers are significant data points that should not be removed.
    # 5. The number of outliers is not too high to affect the analysis and future model training.

    # The data is now cleaned and ready for further analysis.

    # Start by identifying which features are most important in the price of a car by computing the correlation matrix.

    # correlation matrix using Pearson correlation
    correlation_matrix(df, numerical_columns)

    # The correlation matrix shows the relationship between the numerical columns in the dataset.
    # More specifically: 'engine-size', 'curb-weight' have the strongest positive correlation with 'price' while surprisingly 'symboling', 'num-of-doors' and 'stroke' have basically no influence on the price.
    # The columns 'city-mpg' and 'highway-mpg' have a strong negative correlation with 'price' which means as the miles per gallon increase the price decreases.
    # Cars with bigger engines have more horsepower and are heavier.
    # Cars with large width and legth are heavier and have lower mpg aka fuel efficiency.

if __name__ == "__main__":
    main()
    