from __future__ import annotations

import nbformat

from compwa_nbhooks.colab_toc_visible import main
from compwa_nbhooks.helpers.notebook import load_notebook


def test_sets_toc_visible(write_notebook):
    notebook = nbformat.v4.new_notebook()
    path = write_notebook(notebook)

    assert main([path]) == 1
    updated = load_notebook(path)
    assert updated["metadata"]["colab"]["toc_visible"] is True


def test_idempotent(write_notebook):
    notebook = nbformat.v4.new_notebook()
    notebook["metadata"]["colab"] = {"toc_visible": True}
    path = write_notebook(notebook)

    assert main([path]) == 0
