from langchain.vectorstores import Chroma


class ChromaDB:

    def __init__(self, config, embedding_function):
        """
Initializes the ChromaDB class with necessary parameters.

Args:
    config (configparser.ConfigParser): Configuration parser containing settings.
    embedding_function (Callable): Function for generating document embeddings.
"""
        self.config = config
        self.embedding_function = embedding_function
        self.directory = config.get('chroma', 'directory')

    def add_to_db(self, docs):
        """
Adds text data to a Chroma database.

Args:
    docs (list): List of text data to be added to the database.

Returns:
    Chroma: Initialized and persisted Chroma database instance.
"""
        db = Chroma.from_documents(
            docs,
            self.embedding_function,
            persist_directory=self.directory
        )
        return db
