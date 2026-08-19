"""Collect `.PrecommitError` instances from several executed functions.

.. autolink-preface::
    from compwa_nbhooks.helpers.errors import PrecommitError
    from compwa_nbhooks.helpers.executor import Executor
"""

from __future__ import annotations

import sys
from contextlib import AbstractContextManager
from typing import TYPE_CHECKING, TypeVar

from compwa_nbhooks.helpers.errors import PrecommitError

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import TracebackType

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

T = TypeVar("T")
P = ParamSpec("P")


class Executor(AbstractContextManager):
    r"""Execute functions and collect any `.PrecommitError` exceptions.

    The collected exceptions are merged and re-raised as a single `.PrecommitError`
    when the context manager exits. Set :code:`raise_exception=False` to print the
    collected messages instead of raising.

    >>> def function1() -> None:
    ...     raise PrecommitError("Error message 1")
    >>> def function2() -> None:
    ...     raise PrecommitError("Error message 2")
    >>> def function3() -> None: ...
    >>>
    >>> with Executor(raise_exception=False) as execute:
    ...     execute(function1)
    ...     execute(function2)
    ...     execute(function3)
    Error message 1
    --------------------
    Error message 2

    .. automethod:: __call__
    """

    def __init__(self, raise_exception: bool = True) -> None:
        self.__raise_exception = raise_exception
        self.__error_messages: list[str] = []
        self.__is_in_context = False

    @property
    def error_messages(self) -> tuple[str, ...]:
        """View the collected error messages."""
        return tuple(self.__error_messages)

    def __call__(
        self, function: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> T | None:
        """Execute a function and collect any `.PrecommitError` exceptions."""
        if not self.__is_in_context:
            msg = "The __call__ method can only be used within a context manager."
            raise RuntimeError(msg)
        try:
            return function(*args, **kwargs)
        except PrecommitError as exception:
            self.__error_messages.append("\n".join(exception.args))
            return None

    def __enter__(self) -> Self:
        self.__is_in_context = True
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        if exc_type is not None and not issubclass(exc_type, PrecommitError):
            return False
        if isinstance(exc_value, PrecommitError):
            self.__error_messages.append("\n".join(exc_value.args))
        error_message = self.__merge_messages()
        if error_message:
            if self.__raise_exception:
                raise PrecommitError(error_message)
            print(error_message)  # ruff: ignore[print]
        return True

    def __merge_messages(self) -> str:
        stripped_messages = (message.strip() for message in self.__error_messages)
        return "\n--------------------\n".join(stripped_messages)
