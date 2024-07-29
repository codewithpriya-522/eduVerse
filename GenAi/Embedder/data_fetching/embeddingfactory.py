from langchain.embeddings import SentenceTransformerEmbeddings, OpenAIEmbeddings


class EmbeddingFactory:
    def create_embedding_function(config):
        """
        Create and return an embedding function based on the configured embedding type.

        Args:
            config (ConfigParser): Configuration parser containing settings.

        Returns:
            embedding_function: The function used for generating document embeddings.

        Raises:
            ValueError: If the configured embedding type is unsupported.
        """
        embedding_type = config.get('model', 'embedding_type')
        match embedding_type:
            case "huggingface":
                return SentenceTransformerEmbeddings(model_name=config.get('hf', 'model_name'))
            case "openai":
                return OpenAIEmbeddings(deployment=config.get('openai', 'embedding_model_name'), chunk_size=1)
            case _:
                raise ValueError(
                    f"Unsupported embedding type: {embedding_type}")
