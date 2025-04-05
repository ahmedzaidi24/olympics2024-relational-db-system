# queries_defined_advance.py

from python_connection import connection 

# To check if the connection was successful
if connection.is_connected():
    cursor = connection.cursor()

    # Define the five advanced queries
    queries = [
        # Advanced Query 1
        "SELECT country_code, COUNT(athlete_id) AS total_athletes FROM Athletes GROUP BY country_code ORDER BY total_athletes DESC LIMIT 1;",
        
        # Advanced Query 2
        "SELECT v.venue_name, COUNT(e.event_id) AS total_events FROM Venues v JOIN Events e ON v.venue_id = e.venue_id GROUP BY v.venue_name ORDER BY total_events DESC;",
        
        # Advanced Query 3
        "SELECT e.event_name, COUNT(ap.athlete_id) AS athlete_count FROM Events e JOIN Athlete_Participation ap ON e.event_id = ap.event_id GROUP BY e.event_name HAVING athlete_count > 50;",
        
        # Advanced Query 4
        """
        SELECT country_code, COUNT(*) AS gold_medals 
        FROM (
            SELECT m.medals_id, a.country_code
            FROM Medals m
            JOIN Athletes a ON m.winner_id = a.athlete_id
            WHERE m.medal_code = 1 AND m.winner_type = 'Athlete'
        ) AS gold_medal_winners
        GROUP BY country_code ORDER BY gold_medals DESC;
        """,
        
        # Advanced Query 5
        """
        SELECT country_code, total_medals 
        FROM (
            SELECT a.country_code, COUNT(m.medals_id) AS total_medals
            FROM Medals m
            JOIN Athletes a ON m.winner_id = a.athlete_id
            WHERE m.winner_type = 'Athlete'
            GROUP BY a.country_code
        ) AS individual_medal_counts
        ORDER BY total_medals DESC LIMIT 5;
        """
    ]

    # Execute each query and fetch results
    for i, query in enumerate(queries, start=1):
        print(f"\nExecuting Advanced Query {i}:\n{query}")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    
    cursor.close()
else:
    print("Connection to the database failed.")

