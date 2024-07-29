from db import postgres_db, chroma_db


class DatabaseFactory:
    def create_db(self, config, embedding_function, documents):
        """
        Create and return a database instance based on the configured database type.

        Args:
            config (ConfigParser): Configuration parser containing settings.
            embedding_function: The function used for generating document embeddings.
            documents (list): List of document chunks to be added to the database.

        Returns:
            db_instance: Database instance containing added chunks.

        Raises:
            ValueError: If the configured database type is unsupported.
        """
        db_type = config.get('db params', 'db_type')
        match db_type:
            # case "acsdb":
            #     return acs_db.ACSDB(config=config, embedding_function=embedding_function).add_to_db(docs=documents)
            # case "aossdb":
            #     return aoss_db.AOSSDB(config=config, embedding_function=embedding_function).add_to_db(docs=documents)
            case "chromadb":
                return chroma_db.ChromaDB(config=config, embedding_function=embedding_function).add_to_db(docs=documents)
            # case "postgresdb":
            #     return postgres_db.PGVectorDB(config=config, embedding_function=embedding_function).add_to_db(docs=documents)
            case _:
                raise ValueError(f"Unsupported database type: {db_type}")
