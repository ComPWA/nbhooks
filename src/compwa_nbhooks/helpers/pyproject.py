"""Minimal read-only access to the consuming repository's :code:`pyproject.toml`.

This is a small, dependency-light substitute for the full ``Pyproject`` utility in
`ComPWA/policy <https://github.com/ComPWA/policy>`_. The notebook hooks only need to
read the package name and check whether a package is listed as a dependency.
"""

from __future__ import annotations

import re
import sys
from functools import cache

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from compwa_nbhooks.helpers.errors import PrecommitError

_PYPROJECT_PATH = "pyproject.toml"


@cache
def _load() -> dict:
    try:
        with open(_PYPROJECT_PATH, "rb") as stream:
            return tomllib.load(stream)
    except FileNotFoundError:
        return {}


def get_package_name(*, raise_on_missing: bool = False) -> str | None:
    """Get the package name from the :code:`[project]` table."""
    name = _load().get("project", {}).get("name")
    if name is None and raise_on_missing:
        msg = (
            "Please provide a name for the package under the [project] table in"
            " pyproject.toml"
        )
        raise PrecommitError(msg)
    return name


def has_dependency(package: str | tuple[str, ...]) -> bool:
    """Check whether a package is listed as a dependency in :code:`pyproject.toml`.

    The :code:`[project] dependencies` array, the
    :code:`[project.optional-dependencies]` groups, and the :code:`[dependency-groups]`
    are searched. Package names are compared after `PEP 503
    <https://peps.python.org/pep-0503/#normalized-names>`_ normalization.
    """
    document = _load()
    project = document.get("project", {})
    dependencies = set(project.get("dependencies", []))
    for group in project.get("optional-dependencies", {}).values():
        dependencies |= {entry for entry in group if isinstance(entry, str)}
    for group in document.get("dependency-groups", {}).values():
        dependencies |= {entry for entry in group if isinstance(entry, str)}
    packages = {package} if isinstance(package, str) else set(package)
    packages = {_normalize(name) for name in packages}
    for dependency in dependencies:
        name_match = re.match(r"^[a-zA-Z0-9_.-]+", dependency)
        if name_match is not None and _normalize(name_match.group()) in packages:
            return True
    return False


def _normalize(name: str) -> str:
    """Normalize a package name following `PEP 503`_.

    .. _PEP 503: https://peps.python.org/pep-0503/#normalized-names
    """
    return re.sub(r"[-_.]+", "-", name).lower()
