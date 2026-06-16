# ComPWA notebook hooks

[![BSD 3-Clause license](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/main/packages/cspell)
[![CI](https://github.com/ComPWA/nbhooks/actions/workflows/ci.yml/badge.svg)](https://github.com/ComPWA/nbhooks/actions/workflows/ci.yml)
[![Test coverage](https://codecov.io/gh/ComPWA/nbhooks/branch/main/graph/badge.svg)](https://codecov.io/gh/ComPWA/nbhooks)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ComPWA/nbhooks/main.svg)](https://results.pre-commit.ci/latest/github/ComPWA/nbhooks/main)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)

This repository provides [pre-commit](https://pre-commit.com) hooks for formatting and standardizing [Jupyter notebooks](https://jupyter.org) in repositories of the [ComPWA organization](https://github.com/ComPWA) (see our [Help developing](https://compwa.github.io/develop) page). These hooks were extracted from [ComPWA/policy](https://github.com/ComPWA/policy); see [ComPWA/policy#612](https://github.com/ComPWA/policy/issues/612).

## Usage

Add a `.pre-commit-config.yaml` file to your repository with the following content:

```yaml
repos:
  - repo: https://github.com/ComPWA/nbhooks
    rev: ""
    hooks:
      - id: colab-toc-visible
      - id: fix-nbformat-version
      - id: remove-empty-tags
      - id: set-nb-cells
      - id: set-nb-display-name
      - id: strip-nb-whitespace
```

then run

```shell
pre-commit autoupdate --repo=https://github.com/ComPWA/nbhooks
```

This example lists [all available hooks](./.pre-commit-hooks.yaml) (listed here as `id`s) ― you can remove some of them.

| Hook ID                | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| `colab-toc-visible`    | Show the table-of-contents sidebar in Google Colab by default.       |
| `fix-nbformat-version` | Set the `nbformat` minor version to 4 and remove cell IDs.           |
| `remove-empty-tags`    | Remove the `tags` metadata field from cells when it is empty.        |
| `set-nb-cells`         | Add or replace standard cells (install cell, config cell, autolink). |
| `set-nb-display-name`  | Reset the notebook kernel display name to a standard value.          |
| `strip-nb-whitespace`  | Remove trailing whitespace from notebook cells.                      |
