import pyodbc


def store_performance(question_id, message, percentage, actualanswer):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
    # username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    # stdent performs detailed store

    # cursor.execute('''update student_persentage (message,percentage,actual_answer)
    #                    values (?, ?,?)''', (message, percentage, actualanswer))
    update_query = "UPDATE student_persentage SET message = ?, percentage = ?, actual_answer = ? WHERE id = ?"

    # SQL update statement
    cursor.execute(update_query, (message, percentage,
                   actualanswer, question_id))

    # Values to be updated

    conn.commit()

    # Close the cursor and the connection
    cursor.close()
    conn.close()