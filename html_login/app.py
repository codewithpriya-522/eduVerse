from flask import Flask, request, redirect, url_for, render_template
import pyodbc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student_login_signup():
    return render_template('student_login_signup.html')

@app.route('/teacher')
def teacher_login_signup():
    return render_template('teacher_login_signup.html')

@app.route('/admin')
def admin_login_signup():
    return render_template('admin_login_signup.html')

# Database connection
def get_db_connection():
    server = r'LAPTOP-I7B5FA0R\SQLEXPRESS'  # Use raw string for backslash
    database = 'rockyproject'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    return conn

# Create table if not exists
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    # cursor.execute('''
    #     IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='student_details' and xtype='U')
    #     CREATE TABLE student_details (
    #         id INT PRIMARY KEY IDENTITY(1,1),
    #         name NVARCHAR(100),
    #         email NVARCHAR(100) UNIQUE,
    #         password NVARCHAR(100),
    #         s_class VARCHAR(20),
    #         address VARCHAR(100),  -- Increased length for longer addresses
    #         mobile BIGINT,         -- Changed to BIGINT to accommodate phone numbers correctly
    #         pin INT
    #     )
    # ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/student_signup', methods=['POST'])
def student_signup():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        s_class = request.form['s_class']
        address = request.form['address']
        mobile = request.form['mobile']
        pin = request.form['pin']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO student_details (name, email, password, s_class, address, mobile, pin) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, password, s_class, address, mobile, pin))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return "An error occurred while signing up. Please try again later."

@app.route('/student_login', methods=['POST'])
def student_login():
    try:
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM student_details WHERE email = ? AND password = ?
        ''', (email, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return "Login successful!"
        else:
            return "Invalid credentials, please try again."
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return "An error occurred during login. Please try again later."

@app.route('/teacher_signup', methods=['POST'])
def teacher_signup():
    # Add logic to handle teacher signup
    pass

@app.route('/teacher_login', methods=['POST'])
def teacher_login():
    # Add logic to handle teacher login
    pass

@app.route('/admin_signup', methods=['POST'])
def admin_signup():
    # Add logic to handle admin signup
    pass

@app.route('/admin_login', methods=['POST'])
def admin_login():
    # Add logic to handle admin login
    pass

if __name__ == '__main__':
    app.run(debug=True)
