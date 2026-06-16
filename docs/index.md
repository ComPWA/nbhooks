# ComPWA notebook hooks

:::{title} Welcome
:::

This repository provides [pre-commit](https://pre-commit.com) hooks for formatting and standardizing [Jupyter notebooks](https://jupyter.org) across [repositories of the ComPWA organization](https://github.com/orgs/ComPWA/repositories). The hooks are distributed through this repository's [`.pre-commit-hooks.yaml`](https://github.com/ComPWA/nbhooks/blob/main/.pre-commit-hooks.yaml) and are consumed by listing them in a [`.pre-commit-config.yaml`](https://pre-commit.com/index.html#adding-pre-commit-plugins-to-your-project) file. These hooks were extracted from [ComPWA/policy](https://github.com/ComPWA/policy) (see [ComPWA/policy#612](https://github.com/ComPWA/policy/issues/612)).

## Usage

Add a [`.pre-commit-config.yaml`](https://pre-commit.com/index.html#adding-pre-commit-plugins-to-your-project) file to your repository and list which hooks you want to use:

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

and install and activate [`pre-commit`](https://pre-commit.com/#install) as follows:

```shell
pip install pre-commit
pre-commit autoupdate --repo=https://github.com/ComPWA/nbhooks
pre-commit install
```

This repository provides the following hooks:

- {mod}`colab-toc-visible <.colab_toc_visible>`
- {mod}`fix-nbformat-version <.fix_nbformat_version>`
- {mod}`remove-empty-tags <.remove_empty_tags>`
- {mod}`set-nb-cells <.set_nb_cells>`
- {mod}`set-nb-display-name <.set_nb_display_name>`
- {mod}`strip-nb-whitespace <.strip_nb_whitespace>`

```{toctree}
:hidden:
API <api/compwa_nbhooks>
Changelog <https://github.com/ComPWA/nbhooks/releases>
Upcoming features <https://github.com/ComPWA/nbhooks/milestones?direction=asc&sort=title&state=open>
Help developing <https://compwa.github.io/develop>
```
