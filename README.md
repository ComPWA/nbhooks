# ComPWA notebook hooks

[![BSD 3-Clause license](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/main/packages/cspell)
[![CI](https://github.com/ComPWA/nbhooks/actions/workflows/ci.yml/badge.svg)](https://github.com/ComPWA/nbhooks/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ComPWA/nbhooks/main.svg)](https://results.pre-commit.ci/latest/github/ComPWA/nbhooks/main)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)

This repository provides [pre-commit](https://pre-commit.com) hooks for formatting and standardizing [Jupyter notebooks](https://jupyter.org) in repositories of the [ComPWA organization](https://github.com/ComPWA) (see our [Help developing](https://compwa.github.io/develop) page).

> [!NOTE]
> These notebook hooks are being extracted from [ComPWA/policy](https://github.com/ComPWA/policy); see [ComPWA/policy#612](https://github.com/ComPWA/policy/issues/612). This first release sets up only the developer configuration of the repository — the hooks themselves follow in a subsequent pull request.

## Usage

Add a `.pre-commit-config.yaml` file to your repository with the following content:

```yaml
repos:
  - repo: https://github.com/ComPWA/nbhooks
    rev: ""
    hooks:
      - id: ...
```

then run

```shell
pre-commit autoupdate --repo=https://github.com/ComPWA/nbhooks
```

This lists [all available hooks](./.pre-commit-hooks.yaml) (listed here as `id`s) ― you can remove some of them.
