import sqlite3
import pandas as pd

# connect to the database
conn   = sqlite3.connect("company_db.sqlite")
cursor = conn.cursor()

# query A: list of employeesin the market_insights department from the Plzen, Czech Republic sorted by those who currently have a salary above their maximum_ref_value.
# bonus:   sorted by employees who have been above that max ref for the longest period of time.
query_a = """
WITH Recent_Salaries AS (
    -- Get the most recent month_id for each employee
    SELECT employee_id, MAX(month_id) AS recent_month
    FROM  tb_salary
    GROUP BY employee_id
),
Overpaid_Employees AS (
    -- Get employees whose salary is above the reference maximum
    SELECT s.employee_id, s.month_id, s.salary_value, r.maximum_ref_value
    FROM tb_salary s
    JOIN tb_employee e         ON s.employee_id = e.employee_id
    JOIN tb_reference_salary r ON e.position    = r.position
    JOIN Recent_Salaries rs    ON s.employee_id = rs.employee_id AND s.month_id = rs.recent_month
    WHERE e.department = 'market_insights'
    AND e.district     = 'Plzen'
    AND e.country      = 'Czech Republic'
    AND r.year = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER) -- Extract year from month_id
    AND s.salary_value > r.maximum_ref_value
),
Overpaid_Duration AS (
    -- Count how many months each employee has exceeded the max reference value
    SELECT s.employee_id, COUNT(*) AS months_above_max
    FROM tb_salary s
    JOIN tb_employee e         ON s.employee_id = e.employee_id
    JOIN tb_reference_salary r ON e.position    = r.position
    WHERE e.department = 'market_insights'
    AND e.district     = 'Plzen'
    AND e.country      = 'Czech Republic'
    AND r.year         = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER)
    AND s.salary_value > r.maximum_ref_value
    GROUP BY s.employee_id
)

SELECT o.employee_id, e.position, e.department, e.country, e.district,
       o.salary_value, o.maximum_ref_value, o.month_id, d.months_above_max
FROM Overpaid_Employees o
JOIN tb_employee e       ON o.employee_id = e.employee_id
JOIN Overpaid_Duration d ON o.employee_id = d.employee_id
ORDER BY d.months_above_max DESC, o.salary_value - o.maximum_ref_value DESC;
"""

# query B: list of employees and their total salary of supercars from the Woking Borough district in England in 2010 sorted by those who had the lowest annual salary
query_b = """
WITH annual_salary AS (
    SELECT s.employee_id, 
           SUM(s.salary_value) AS total_salary
    FROM tb_salary s
    WHERE s.month_id BETWEEN 201001 AND 201012  
    GROUP BY s.employee_id
)
SELECT e.employee_id,
       e.position, 
       e.department, 
       e.country, 
       e.district, 
       a.total_salary
FROM tb_employee e
JOIN annual_salary a ON e.employee_id = a.employee_id
WHERE e.department = 'supercars'
  AND e.district   = 'Woking Borough'
  AND e.country    = 'Surrey (England)'
ORDER BY a.total_salary ASC;
"""

# run the queries
cursor.execute(query_a)
rows = cursor.fetchall()
rows = [row[:-1] for row in rows]
df = pd.DataFrame(rows, columns=["employee_id", "position", "department", "country", "district", "salary_value", "maximum_ref_value", "month_id"])
print(df)
print("---------------------------------------------------------------------------------------------------------------")

cursor.execute(query_b)
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["employee_id", "position", "department", "country", "district", "total_salary_2010"])
print(df)
print("---------------------------------------------------------------------------------------------------------------")

# close the connection
conn.close()