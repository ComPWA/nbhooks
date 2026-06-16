"""Minimal read-only access to the consuming repository's :code:`pyproject.toml`.

This is a small, dependency-light substitute for the full ``Pyproject`` utility in
`ComPWA/policy <https://github.com/ComPWA/policy>`_. The notebook hooks only need to
read the package name and check whether a package is listed as a dependency.
"""

from __future__ import annotations

import re
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from compwa_nbhooks.errors import PrecommitError

_PYPROJECT_PATH = "pyproject.toml"


def _load() -> dict:
    with open(_PYPROJECT_PATH, "rb") as stream:
        return tomllib.load(stream)


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

    Both the :code:`[project] dependencies` array and the
    :code:`[dependency-groups]` are searched.
    """
    document = _load()
    dependencies = set(document.get("project", {}).get("dependencies", []))
    for group in document.get("dependency-groups", {}).values():
        dependencies |= {entry for entry in group if isinstance(entry, str)}
    packages = {package} if isinstance(package, str) else set(package)
    for dependency in dependencies:
        name_match = re.match(r"^[a-zA-Z0-9_.-]+", dependency)
        if name_match is not None and name_match.group().lower() in packages:
            return True
    return False
