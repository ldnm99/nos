import sqlite3
import pandas as pd

def query_a(cursor):
    query = """
    WITH Recent_Salaries AS (                               -- Creates subquery to get the most recent salary for each employee                        
        SELECT employee_id, MAX(month_id) AS recent_month   -- Gets the most recent month for each employee
        FROM tb_salary
        GROUP BY employee_id
    ),
    Overpaid_Employees AS (                                                         -- Creates subquery to get employees who are overpaid
        SELECT s.employee_id, s.month_id, s.salary_value, r.maximum_ref_value       -- Gets the salary and maximum reference salary for each employee
        FROM tb_salary s
        JOIN tb_employee e ON s.employee_id = e.employee_id                                           -- Joins the salary and employee tables
        JOIN tb_reference_salary r ON e.position = r.position                                         -- Joins the employee and reference salary tables
        JOIN Recent_Salaries rs ON s.employee_id = rs.employee_id AND s.month_id = rs.recent_month    -- Joins the recent salary subquery
        WHERE e.department = 'market_insights'                                     -- Filters for employees in the market_insights department in Plzen, Czech Republic
        AND e.district = 'Plzen'
        AND e.country = 'Czech Republic'
        AND r.year = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER)                     -- Filters for the reference salary year matching the salary year
        AND s.salary_value > r.maximum_ref_value
    ),
    Overpaid_Duration AS (                                      -- Creates subquery to get the number of months each employee has been overpaid
        SELECT s.employee_id, COUNT(*) AS months_above_max      -- Counts the number of months each employee has been overpaid
        FROM tb_salary s
        JOIN tb_employee e ON s.employee_id = e.employee_id     -- Joins the salary and employee tables
        JOIN tb_reference_salary r ON e.position = r.position   -- Joins the employee and reference salary tables
        WHERE e.department = 'market_insights'                  -- Filters for employees in the market_insights department in Plzen, Czech Republic
        AND e.district = 'Plzen'
        AND e.country = 'Czech Republic'
        AND r.year = CAST(SUBSTR(s.month_id, 1, 4) AS INTEGER)
        AND s.salary_value > r.maximum_ref_value
        GROUP BY s.employee_id                                  -- Groups the results by employee_id
    )
    SELECT o.employee_id, e.position, e.department, e.country, e.district,
           o.salary_value, o.maximum_ref_value, o.month_id, d.months_above_max      -- Selects the columns to display in the final result
    FROM Overpaid_Employees o                                                       -- Joins the subqueries created above
    JOIN tb_employee e ON o.employee_id = e.employee_id
    JOIN Overpaid_Duration d ON o.employee_id = d.employee_id
    ORDER BY d.months_above_max DESC, o.salary_value - o.maximum_ref_value DESC;    -- BONUS: Orders the results by the number of months overpaid and the difference between salary and maximum reference salary
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    rows = [row[:-1] for row in rows]
    return pd.DataFrame(rows, columns=["employee_id", "position", "department", "country", "district", "salary_value", "maximum_ref_value", "month_id"])

def query_b(cursor):
    query = """
    WITH annual_salary AS (                            -- Creates subquery to get the total salary for each employee in 2010
        SELECT s.employee_id, 
               SUM(s.salary_value) AS total_salary     -- Sums the salary for each employee
        FROM tb_salary s
        WHERE s.month_id BETWEEN 201001 AND 201012
        GROUP BY s.employee_id                         -- Groups the results by employee_id
    )
    SELECT e.employee_id,
           e.position, 
           e.department, 
           e.country, 
           e.district, 
           a.total_salary
    FROM tb_employee e
    JOIN annual_salary a ON e.employee_id = a.employee_id   -- Joins the annual salary subquery created above and filters for employees in the supercars department in Woking Borough, Surrey (England)
    WHERE e.department = 'supercars'
      AND e.district = 'Woking Borough'
      AND e.country = 'Surrey (England)'
    ORDER BY a.total_salary ASC;                            -- Orders the results by total salary in ascending order
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

# Performance considerations:
# Since it's a small dataset, we can run the queries as is. 
# However, if the dataset grows significantly, we might need to consider indexing the columns used in the JOIN and WHERE clauses to improve query performance.
# For example in salary table indexing the columns employee_id and month_id could help speed up the queries. 
# Indexing on department, country, and district columns in the employee table could also help improve performance.
# Also since the salary reference table is joined with the employee table, indexing the position column in the reference salary table could also speed up.

# If the data grows significantly, we might also consider partitioning the tables to improve query performance.
# For example the salary table could partitioned by month_id to make it easier to query data for specific time periods.
# The queries also use a lot of Joins, so we might consider denormalizing the data to reduce the number of joins and improve query performance.

# We could also consider using materialized views to store the results of the subqueries and improve query performance.
# If the dataset grows significantly we should consider transitioning to a more scalable database solution like PostgreSQL or MySQL and implement a star or snowflake schem solution.

if __name__ == "__main__":
    main()
