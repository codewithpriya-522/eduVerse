from langchain.vectorstores.pgvector import PGVector
from langchain.vectorstores.pgvector import DistanceStrategy


class PGVectorDB:
    def __init__(self, config, embedding_function):
        """
        Initializes the PGVectorDB class with necessary parameters.

        Args:
            config (dict): Configuration parameters for the database connection.
            embedding_function (callable): The function used to generate embeddings for texts.
        """
        self.config = config
        self.embedding_function = embedding_function
        self._extract_config_params()

    def _extract_config_params(self):
        """
        Extracts database connection parameters from the configuration.
        """
        # postgres_params = self.config.get('postgres', {})
        # self.host = postgres_params.get('host')
        # self.port = postgres_params.get('port')
        # self.user = postgres_params.get('username')
        # self.password = postgres_params.get('password')
        # self.dbname = postgres_params.get('db_name')
        # self.collectionname = postgres_params.get('collection_name')
        # postgres_params = self.config.get('postgres', {})
        self.host = self.config['postgres']['host']
        self.port = self.config['postgres']['port']
        self.user = self.config['postgres']['username']
        self.password = self.config['postgres']['password']
        self.dbname = self.config['postgres']['db_name']
        self.collectionname = self.config['postgres']['collection_name']

    def add_to_db(self, docs):
        """
        Creates and populates a PostgreSQL vector database using the given configuration,
        embedding function, and list of docs.

        Args:
            docs (list): List of docs to be added to the database.

        Returns:
            PGVector: A PGVector instance representing the populated database.
        """
        # connection_string = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

        db = PGVector.from_documents(
            documents=docs,
            embedding=self.embedding_function,
            distance_strategy=DistanceStrategy.COSINE,
            connection_string=connection_string,
            collection_name=self.collectionname
        )

        return db
