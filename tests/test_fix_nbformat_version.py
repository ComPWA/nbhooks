from __future__ import annotations

import nbformat

from compwa_nbhooks.fix_nbformat_version import main
from compwa_nbhooks.helpers.notebook import load_notebook


def test_sets_minor_version_and_strips_ids(write_notebook):
    notebook = nbformat.v4.new_notebook()
    notebook["nbformat_minor"] = 5
    cell = nbformat.v4.new_code_cell("print(1)")
    cell["id"] = "abc123"
    notebook["cells"].append(cell)
    path = write_notebook(notebook)

    assert main([path]) == 0
    updated = load_notebook(path)
    assert updated["nbformat_minor"] == 4
    assert "id" not in updated["cells"][0]


def test_rejects_binary_output(write_notebook):
    notebook = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("plot()")
    cell["outputs"] = [
        nbformat.v4.new_output("display_data", data={"image/png": "base64=="}),
    ]
    notebook["cells"].append(cell)
    path = write_notebook(notebook)

    assert main([path]) == 1
