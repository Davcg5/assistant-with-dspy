import dspy


class AssistantSignature(dspy.Signature):
    """
    Analyze a list of pieces of information about the game and provide
    help based on the request of the user
    """
    definitions = dspy.InputField(
        format=list,
        desc=(
            "The pieces of information of the game, in spanish"
        )
    )
    query = dspy.InputField(
        format=str,
        desc="The request from the user in spanish"
    )
    advice = dspy.OutputField(
        format=str,
        desc=(
            "Strategic advice or answer to the question in spanish"
        ),
    )
