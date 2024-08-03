import dspy
import typing

from assistant.signatures.assistant import AssistantSignature
from assistant.modules.terms_finder import TermsFinder
from assistant.modules.context_extractor import ContextExtractor


class Assistant(dspy.Module):

    def __init__(
        self,
        terms_finder: typing.Type[TermsFinder],
        context_extractor: ContextExtractor
    ) -> None:
        super().__init__()
        self.terms_finder = terms_finder()
        self.definitions = context_extractor
        self.assistant = dspy.ChainOfThought(AssistantSignature, n=1)

    def forward(self, query: str) -> str:
        terms = self.terms_finder(query)
        definitions = [self.definitions(term) for term in terms]
        answer = self.assistant(
            definitions=definitions,
            query=query,
        )

        return answer.advice
