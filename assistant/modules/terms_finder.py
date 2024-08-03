import dspy
import typing


class TermsFinder(dspy.Module):
    """
    Extract 'cuarenta' terms from a query
    """
    def __init__(self) -> None:

        super().__init__()
        self.terms_extractor = dspy.Predict("query -> terms")

    def forward(self, query: str) -> typing.List[str]:
        """
        Gets a query and calls terms extractor to get
        the terms involved in the game
        Params:
        query:str
            The user request
        Returns
        terms:List[str]
            List of terms found
        """
        max_num_terms = max(1, len(query.split())//4)
        prompt = (
            f"Identify up to {max_num_terms} terms "
            "that can be considered jargon or in the game of ecuadorian "
            "forty card game: "
        )
        prediction = self.terms_extractor(
            query=f"{prompt}\n{query}"
        )
        answer = prediction.terms
        if "Terms: " in answer:
            start = answer.rindex("Terms: ") + len("Terms: ")
            answer = answer[start:]
        return [a.strip() for a in answer.split(',')]
