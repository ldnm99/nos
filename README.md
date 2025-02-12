This exercise contains multiple Python scripts for data manipulation, algorithm testing, and database creation. It includes functionality for calculating the running average, cleaning data, validating brackets, merging intervals, working with median arrays, explaining SQL queries, and interacting with an SQLite database.

Files in the Project
running_average.py: Calculates and prints the running average of a list of numbers.
data_cleaning.py: Contains functions for cleaning and processing data, such as handling missing values and outliers.
bracket_validation.py: Validates if a given string has balanced brackets.
interval_merging.py: Merges overlapping intervals in a list of intervals.
median_arrays.py: Calculates the median of multiple arrays.
queries_explained.py: Contains SQL query explanations and example queries.
create_database.sql: SQL script to create a database and populate it with data.
test_algorithms.py: Contains unit tests for all the Python algorithms in the project.

How to Run the Scripts
1. Download or Clone the Repository:
If you haven't already, clone the repository or download the files to your local machine.

2. Install Dependencies:
This project requires Python 3.9 or higher. You can check your version by running:
    python --version

If you need to install Python, download it from the official Python website: https://www.python.org/downloads/

3. Set Up a Virtual Environment (Optional but Recommended):
It's recommended to use a virtual environment to isolate your project dependencies. Here's how to set it up:
    python -m venv venv

Activate the virtual environment:

On Windows:
    venv\Scripts\activate

4. Install Required Libraries:
Install all the necessary libraries by running the following:
    pip install seaborn matplotlib scipy pandas pytest sqlite3

Libraries Used
This project uses the following libraries:

Seaborn: For statistical data visualization.
Matplotlib: For creating plots and visualizations.
SciPy: For scientific computing functions.
Pandas: For data manipulation and analysis.
sqlite3: For interacting with an SQLite database.
Random: For generating random numbers (if used in any algorithms).
pytest: For running unit tests.


5. Run the Script:
To run the scripts, open your terminal or command prompt, navigate to the directory where the file is located, and then execute:
    python data_cleaning.py
    python running_average.py
    python bracket_validation.py
    python interval_merging.py
    python median_arrays.py
    python queries_explained.py

6. Setting Up the Database
To create the database, you can run the create_database.sql script in an SQLite database. To execute the script, use the following steps:

Open an SQLite command-line interface or use a database management tool (like DB Browser for SQLite).
    Run the create_database.sql script:

7. Running Tests 
If you'd like to run the tests for the project, use pytest to ensure everything works correctly.

Run the following command to execute the tests:
    pytest test_algorithms.py

