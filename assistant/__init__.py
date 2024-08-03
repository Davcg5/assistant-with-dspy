import dspy

class BasicQA(dspy.Signature):
    """Answer questions with short factoid answers."""

    question = dspy.InputField()
    answer = dspy.OutputField(
        format=str,
        desc="often between 1 and 5 words",
        prefix="Question's Answer:"
    )
