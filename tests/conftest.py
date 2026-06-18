from __future__ import annotations

from typing import TYPE_CHECKING

import nbformat
import pytest
from nbformat import NotebookNode

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


@pytest.fixture
def write_notebook(tmp_path: Path) -> Callable[[NotebookNode, str], str]:
    def _write(notebook: NotebookNode, name: str = "notebook.ipynb") -> str:
        path = tmp_path / name
        nbformat.write(notebook, str(path))
        return str(path)

    return _write
