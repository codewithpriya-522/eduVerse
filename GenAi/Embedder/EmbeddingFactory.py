import os
from langchain.embeddings import SentenceTransformerEmbeddings, OpenAIEmbeddings


class EmbeddingFactory:

    """
Factory class for creating document embeddings.
"""

    def __init__(self, config):
        self.config = config
        self._extract_config_params()

    def _extract_config_params(self):
        """
Extracts configuration parameters for Embedder.
"""
        self.model = self.config['model']
        self.hf = self.config['hf']
        self.openai = self.config['openai']
        self.db_params = self.config['db params']

    def create_embedding_function(self):
        """
Create and return an embedding function based on the configured embedding type.

Args:
    config (ConfigParser): Configuration parser containing settings.

Returns:
    embedding_function: The function used for generating document embeddings.

Raises:
    ValueError: If the configured embedding type is unsupported.
"""
        embedding_type = self.model.get('embedding_type')
        match embedding_type:
            case "huggingface":
                return SentenceTransformerEmbeddings(model_name=self.hf.get('model_name'))
            case "openai":
                if self.db_params.get('db_type').lower() in ["chromadb", "postgresdb"]:
                    return OpenAIEmbeddings(deployment=os.getenv("OPENAI_DEPLOYMENT_NAME"), chunk_size=1)
                else:
                    return OpenAIEmbeddings(deployment=self.openai.get('deployment_name'), model=self.openai.get('deployment_name'), chunk_size=1, openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"), openai_api_type=self.openai.get('api_type'))

            case _:
                raise ValueError(
                    f"Unsupported embedding type: {embedding_type}")
