def generate_question_id(number: int) -> str:
    """
    Generate a stable PrepFlow question ID from a numeric sequence.

    Example:
    1 -> PFQ-000000001
    """

    return f"PFQ-{number:09d}"