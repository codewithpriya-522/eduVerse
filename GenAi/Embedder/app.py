import os
import json
import configparser
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from utils import logging
# from utils import databasefactory, embeddingfactory, parsedb
# from ai import azure_openai  # , cfgi
import DocumementProcessor
import DatabaseFactory
import EmbeddingFactory
from pdf_reader import generate_text_pdf, result_formatter
from openai_api import geminikey
from utils import constants
from store_question_answer import connection_ssms
from data_fetching import databasefactory, embeddingfactory, parsedb
from store_context import store_context_accuracy, fatch_data
import fatch_ans_vcdb
from stream_selection import percentage_retrive,strore_stream
from student_details import stdent_performance
from flask import Flask, request, redirect, url_for, render_template,jsonify
from multiprocessing import Process, Queue
from tkinter import Tk, filedialog
import pyodbc
# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, support_credentials=True)

# Configure configparser
config = configparser.ConfigParser()
config.read(os.getenv("CONFIG_FILE"))
logger = logging.getlogger(config)

# @app.route('/api/policybot', methods=['POST'])
# @cross_origin(supports_credentials=True)
# def query_policy():




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
            return render_template('student_profile.html')
        else:
            return "Invalid credentials, please try again."
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return "An error occurred during login. Please try again later."

@app.route('/teacher_signup', methods=['POST'])
def teacher_signup():
    # Add logic to handle teacher signup
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        subject = request.form['subject']
        address = request.form['address']
        mobile = request.form['mobile']
        pin = request.form['pin']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO teacher_details (name, email, password, subject, address, mobile, pin) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, password, subject, address, mobile, pin))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return "An error occurred while signing up. Please try again later."
    

