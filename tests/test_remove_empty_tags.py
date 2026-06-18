import nbformat

from compwa_nbhooks.helpers.notebook import load_notebook
from compwa_nbhooks.remove_empty_tags import main


def test_removes_empty_tags(write_notebook):
    notebook = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("print(1)")
    cell["metadata"]["tags"] = []
    notebook["cells"].append(cell)
    path = write_notebook(notebook)

    assert main([path]) == 1
    assert "tags" not in load_notebook(path)["cells"][0]["metadata"]


def test_keeps_nonempty_tags(write_notebook):
    notebook = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("print(1)")
    cell["metadata"]["tags"] = ["hide-input"]
    notebook["cells"].append(cell)
    path = write_notebook(notebook)

    assert main([path]) == 0
    assert load_notebook(path)["cells"][0]["metadata"]["tags"] == ["hide-input"]
