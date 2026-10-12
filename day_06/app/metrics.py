def calculate_error_rate(
    errors: int,
    requests: int
) -> float:
    """Calculate the fraction of failed requests."""
    return errors / requests