@app.route('/teacher_login', methods=['POST'])
def teacher_login():
    # Add logic to handle teacher login
    try:
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM teacher_details WHERE email = ? AND password = ?
        ''', (email, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return render_template('teacher_profile.html')
        else:
            return "Invalid credentials, please try again."
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return "An error occurred during login. Please try again later."


@app.route('/admin_signup', methods=['POST'])
def admin_signup():
    # Add logic to handle admin signup
    pass

@app.route('/admin_login', methods=['POST'])
def admin_login():
    # Add logic to handle admin login
    pass

def get_user_profile(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_details WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'password': row[3],
            's_class': row[4],
            'address': row[5],
            'mobile': row[6],
            'pin': row[7]
        }
    return None
@app.route('/profile/<int:user_id>', methods=['GET'])
def profile(user_id):
    user_profile = get_user_profile(user_id)
    if user_profile:
        return jsonify(user_profile)
    else:
        return jsonify({'error': 'User not found'}), 404


def get_teacher_profile(teacher_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_details WHERE t_id = ?", (teacher_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'password': row[3],
            'subject': row[4],
            'address': row[5],
            'mobile': row[6],
            'pin': row[7]
        }
    return None
@app.route('/profileTeacher/<int:teacher_id>', methods=['GET'])
def profileTeacher(teacher_id):
    teacher_profile = get_teacher_profile(teacher_id)
    if teacher_profile:
        return jsonify(teacher_profile)
    else:
        return jsonify({'error': 'User not found'}), 404

# For embedding----------->
@app.route('/api/embedding', methods=['post'])
@cross_origin(supports_credentials=True)
def embedding_method():
    data = request.get_json()
    path = data.get('path')
    processor = DocumementProcessor.DocumentProcessor(
        config, logger, DatabaseFactory.DatabaseFactory(), EmbeddingFactory.EmbeddingFactory(config=config), path=path)
    processor.process_documents()
    return {'code': 200}

# For pdf summarization-------->
@app.route('/api/summarization', methods=['post'])
@cross_origin(supports_credentials=True)
def summarization_method():
    data = request.get_json()
    path = data.get('pdf_path')
    get_textdata = generate_text_pdf.get_summmarized_text(
        path)  # you have to provide path of the pdf file
    return {'context': get_textdata}

# Question generation ----------->
@app.route('/api/questiongeneration', methods=['post'])
@cross_origin(supports_credentials=True)
def questiongeneration_method():
    data = request.get_json()
    context = data.get('context')
    print(type(context))
    print("the context", context)
    prompt = constants.question_generator_prompt + context
    print("The prompt", prompt)
    data = geminikey.generate_ai_response(prompt)
    print("the data", data)
    print("the parts data", data.parts[0].text)
    # data = openai_langchain.generative_text_response(prompt)

    parsed_data = json.loads(data.parts[0].text)
    # parsed_data = result_formatter.question_answer_formatted(
    #     data.parts[0].text)
    print(parsed_data)
    question_id = connection_ssms.coonec_sql(parsed_data)
    return question_id


# storing data------->
@app.route('/api/storecontext', methods=['post'])
@cross_origin(supports_credentials=True)
def storecontext_method():
    # data = request.get_json()
    data = request.get_json()
    question_id = data.get('question_id')
    question_id = int(question_id)
    question = fatch_data.get_single_value(question_id)
    questionid = question_id
    # question = "What was the scene like as the sun rose?"
    # questionid=1
    embedding_function = embeddingfactory.EmbeddingFactory.create_embedding_function(
        config=config)
    db = databasefactory.ChromaFactory.get_database(
        config, logger=logger, embedding_function=embedding_function)
    context, metadata = parsedb.RetreiverClass.get_context(
        config, db, query=question)
    print(context)
    store_context_accuracy.update_record(context, questionid)
    return {'code': 200}
    # store the context to the db


# @app.route('/api/storecontext', methods=['post'])
# @cross_origin(supports_credentials=True)
# def storecontext():
#     data = request.get_json()
#     question_id = data.get('question_id')
#     fatch_ans_vcdb.storecontext_method(question_id, config, logger)
#     return 'ok'


@app.route('/api/accurecytest', methods=['post'])
@cross_origin(supports_credentials=True)
def accurecytest_method():
    data = request.get_json()
    # question = store_context_accuracy.fatch_question(id)
    # context = data.get('context')
    question_id = data.get('question_id')
    question_id = int(question_id)
    # studentanswer = data.get('student_answer')
    # stdent = "The brook, a ribbon of crystal-clear water, wove its way through the underbrush. Its surface, disturbed only by the occasional splash of a leaping fish or the fall of a leaf, mirrored the sky’s deep blue. The brook’s journey was not merely a passage through the forest but a life-giving force that sustained the myriad forms of flora and fauna along its banks. Small creatures like frogs and dragonflies flitted about, their lives intimately connected to the water’s course."
    question, context = store_context_accuracy.fatch_question_context_studentans(
        question_id)
    stdent_answer=store_context_accuracy.fathch_student_answer(question_id)
    prompt = constants.student_result_analyzer_prompt.format(stdent_answer=stdent_answer,
                                                             context=context, question=question)
    data = geminikey.generate_ai_response(prompt)

    response = json.loads(data.parts[0].text)
    print(response)
    message = (response.get("message", ""))
    percentage = (response.get("percentage", ""))
    actual_answer = (response.get("actual_answer", ""))
    stdent_performance.store_performance(question_id=question_id,message=message, percentage=percentage, actualanswer=actual_answer)
    print(response)
    return {"response": response}

@app.route('/api/streamselection', methods=['post'])
@cross_origin(supports_credentials=True)
def streamselection():
    data = request.get_json()
    s_id = data.get('s_id')
    Bengali,English,Science,Histry,Geography,MAth=percentage_retrive.marks_retrive(s_id)
    prompt=constants.student_stream_selection.format(Bengali=Bengali,English=English,Science=Science,Histry=Histry,Geography=Geography,MAth=MAth)

    data = geminikey.generate_ai_response(prompt)
    data=data.parts[0].text
    print(data)
    data=json.loads(data)
    print(data)
    if isinstance(data, dict):
        # If the variable is already a dictionary, return it as is
        data=data
    elif isinstance(data, list):
        # Convert list to a dictionary with index as key
        data={index: value for index, value in enumerate(data)}
    else:
        # For other types, return a dictionary with a single key-value pair
        data={"value": data}
    print(type(data))
    stream=(data.get("stream",""))
    print(stream)
    print(type(stream))
    strore_stream.stream_stroe(s_id,stream)
    return {"code":200}

# Uploading folder for embedding
@app.route('/folder_uploaded')
def folder_uploaded():
    return render_template('folder_uploaded.html')

def open_file_dialog(queue, subject):
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title=f"Select folder for {subject}")
    root.destroy()
    queue.put(folder_path)

# choose subject --->
@app.route('/choose_subject')
def choose_subject():
    return render_template('choose_subject.html')

# select folder --->
@app.route('/select_folder', methods=['GET'])
def select_folder():
    subject = request.args.get('subject')
    queue = Queue()
    process = Process(target=open_file_dialog, args=(queue, subject))
    process.start()
    process.join()
    folder_path = queue.get()
    
    if folder_path:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# select pdf---->

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return redirect(request.url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'File {filename} has been uploaded successfully!'

@app.route('/select_pdf')
def select_pdf():
    return render_template('select_pdf.html')

    

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
