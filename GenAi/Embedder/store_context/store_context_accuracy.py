import pyodbc


# def strore_contex(context, id):
#     server = 'LAPTOP-L8FRP4VT\SQLEXPRESS'
#     database = 'rockyproject'
#     username = 'LAPTOP-L8FRP4VT\arnab'
#     Trusted_Connection = 'yes'

#     Create a connection string
#     connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

#     Connect to the SQL Server
#     conn = pyodbc.connect(connection_string)
#     cursor = conn.cursor()
#     # stdent performs detailed store
#     for i in response:
#         cursor.execute('''insert into student_persentage (message1,percentagge)
#                        values (?, ?)''', (i['message'], i['percentage']))

#     SQL update statement
#     update_query = """
#     UPDATE qa_pairs
#     SET context = ?
#     WHERE id = ?
#     """

#     Values to be updated
#     context = context
#     id = id

#     Execute the update statement
#     cursor.execute(update_query, (context, id))

#     Commit the transaction
#     conn.commit()

#     Close the cursor and the connection
#     cursor.close()
#     conn.close()

#     print("Salary updated successfully")


# question = "What was the scene like as the sun rose?"
# questionid = 1
# context = "shrouded in a veil of mist. The sight was breathtaking, a reminder of the vastness and majesty of the natural world.As  he sun began its descent, the format took on a different character. The light softened casting a warm, golden he over everything. The shadows grew longer, and the air became "

# strore_contex(context, id)


def update_record(context, record_id):
    # Define your connection string

    # Define connection parameters
    # e.g., 'localhost' or 'your_server_name\instance'
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
    # username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Establish a connection to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Define the update query
    update_query = "UPDATE qa_pairs SET context = ? where id = ?"

    try:
        # Execute the update query
        cursor.execute(update_query, (context, record_id))

        # Commit the transaction
        conn.commit()
        print("Record updated successfully.")
    except pyodbc.Error as e:
        print(f"Error updating record: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


# Example usage
def fatch_question_context_studentans(id):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
    #username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

   # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    id_value = id  # Replace with the ID you want to fetch the question for
    query = """
    SELECT question,context
    FROM qa_pairs
    WHERE id = ?
    """

    # Execute the query with the condition value
    cursor.execute(query, (id_value,))

    # Fetch one row from the executed query
    row = cursor.fetchone()

    # Check if the row is not None and print the question
    if row:
        question = row.question  # Assuming your column name is 'question'
        context = row.context  # Assuming your column name is 'context
        #student_result = row.student_result  # Assuming your column name is 'student_ans
        # print(student_result)
    else:
        print("No data found for the given ID")

    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return question, context


def fathch_student_answer(id):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
    #username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

   # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    id_value = id  # Replace with the ID you want to fetch the question for
    query = """
    SELECT student_result
    FROM student_persentage
    WHERE id = ?
    """
    cursor.execute(query, (id_value,))
    row = cursor.fetchone()

    # Check if the row is not None and print the question
    if row:
        
        student_result = row.student_result  # Assuming your column name is 'student_ans
        # print(student_result)
    else:
        print("No data found for the given ID")

    # Close the cursor and the connection
    cursor.close()
    conn.close()
    return student_result
