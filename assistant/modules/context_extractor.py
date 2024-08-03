import dspy

from assistant.retrievers.retriever import Retriever

class ContextExtractor(dspy.Module):

    def __init__(self, retriever: Retriever) -> None:

        super().__init__()
        self.retriever = retriever

    def forward(self, term: str) -> str:

        definition = self.retriever.retrieve(
            query=term
        )
        return definition if definition else ""
