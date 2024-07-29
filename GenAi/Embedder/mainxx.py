import os
import re
import json
import configparser
from dotenv import load_dotenv
from pdf_reader import generate_text_pdf, result_formatter
from store_question_answer import connection_ssms
import DocumementProcessor
import DatabaseFactory
import EmbeddingFactory
from utils import logging
from openai_api import geminikey
from utils import constants
from data_fetching import databasefactory, embeddingfactory, parsedb
# Load environment variables from .env file
load_dotenv()

# if __name__ == "__main__":

#     # Embedding---------------
#     config = configparser.ConfigParser()
#     config.read(os.getenv("CONFIG_FILE"))

#     logger = logging.getlogger(config)

# processor = DocumementProcessor.DocumentProcessor(
#     config, logger, DatabaseFactory.DatabaseFactory(), EmbeddingFactory.EmbeddingFactory(config=config))
# processor.process_documents()

# Fetdata after embedding--------------------------------

# question = "What is the significance of the brook in the forest?"
# embedding_function = embeddingfactory.EmbeddingFactory.create_embedding_function(
#     config=config)
# db = databasefactory.ChromaFactory.get_database(
#     config, logger=logger, embedding_function=embedding_function)
# context, metadata = parsedb.RetreiverClass.get_context(
#     config, db, query=question)

# Checking the accuracy of the student answers---------------------
# stdent = "The brook, a ribbon of crystal-clear water, wove its way through the underbrush. Its surface, disturbed only by the occasional splash of a leaping fish or the fall of a leaf, mirrored the sky’s deep blue. The brook’s journey was not merely a passage through the forest but a life-giving force that sustained the myriad forms of flora and fauna along its banks. Small creatures like frogs and dragonflies flitted about, their lives intimately connected to the water’s course."
# prompt = constants.student_result_analyzer_prompt.format(stdent_answer=stdent,
#                                                          context=context, question=question)
# data = geminikey.generate_ai_response(prompt)

# response = json.loads(data.parts[0].text)

# print(response.get("message", ""))
# print(response.get("percentage", ""))
# print(response.get("message", ""))

# # Question Answer generation-------------------------
# # part 1 - get the pdf and generate the text out of it and summarize it
# get_textdata = generate_text_pdf.get_summmarized_text(
#     '')  # you have to provide path of the pdf file

# # # Part 3 - generate the question and answer
# prompt = constants.question_generator_prompt.format(context=get_textdata)
# data = geminikey.generate_ai_response(prompt)
# # data = openai_langchain.generative_text_response(prompt)

# parsed_data = json.loads(data.parts[0].text)
# # parsed_data = result_formatter.question_answer_formatted(
# #     data.parts[0].text)
# print(parsed_data)
# connection_ssms.coonec_sql(parsed_data)

# # Part 4 - store the question and answer in the database

# # Answer Matching - get the Student Answer and Database answer + embedding enswer compaere and generate the matching parcentage
