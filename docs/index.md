# ComPWA notebook hooks

:::{title} Welcome
:::

This repository provides [pre-commit](https://pre-commit.com) hooks for formatting and standardizing [Jupyter notebooks](https://jupyter.org) across [repositories of the ComPWA organization](https://github.com/orgs/ComPWA/repositories). The hooks are distributed through this repository's [`.pre-commit-hooks.yaml`](https://github.com/ComPWA/nbhooks/blob/main/.pre-commit-hooks.yaml) and are consumed by listing them in a [`.pre-commit-config.yaml`](https://pre-commit.com/index.html#adding-pre-commit-plugins-to-your-project) file.

:::{note}
The notebook hooks are being extracted from [ComPWA/policy](https://github.com/ComPWA/policy) (see [ComPWA/policy#612](https://github.com/ComPWA/policy/issues/612)). This page documents the repository once that migration lands; this first release sets up only the developer configuration.
:::

## Usage

Add a [`.pre-commit-config.yaml`](https://pre-commit.com/index.html#adding-pre-commit-plugins-to-your-project) file to your repository and list which hooks you want to use:

```yaml
repos:
  - repo: https://github.com/ComPWA/nbhooks
    rev: ""
    hooks:
      - id: ...
```

and install and activate [`pre-commit`](https://pre-commit.com/#install) as follows:

```shell
pip install pre-commit
pre-commit autoupdate --repo=https://github.com/ComPWA/nbhooks
pre-commit install
```

```{toctree}
:hidden:
API <api/compwa_nbhooks>
Changelog <https://github.com/ComPWA/nbhooks/releases>
Upcoming features <https://github.com/ComPWA/nbhooks/milestones?direction=asc&sort=title&state=open>
Help developing <https://compwa.github.io/develop>
```
