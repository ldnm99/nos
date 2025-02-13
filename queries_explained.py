import sqlite3
import pandas as pd

def query_a(cursor):
    query = """
    WITH Recent_Salaries AS (
        SELECT employee_id, MAX(month_id) AS recent_month
        FROM tb_salary
        GROUP BY employee_id
    ),
    Overpaid_Employees AS (
        SELECT s.employee_id, s.month_id, s.salary_value, r.maximum_ref_value
        FROM tb_salary s
        JOIN tb_employee e ON s.employee_id = e.employee_id
        JOIN tb_reference_salary r ON e.position = r.position
        JOIN Recent_Salaries rs ON s.employee_id = rs.employee_id AND s.month_id = rs.recent_month
        WHERE e.department = 'market_insights'
        AND e.district = 'Plzen'
        AND e.country = 'Czech Republic'
        AND r.year = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER)
        AND s.salary_value > r.maximum_ref_value
    ),
    Overpaid_Duration AS (
        SELECT s.employee_id, COUNT(*) AS months_above_max
        FROM tb_salary s
        JOIN tb_employee e ON s.employee_id = e.employee_id
        JOIN tb_reference_salary r ON e.position = r.position
        WHERE e.department = 'market_insights'
        AND e.district = 'Plzen'
        AND e.country = 'Czech Republic'
        AND r.year = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER)
        AND s.salary_value > r.maximum_ref_value
        GROUP BY s.employee_id
    )
    SELECT o.employee_id, e.position, e.department, e.country, e.district,
           o.salary_value, o.maximum_ref_value, o.month_id, d.months_above_max
    FROM Overpaid_Employees o
    JOIN tb_employee e ON o.employee_id = e.employee_id
    JOIN Overpaid_Duration d ON o.employee_id = d.employee_id
    ORDER BY d.months_above_max DESC, o.salary_value - o.maximum_ref_value DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    rows = [row[:-1] for row in rows]
    return pd.DataFrame(rows, columns=["employee_id", "position", "department", "country", "district", "salary_value", "maximum_ref_value", "month_id"])

def query_b(cursor):
    query = """
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
      AND e.district = 'Woking Borough'
      AND e.country = 'Surrey (England)'
    ORDER BY a.total_salary ASC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    return pd.DataFrame(rows, columns=["employee_id", "position", "department", "country", "district", "total_salary_2010"])

def main():
    conn = sqlite3.connect("company_db.sqlite")
    cursor = conn.cursor()

    # Run and display results for query A
    df_a = query_a(cursor)
    print(df_a)
    print("---------------------------------------------------------------------------------------------------------------")

    # Run and display results for query B
    df_b = query_b(cursor)
    print(df_b)
    print("---------------------------------------------------------------------------------------------------------------")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
