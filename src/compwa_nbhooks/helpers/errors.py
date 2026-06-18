"""Custom exception types for the pre-commit hooks."""


class PrecommitError(RuntimeError):
    """Exceptions that are caught by a pre-commit hook and printed instead."""
