# queries_defined_basic.py
from python_connection import connection  

# To Check if the connection was successful
if connection.is_connected():
    cursor = connection.cursor()

    # Define the five basic queries
    queries = [
        "SELECT * FROM Athletes WHERE YEAR(ath_dob) > 2005;",
        "SELECT ath_name, country_code FROM Athletes WHERE ath_gender = 'M' AND country_code LIKE 'U%';",
        "SELECT * FROM Events WHERE MONTH(event_date) = 7 AND YEAR(event_date) = 2024;",
        "SELECT ath_name, country_code FROM Athletes WHERE ath_name LIKE '%Alex%';",
        "SELECT medals_id, winner_id, winner_type, event_id FROM Medals WHERE medal_code = 1;"
    ]

    # Execute each query and fetch results
    for i, query in enumerate(queries, start=1):
        print(f"\nExecuting Basic Query {i}:\n{query}")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    cursor.close()
else:
    print("Connection to the database failed.")

