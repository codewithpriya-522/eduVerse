import pyodbc


def get_single_value(params):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'rockyproject'
    #username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "SELECT question FROM qa_pairs WHERE id = ?"
    try:

        # Execute the query
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

            # Fetch the single value
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    except pyodbc.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        cursor.close()
        conn.close()


# Example usage
# query = "SELECT question FROM qa_pairs WHERE id = ?"
