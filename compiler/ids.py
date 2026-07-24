def generate_question_id(pack_id: str, number: int) -> str:
    """
    Generate a globally unique PrepFlow question ID within a Pack namespace.

    Example:
    ("fundamentals", 1) -> PFQ-fundamentals-000000001
    """

    if not pack_id:
        raise ValueError("Pack ID cannot be empty when generating a question ID.")

    if number < 1:
        raise ValueError("Question ID sequence number must be positive.")

    return f"PFQ-{pack_id}-{number:09d}"
