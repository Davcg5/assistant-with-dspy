import os

from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.schema import Node

from assistant.retrievers.retriever import Retriever

API_KEY = os.environ.get("GEMINI_API_KEY")


class LlamaIndexRetriever(Retriever):

    """
    Retriever used by the definitions getter that uses llama_index
    """
    def get_nodes_from_documents(self, documents):
        nodes = []
        for doc in documents:
            lines = doc.text.split("\n")
            for i, line in enumerate(lines):
                if line.strip():
                    nodes.append(Node(text=line, doc_id=f"{doc.doc_id}_line{i}"))
        return nodes

    def __init__(self):
        """
        Starts model 
        """

        self.embed_model = GeminiEmbedding(
            model_name="models/text-embedding-004",
            embed_batch_size=16,
            api_key=API_KEY,
        )

    def populate(self, file_path):
        """
        Populate the index
        Params:
        file_path:str
            Path to the file
        """

        documents = SimpleDirectoryReader(file_path).load_data()
        nodes = self.get_nodes_from_documents(documents)
        self.index_loaded = VectorStoreIndex(
            nodes,
            embed_model=self.embed_model,
        )

    def retrieve(self, query):
        """
        Get the data
        Params:
        query:str
            The query the retriever will use
        Returns:
        result:str
            The data retrieved from the index
        """
        data_retrieved = self.index_loaded.as_retriever(
            vector_store_query_mode="mmr",
            similarity_top_k=3,
        ).retrieve(query)

        data_text = [data.text for data in data_retrieved]
        return ",".join(data_text)
