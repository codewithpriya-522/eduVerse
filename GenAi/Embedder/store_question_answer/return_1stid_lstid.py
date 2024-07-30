import pyodbc
import json


def fetch_data_from_sql_server():
    # Define your connection string
    # Define connection parameters
    # e.g., 'localhost' or 'your_server_name\instance'
    server = 'LAPTOP-L8FRP4VT\SQLEXPRESS'
    database = 'rockyproject'
    username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    # conn = pyodbc.connect(connection_string)
    # cursor = conn.cursor()
    try:

       # JSON data
        json_data = '''
        [
            {"Question": "What is Python?", "Answer": "A programming language."},
            {"Question": "What is SQL?", "Answer": "A language for managing databases."}
        ]
        '''

        # Parse JSON data
        qa_pairs = json.loads(json_data)
        print(qa_pairs)
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Create a temporary table to store the identity values
        cursor.execute('CREATE TABLE #TempInserted (Id INT)')

        # Prepare the SQL insert statement with OUTPUT clause
        insert_sql = '''
        INSERT INTO qa_pairs (Question, Answer)
        OUTPUT INSERTED.Id INTO #TempInserted
        VALUES (?, ?)
        '''

        # Extract values for batch insert
        values = [(pair['Question'], pair['Answer']) for pair in qa_pairs]

        # Execute batch insert
        cursor.executemany(insert_sql, values)

        # Retrieve the identity values from the temporary table
        cursor.execute('SELECT Id FROM #TempInserted')
        identity_values = [row[0] for row in cursor.fetchall()]
        print(identity_values)
        # Drop the temporary table
        cursor.execute('DROP TABLE #TempInserted')
    except pyodbc.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        cursor.commit()
        cursor.close()
        conn.close()


# Example usage
# query = "SELECT * FROM qa_pairs WHERE question = "?"
params = ('some_value',)  # Example parameter

data = fetch_data_from_sql_server()
print(data)
