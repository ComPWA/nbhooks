"""Helpers for querying files tracked by Git."""

from __future__ import annotations

import subprocess  # noqa: S404
from functools import cache


def git_ls_files(*glob: str, untracked: bool = False) -> list[str]:
    """Get the tracked and untracked files, but excluding files in .gitignore."""
    return _git_ls_files_cmd(*glob, untracked=untracked).splitlines()


@cache
def _git_ls_files_cmd(*glob: str, untracked: bool = False) -> str:
    cmd = ["git", "ls-files", *glob]
    if untracked:
        cmd.extend(["--cached", "--exclude-standard", "--others"])
    return subprocess.check_output(cmd).decode("utf-8")  # noqa: S603
