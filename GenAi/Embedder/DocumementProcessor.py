import os
from langchain.text_splitter import CharacterTextSplitter

from utils import constants, document_parser


class DocumentProcessor:

    def __init__(self, config, logger, db_factory, embedding_factory, path):
        """
Initializes a DocumentProcessor instance.

Args:
    config (ConfigParser): Configuration parser containing settings.
    logger: Logger for logging messages.
    db_factory: Factory for creating database instances.
    embedding_factory: Factory for creating embedding functions.
"""
        self.config = config
        self.logger = logger
        self.db_factory = db_factory
        self.embedding_factory = embedding_factory
        self.successful_files = []
        self.failed_files = []
        self._extract_config_params()
        self._pdf_path = path

    def _extract_config_params(self):
        """
Extracts configuration parameters.
"""
        self.splitter = self.config['splitter']
        self.db_params = self.config['db params']

    def process_documents(self):
        """
Process documents by splitting them into smaller chunks and adding to a database.

This function performs the following steps:
1. Retrieves the root directory for processing from the configuration.
2. Walks through the directory tree and retrieves a list of documents.
3. Splits the documents into smaller chunks using a text splitter.
4. Initializes an embedding function for generating document embeddings.
5. Adds the chunks to a database based on the configured database type.

Returns:
    db_instance: Database instance containing added chunks.

Note:
    Make sure to configure the settings in the configuration file and have
    the necessary database and embedding functionalities in place.
"""
        # root_dir = self.splitter.get('app_dir')
        root_dir = self._pdf_path
        self.logger.info(f"Root Directory - {root_dir}")

        # if not root_dir:
        #     self.logger.error("Root directory path is not set.")
        #     return
        if not os.path.exists(root_dir):
            self.logger.warning("Directory doesn't exist")
            return

        try:
            embedding_function = self.embedding_factory.create_embedding_function()
        except Exception as e:
            self.logger.error(f"Failed to initialize embedding function")
            self.logger.error(f"Error message - {str(e)}")
            return

        self.logger.info(f"Retrieving documents")
        # Walk through the directory tree
        for dirpath, dirnames, filenames in os.walk(root_dir):
            if not filenames:
                self.logger.warning("No files found for processing.")
                continue
            for filename in filenames:
                try:
                    self.logger.info(
                        f"Reading file - {filename} from {dirpath} directory")

                    documents = document_parser.extract_documents(
                        self.config, dirpath=dirpath, filename=filename)

                    if documents == "error":
                        self.logger.warning(
                            f"Failed to extract documents from {filename}")
                        continue

                    self.logger.info(
                        f"Successfully extracted documents from {filename}.")
                    self.logger.info(f"Splitting documents into chunks")

                    if not documents:
                        self.logger.warning(
                            "No documents found for processing.")
                        continue

                    documents = self.split_documents(documents)

                    self.logger.info(
                        f"Successfully split documents into chunks")

                    self.add_to_database(documents, embedding_function)
                    self.successful_files.append(filename)
                except Exception as e:
                    self.logger.error(
                        f"Failed to extract documents from {filename}")
                    self.logger.error(f"Error message - {str(e)}")
                    self.failed_files.append(filename)
                    break
        if self.successful_files:
            self.logger.info(
                f"Files added to db - {', '.join(self.successful_files)}")
        if self.failed_files:
            self.logger.info(
                f"Files failed to add to db - {', '.join(self.failed_files)}")

    def split_documents(self, documents):

        chunk_separator = self.splitter.get('chunk_separator', fallback="page")

        if chunk_separator == "page":
            self.logger.info(f"Documents are already split into pages")
        else:
            chunk_size = self.splitter.get('chunk_size', fallback=1000)
            chunk_overlap = self.splitter.get('chunk_overlap', fallback=0)
            text_splitter = CharacterTextSplitter(
                separator=constants.separator_mapping.get(chunk_separator),
                chunk_size=int(chunk_size),
                chunk_overlap=int(chunk_overlap)
            )
            documents = text_splitter.split_documents(documents)
        return documents

    def add_to_database(self, documents, embedding_function):
        try:
            self.logger.info(f"Adding chunks to db")
            self.logger.info(f"DB found - {self.db_params.get('db_type')}")

            db = self.db_factory.create_db(
                self.config, embedding_function, documents)

            self.logger.info(f"Successfully added vectors to the database")
        except Exception as e:
            self.logger.error(f"Failed to add vectors to the database")
            self.logger.error(f"Error message - {str(e)}")
