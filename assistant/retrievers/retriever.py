from abc import abstractmethod


class Retriever:
    """
    Class to be implemented by the specific retrievers
    """

    @abstractmethod
    def populate(self, **kwargs):
        """
        Read the info and populate the store
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, query: str):
        """
        Get the info from the store
        Params:
        query:str
            The query to be sent to the retriever
        """
        raise NotImplementedError
