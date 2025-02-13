# Data Manipulation and Algorithm Testing

This exercise contains multiple Python scripts for data manipulation, algorithm testing, and database creation. The functionality includes:

- Calculating the running average
- Cleaning data
- Validating brackets
- Merging intervals
- Working with median arrays
- Explaining SQL queries
- Interacting with an SQLite database

## Files in the Project

- **running_average.py**: Calculates and prints the running average of a list of numbers.
- **data_cleaning.py**: Contains functions for cleaning and processing data, including handling missing values and outliers.
- **bracket_validation.py**: Validates if a given string has balanced brackets.
- **interval_merging.py**: Merges overlapping intervals in a list of intervals.
- **median_arrays.py**: Calculates the median of multiple arrays.
- **queries_explained.py**: Contains SQL query explanations and example queries.
- **create_database.sql**: SQL script to create a database and populate it with data.
- **test_algorithms.py**: Contains unit tests for all the Python algorithms in the project.

## How to Run the Scripts

1. **Download or Clone the Repository**:
   - If you haven't already, clone the repository or download the files to your local machine.

2. **Install Dependencies**:
   - This project requires Python 3.9 or higher. You can check your version by running:
     ```
     python --version
     ```
   - If you need to install Python, download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

3. **Install Required Libraries**:
   - Install all the necessary libraries by running the following command:
     ```
     pip install seaborn matplotlib scipy pandas pytest sqlite3
     ```

## Libraries Used

This project uses the following libraries:

- **Seaborn**: For statistical data visualization.
- **Matplotlib**: For creating plots and visualizations.
- **SciPy**: For scientific computing functions.
- **Pandas**: For data manipulation and analysis.
- **sqlite3**: For interacting with an SQLite database.
- **Random**: For generating random numbers (if used in any algorithms).
- **pytest**: For running unit tests.

## Running the Scripts

To run the scripts, open your terminal or command prompt, navigate to the directory where the file is located, and then execute the desired script using:
```
python data_cleaning.py
```

- Running Average script:
```
python running_average.py "[0.5, 3.0, 7.5, 14.0, 22.5, 33.0, 45.5, 60.0, 76.5, 95.0, 115.5, 138.0, 162.5, 189.0, 217.5, 248.0, 280.5, 315.0, 351.5]"
```

- Bracket Validation script:
```
python bracket_validation.py "{[BENFICA 1904]}"
```

- Merge Intervals script
```
python interval_merging.py "[[2, 4], [2, 5], [3, 6], [9, 11]]"
```

- Median Number Array script
```
python median_arrays.py "[[4, 2, 1], [2, 5], [7, 6]]"
```
- Create the database and populate with dummy data using:
```
python dummy_sql_data.py
```

- Run the queries using the script:
```
python queries_explained.py
```

## Setting Up the Database

To create the database, run the `create_database.sql` script in an SQLite database. To execute the script, use the following steps:

1. Open an SQLite command-line interface or use a database management tool (like DB Browser for SQLite).
2. Run the `create_database.sql` script.

## Running Tests

If you'd like to run the tests for the project, use pytest to ensure everything works correctly. Run the following command to execute the tests:
```
pytest test_algorithms.py
```

## Considerations
1. Algorithm Development:
I began by developing the Python scripts for the algorithms. After completing the scripts and conducting testing, I proceeded with the SQL exercise.

2. Testing the SQL Queries:
To ensure the correctness of my SQL queries, I decided to create a test database. I created a script, dummy_sql_data.py, which uses SQLite (since it's pre-installed) to generate a dummy database.

3. Core Task:
Once the algorithms and SQL tasks were completed, I focused on the core task.

4. Data Preparation:

I manually downloaded the necessary files and added them to the data folder of the project.
Upon opening the files, I realized that the column names, value ranges, and data types could be found in the .names file.
After successfully reading the data with the appropriate column names, I proceeded to address missing values and incorrect data types.

5. Data Type and Value Transformation:

I noticed that two columns contained data that should have been numerical but were represented as strings. I mapped these string values to their corresponding numerical values.
The missing values were represented as "?" rather than NaN, so I converted these question marks into NaN to properly handle the missing data.

6. Handling Missing Data:

With the data now in the correct format and all missing values converted to NaN, I focused on handling these missing values.

7. Choosing a Method for Missing Values:

I opted for the median imputation method instead of more complex machine learning approaches. This decision was driven by the fact that most missing values were concentrated in one column, and a simpler approach would be sufficient for low complexity.
It’s worth noting that no comparison between other methods (like mode, mean, KNN, regression, or data dropping) was conducted. The median is a reliable, robust method that is less affected by outliers.

8. Outlier Detection:

To detect outliers, I used the Z-score method, which standardizes the data and identifies values significantly different from the mean (most effective with normally distributed data).
Additionally, I created box plots for a visual representation of the outliers. Through this analysis, I concluded that the outliers were valid data points and represented at most ±5% of the data in a column. This insight allows for potential machine learning techniques, such as using a log scaler, to reduce the influence of outliers.

9. Correlation Analysis:

I then explored the correlations between the columns to identify which attributes had positive or negative relationships with one another.

10. Further Analysis:

While further analysis could have been conducted (e.g., finding the number of BMW cars or identifying the most expensive cars), this was not performed in this particular task.
Regarding the automation of the ETL process using Apache Airflow, since I wasn’t fully familiar with it, I didn’t dive deeply into learning it. However, from the documentation I reviewed, it seems that a DAG file is created where each task, such as handling missing values (which should be in its own .py file), is added and scheduled to run in a specific order. From what I understand, this will be helpful for automating and scheduling the ETL process in my own project, so I won’t have to manually run the .py script every friday to fetch data for my football league from the premier league API.