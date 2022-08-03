class Error(Exception):
    """Base class for other exceptions."""
    pass


class NegativeValueError(Error):
    """Raised when the negative input value is passed."""
    
    def __init__(self, value) -> None:
        self.message = f"Value can't be lower than 0, got '{value}'!"
        self.value = value

    def __str__(self) -> str:
        return self.message


class EmptyFileError(Error):
    """Raised when the opened file is empty."""

    def __init__(self, value) -> None:
        self.message = f"'{value}' file is empty."
        self.value = value

    def __str__(self) -> str:
        return self.message