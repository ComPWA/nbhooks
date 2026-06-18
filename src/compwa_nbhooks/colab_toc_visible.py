"""Add notebook metadata to open the TOC sidebar on Google Colab."""

from __future__ import annotations

import argparse
import sys
from typing import TYPE_CHECKING

import nbformat

from compwa_nbhooks.helpers.errors import PrecommitError
from compwa_nbhooks.helpers.executor import Executor
from compwa_nbhooks.helpers.notebook import load_notebook

if TYPE_CHECKING:
    from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Paths to the notebooks of which the metadata should be updated.",
    )
    args = parser.parse_args(argv)
    with Executor(raise_exception=False) as do:
        for filename in args.filenames:
            do(_update_metadata, filename)
    return 1 if do.error_messages else 0


def _update_metadata(path: str) -> None:
    notebook = load_notebook(path)
    metadata = notebook["metadata"]
    updated = False
    if metadata.get("colab") is None:
        updated = True
        metadata["colab"] = {}
    if not metadata["colab"].get("toc_visible"):
        updated = True
        metadata["colab"]["toc_visible"] = True
    if not updated:
        return
    nbformat.write(notebook, path)
    msg = f"Colab TOC is now visible for notebook {path}"
    raise PrecommitError(msg)


if __name__ == "__main__":
    sys.exit(main())
