from __future__ import annotations

import nbformat

from compwa_nbhooks.notebook import load_notebook
from compwa_nbhooks.strip_nb_whitespace import main


def test_strips_trailing_whitespace(write_notebook):
    notebook = nbformat.v4.new_notebook()
    notebook["cells"].append(nbformat.v4.new_code_cell("print(1)   \n"))
    path = write_notebook(notebook)

    assert main([path]) == 1
    assert load_notebook(path)["cells"][0]["source"] == "print(1)"


def test_leaves_clean_source(write_notebook):
    notebook = nbformat.v4.new_notebook()
    notebook["cells"].append(nbformat.v4.new_code_cell("print(1)"))
    path = write_notebook(notebook)

    assert main([path]) == 0
