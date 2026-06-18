from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from compwa_nbhooks.helpers import pyproject

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def write_pyproject(tmp_path: Path, monkeypatch):
    def _write(content: str) -> None:
        (tmp_path / "pyproject.toml").write_text(content)
        monkeypatch.chdir(tmp_path)
        pyproject._load.cache_clear()

    yield _write
    pyproject._load.cache_clear()


def test_get_package_name(write_pyproject):
    write_pyproject('[project]\nname = "my-package"\n')
    assert pyproject.get_package_name() == "my-package"


def test_has_dependency_normalizes_names(write_pyproject):
    write_pyproject(
        '[project]\nname = "x"\ndependencies = ["pyproject_local_kernel>=1.0"]\n'
    )
    assert pyproject.has_dependency("pyproject-local-kernel") is True
    assert pyproject.has_dependency("Pyproject.Local.Kernel") is True
    assert pyproject.has_dependency("other") is False


def test_has_dependency_searches_optional_and_groups(write_pyproject):
    write_pyproject(
        '[project]\nname = "x"\n'
        '[project.optional-dependencies]\ndoc = ["sphinx"]\n'
        '[dependency-groups]\ndev = ["pytest"]\n'
    )
    assert pyproject.has_dependency("sphinx") is True
    assert pyproject.has_dependency("pytest") is True
