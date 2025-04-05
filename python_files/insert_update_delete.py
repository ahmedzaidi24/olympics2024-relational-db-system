# Importing connection from the python_connection file
from python_connection import connection  

try:
    # To check if the connection was successful
    if connection.is_connected():
        cursor = connection.cursor()

        # 1. INSERT Operation: Adding a new athlete
        print("\nInserting a new athlete")
        insert_query = """
        INSERT INTO Athletes (athlete_id, ath_name, ath_gender, ath_dob, country_code) 
        VALUES ('A12345', 'Syed Zaidi', 'M', '1997-12-17', 'PAK')
        """
        cursor.execute(insert_query)
        connection.commit()

        # Confirm the INSERT operation
        cursor.execute("SELECT * FROM Athletes WHERE athlete_id = 'A12345'")
        for row in cursor.fetchall():
            print(row)

        # 2. UPDATE Operation: Updating the athlete's name
        print("\nUpdating athlete's name")
        update_query = """
        UPDATE Athletes 
        SET ath_name = 'Syed Muhammad Ahmed Zaidi' 
        WHERE athlete_id = 'A12345'
        """
        cursor.execute(update_query)
        connection.commit()

        # Confirm the UPDATE operation
        cursor.execute("SELECT * FROM Athletes WHERE athlete_id = 'A12345'")
        for row in cursor.fetchall():
            print(row)

        # 3. DELETE Operation: Deleting the athlete
        print("\nDeleting the athlete")
        delete_query = """
        DELETE FROM Athletes 
        WHERE athlete_id = 'A12345'
        """
        cursor.execute(delete_query)
        connection.commit()

        # Confirm the DELETE operation
        cursor.execute("SELECT * FROM Athletes WHERE athlete_id = 'A12345'")
        if cursor.rowcount == 0:
            print("No Athlete found")
        else:
            for row in cursor.fetchall():
                print(row)

      
        cursor.close()

    else:
        print("Failed to connect to the database.")

except Exception as e:
    print(f"Error: {e}")

