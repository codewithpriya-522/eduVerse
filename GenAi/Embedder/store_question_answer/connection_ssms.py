import pyodbc
import json


def coonec_sql(qa_list):
    #print("The QA list:--------->", qa_list)
    
    # Ensuring qa_list is a list of dictionaries
    if isinstance(qa_list, str):
        try:
            qa_list = json.loads(qa_list)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return
    
    if not isinstance(qa_list, list) or not all(isinstance(part, dict) for part in qa_list):
        print("Data is not in the expected format of a list of dictionaries.")
        return

    # for i in range(len(qa_list)):
    #     question = qa_list[i].get("Question")
    #     answer = qa_list[i].get("Answer")
    #     print(f"Question: {question}")
    #     print(f"Answer: {answer}")
    #     print()  # Add an empty line between entries
    # Define connection parameters
    # e.g., 'localhost' or 'your_server_name\instance'
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
   
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Create a table (if not exists)
    cursor.execute('''
    IF OBJECT_ID('qa_pairs', 'U') IS NULL
    BEGIN
        CREATE TABLE qa_pairs (
            id INT IDENTITY(1,1) PRIMARY KEY,
            question NVARCHAR(MAX),
            answer NVARCHAR(MAX)
        )
    END
    ''')
    cursor.execute('CREATE TABLE #TempInserted (Id INT)')
    # Insert data into the table
    # for entry in qa_list:
    #     cursor.execute('''
    #     INSERT INTO qa_pairs (question, answer)
    #     VALUES ( ?, ?)
    #     ''', (entry['Question'], entry['Answer']))

    insert_sql = '''
        INSERT INTO qa_pairs (question, answer)
        OUTPUT INSERTED.Id INTO #TempInserted
        VALUES (?, ?)'''

    values = [(pair['Question'], pair['Answer']) for pair in qa_list]

    # Execute batch insert
    cursor.executemany(insert_sql, values)
    cursor.execute('SELECT Id FROM #TempInserted')
    identity_values = [row[0] for row in cursor.fetchall()]

    cursor.execute('DROP TABLE #TempInserted')
    # Commit the transaction
    conn.commit()
    cursor.close()
    conn.close()
    return identity_values


# store student performance
