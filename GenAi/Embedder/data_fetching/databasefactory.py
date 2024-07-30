import json
import openai
import os

from langchain.vectorstores import Chroma
from langchain.vectorstores.pgvector import PGVector

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
# from azure.search.documents.models import (
#     QueryAnswerType,
#     QueryCaptionType,
#     QueryLanguage,
#     QueryType,
#     RawVectorQuery,
# )


class ChromaFactory:

    def get_database(config, logger, embedding_function):
        """
Get a database instance for a specific collection.

Args:
    config (ConfigParser): Configuration parser containing database connection details.
    embedding_function: The function used for generating document embeddings.

Returns:
    Chroma: A database instance.
"""
        directory = config.get('chroma', 'directory')
        logger.debug(f"Chroma Persistent Directory - {directory}")
        return Chroma(persist_directory=directory, embedding_function=embedding_function)

    def get_page_content(db, query):
        docs = db.similarity_search(query)
        # here you can add for loop to add all the page_content of each doc in single string , then u can  return that
        return docs[0].page_content
