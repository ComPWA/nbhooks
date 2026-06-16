from __future__ import annotations

import nbformat

from compwa_nbhooks import set_nb_display_name
from compwa_nbhooks.notebook import load_notebook
from compwa_nbhooks.set_nb_display_name import main


def test_sets_default_display_name(write_notebook, monkeypatch):
    # cspell:ignore kernelspec
    monkeypatch.setattr(set_nb_display_name, "has_dependency", lambda _: False)
    notebook = nbformat.v4.new_notebook()
    notebook["metadata"]["kernelspec"] = {"display_name": "wrong", "name": "python3"}
    path = write_notebook(notebook)

    assert main([path]) == 1
    kernelspec = load_notebook(path)["metadata"]["kernelspec"]
    assert kernelspec["display_name"] == "Python 3 (ipykernel)"


def test_uses_pyproject_local_kernel(write_notebook, monkeypatch):
    monkeypatch.setattr(set_nb_display_name, "has_dependency", lambda _: True)
    notebook = nbformat.v4.new_notebook()
    notebook["metadata"]["kernelspec"] = {"display_name": "wrong", "name": "python3"}
    path = write_notebook(notebook)

    assert main([path]) == 1
    kernelspec = load_notebook(path)["metadata"]["kernelspec"]
    assert kernelspec["display_name"] == "Pyproject Local"


def test_idempotent(write_notebook, monkeypatch):
    monkeypatch.setattr(set_nb_display_name, "has_dependency", lambda _: False)
    notebook = nbformat.v4.new_notebook()
    notebook["metadata"]["kernelspec"] = {
        "display_name": "Python 3 (ipykernel)",
        "name": "python3",
    }
    path = write_notebook(notebook)

    assert main([path]) == 0
