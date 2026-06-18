import nbformat

from compwa_nbhooks import set_nb_cells
from compwa_nbhooks.helpers.notebook import load_notebook
from compwa_nbhooks.set_nb_cells import main


def _new_notebook() -> nbformat.NotebookNode:
    notebook = nbformat.v4.new_notebook()
    notebook["nbformat_minor"] = 4
    return notebook


def _cell(constructor, *args) -> nbformat.NotebookNode:
    cell = constructor(*args)
    cell.pop("id", None)  # following nbformat_minor = 4
    return cell


def test_config_cell_is_inserted(write_notebook):
    notebook = _new_notebook()
    notebook["cells"].append(_cell(nbformat.v4.new_code_cell, "print(1)"))
    path = write_notebook(notebook)

    assert main(["--config-cell", path]) == 1
    cells = load_notebook(path)["cells"]
    assert "STATIC_WEB_PAGE" in cells[0]["source"]
    assert cells[0]["metadata"]["tags"] == ["remove-cell"]


def test_install_cell_uses_package_name(write_notebook, monkeypatch):
    monkeypatch.setattr(set_nb_cells, "get_package_name", lambda **_: "my-package")
    set_nb_cells.__get_install_cell.cache_clear()
    notebook = _new_notebook()
    notebook["cells"].append(_cell(nbformat.v4.new_markdown_cell, "# Title"))
    path = write_notebook(notebook)

    assert main(["--add-install-cell", path]) == 1
    assert "%pip install -q my-package" in load_notebook(path)["cells"][0]["source"]


def test_skips_notebook_with_marker(write_notebook):
    notebook = _new_notebook()
    notebook["cells"].append(
        _cell(nbformat.v4.new_markdown_cell, "<!-- no-set-nb-cells -->")
    )
    path = write_notebook(notebook)

    assert main(["--config-cell", path]) == 0


def test_inserts_single_autolink_concat(write_notebook):
    notebook = _new_notebook()
    notebook["cells"].append(_cell(nbformat.v4.new_markdown_cell, "# Title"))
    path = write_notebook(notebook)

    assert main(["--autolink-concat", path]) == 1
    sources = [c["source"] for c in load_notebook(path)["cells"]]
    assert sum("autolink-concat" in s for s in sources) == 1
