import sqlite3
import random

# connect to SQLite 
conn = sqlite3.connect("company_db.sqlite")
cursor = conn.cursor()

# drop tables if they exist (for rerunning the script)
cursor.executescript("""
DROP TABLE IF EXISTS tb_employee;
DROP TABLE IF EXISTS tb_salary;
DROP TABLE IF EXISTS tb_reference_salary;

CREATE TABLE tb_employee (
    employee_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    position TEXT,
    department TEXT,
    country TEXT,
    district TEXT
);

CREATE TABLE tb_salary (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    month_id INTEGER,
    employee_id INTEGER,
    salary_value REAL,
    FOREIGN KEY(employee_id) REFERENCES tb_employee(employee_id)
);

CREATE TABLE tb_reference_salary (
    position TEXT,
    year INTEGER,
    maximum_ref_value REAL,
    minimum_ref_value REAL,
    PRIMARY KEY(position, year)
);
""")

# sample employees
employees = [
    (1, 30, 'F', 'Manager',    'HR',              'Czech Republic',   'Plzen'),
    (2, 35, 'F', 'Mechanic',   'supercars',       'Surrey (England)', 'Woking Borough'),
    (3, 40, 'M', 'Lawyer',     'Tax',             'Czech Republic',   'Plzen'),
    (4, 28, 'M', 'Engineer',   'supercars',       'Surrey (England)', 'Woking Borough'),
    (5, 55, 'M', 'Manager',    'market_insights', 'Czech Republic',   'Plzen'),
    (6, 25, 'F', 'Mechanic',   'supercars',       'Surrey (England)', 'Lisbon'),
    (7, 54, 'M', 'Consultant', 'market_insights', 'Czech Republic',   'Plzen'),
]

cursor.executemany("INSERT INTO tb_employee VALUES (?, ?, ?, ?, ?, ?, ?)", employees)

# generate salaries for 2010-2023
salaries = []
for emp_id in range(1, 8):          # nº employees
    for year in range(2010, 2024):  # year
        for month in range(1, 13):  # month
            month_id = int(f"{year}{month:02d}")
            if emp_id in [5, 7]:
                salary = random.randint(5500, 7000) # Random salary to meet the query conditions
            else:
                salary = random.randint(2000, 4500)  # Random salary
            salaries.append((month_id, emp_id, salary))

cursor.executemany("INSERT INTO tb_salary (month_id, employee_id, salary_value) VALUES (?, ?, ?)", salaries)

# base reference salary for positions
base_reference_salaries = {
    'Consultant':  (5000, 3000),
    'Mechanic':    (4500, 2800),
    'Engineer':    (4800, 3000),
    'Lawyer':      (5200, 3500),
    'Manager':     (5000, 2200) 
}
reference_salaries = []

# reference salaries for each year from 2010 to 2023
for year in range(2010, 2024):
    for position, (max_salary, min_salary) in base_reference_salaries.items():
        # annual payrise of 1% (inflation)
        new_max = round(max_salary * (1.01 ** (year - 2023)), 2)
        new_min = round(min_salary * (1.01 ** (year - 2023)), 2)
        reference_salaries.append((position, year, new_max, new_min))

cursor.executemany("INSERT INTO tb_reference_salary VALUES (?, ?, ?, ?)", reference_salaries)

conn.commit()
conn.close()

print("Dummy data created")

