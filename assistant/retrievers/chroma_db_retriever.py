import os

import chromadb
import chromadb.utils.embedding_functions as embedding_functions


from assistant.retrievers.retriever import Retriever

API_KEY = os.environ.get("GEMINI_API_KEY")


class ChromaDBRetriever(Retriever):

    """
    Retriever used by the definitions getter that uses chromadb
    """

    def __init__(self):
        """
        Constructs module, starts collection
        """
        self.emb_function = embedding_functions.GooglePalmEmbeddingFunction(
            api_key=API_KEY
        )
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            "rules",
            embedding_function=self.emb_function
        )

    def populate(self, file_path: str) -> None:
        """
        Populate the collection
        Params:
        file_path:str
            Path to the file
        """

        with open(file_path, 'r') as file:
            documents = file.readlines()

        embeddings = self.emb_function(documents)
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=[f"id{i}" for i in range(len(documents))]
        )

    def retrieve(self, query: str) -> str:
        """
        Get the information from the collection
        Params:
        query:str
            The query the retriever will use
        Returns:
        result:str
            The data retrieved from the collection

        """
        query_embedding = self.emb_function([query])[0]
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )
        result = results["documents"][0]
        return ".".join(result)
