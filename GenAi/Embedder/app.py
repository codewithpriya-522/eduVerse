import os
import json
import configparser
from dotenv import load_dotenv
from flask import Flask, request
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


@app.route('/api/hello', methods=['get'])
@cross_origin(supports_credentials=True)
def query_policy():
    return "HELO WORLD"


@app.route('/api/bye', methods=['get'])
@cross_origin(supports_credentials=True)
def bye_query():
    return "Bye Bye"


@app.route('/api/embedding', methods=['post'])
@cross_origin(supports_credentials=True)
def embedding_method():
    data = request.get_json()
    path = data.get('path')
    processor = DocumementProcessor.DocumentProcessor(
        config, logger, DatabaseFactory.DatabaseFactory(), EmbeddingFactory.EmbeddingFactory(config=config), path=path)
    processor.process_documents()
    return {'code': 200}


@app.route('/api/summarization', methods=['post'])
@cross_origin(supports_credentials=True)
def summarization_method():
    data = request.get_json()
    path = data.get('pdf_path')
    get_textdata = generate_text_pdf.get_summmarized_text(
        path)  # you have to provide path of the pdf file
    return {'context': get_textdata}


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


# storing data
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
    print(type(data))
    stream=(data.get("stream",""))
    print(stream)
    print(type(stream))
    strore_stream.stream_stroe(s_id,stream)
    return {"code":200}



    



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
