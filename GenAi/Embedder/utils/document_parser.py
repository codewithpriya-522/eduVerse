import os
from langchain.document_loaders import TextLoader, Docx2txtLoader, PyPDFLoader

from utils.pdfloader import PDFLoader


def extract_documents(config, dirpath, filename):
    """
    Loads and/ or splits text documents.

    Args:
        config (configparser.ConfigParser): Configuration parser containing settings.
        directory (str): Root directory to search for text documents.

    Returns:
        list: List of loaded and split text documents.
    """
    documents = []  # List to store loaded and split documents

    try:
        if filename.endswith(".docx"):
            loader = Docx2txtLoader(os.path.join(dirpath, filename))
            documents.extend(loader.load_and_split())
        elif filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(dirpath, filename))
            try:
                # loader = PDFLoader(config, os.path.join(dirpath, filename))
                documents.extend(loader.load())
                print(documents)
            except Exception as e:
                print("Loader error - ", e)
        else:
            loader = TextLoader(os.path.join(
                dirpath, filename), encoding="utf-8")
            documents.extend(loader.load_and_split())
    except Exception as e:
        return "error"

    return documents
