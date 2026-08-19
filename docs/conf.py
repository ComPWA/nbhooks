from sphinx_api_relink.helpers import get_branch_name, get_package_version

BRANCH = get_branch_name()
ORGANIZATION = "ComPWA"
REPO_NAME = "nbhooks"
REPO_TITLE = "ComPWA notebook hooks"
PACKAGE_NAME = "compwa_nbhooks"

add_module_names = False
api_github_repo = f"{ORGANIZATION}/{REPO_NAME}"
api_target_substitutions: dict[str, str | tuple[str, str]] = {
    "P": "typing.ParamSpec",
    "P.args": ("attr", "typing.ParamSpec.args"),
    "P.kwargs": ("attr", "typing.ParamSpec.kwargs"),
    "T": "typing.TypeVar",
}
author = "Common Partial Wave Analysis"
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"
autosectionlabel_prefix_document = True
codeautolink_concat_default = True
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest
copyright = "2026, Common Partial Wave Analysis"
default_role = "py:obj"
extensions = [
    "myst_parser",
    "sphinx_api_relink",
    "sphinx_codeautolink",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
generate_apidoc_package_path = f"../src/{PACKAGE_NAME}"
html_favicon = "_static/favicon.ico"
html_last_updated_fmt = "%-d %B %Y"
html_logo = (
    "https://raw.githubusercontent.com/ComPWA/ComPWA/04e5199/doc/images/logo.svg"
)
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "Common Partial Wave Analysis",
            "url": "https://compwa.github.io",
            "icon": "_static/favicon.ico",
            "type": "local",
        },
        {
            "name": "GitHub",
            "url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {"text": "ComPWA notebook hooks"},
    "path_to_docs": "docs",
    "repository_branch": BRANCH,
    "repository_url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "use_download_button": False,
    "use_edit_page_button": True,
    "use_fullscreen_button": False,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
}
html_title = REPO_TITLE
intersphinx_mapping = {
    "nbformat": ("https://nbformat.readthedocs.io/en/stable", None),
    "python": ("https://docs.python.org/3", None),
}
linkcheck_ignore = [
    "https://github.com/ComPWA/nbhooks/blob/main/.pre-commit-hooks.yaml",
]
myst_enable_extensions = [
    "colon_fence",
]
nitpicky = True
primary_domain = "py"
project = PACKAGE_NAME
release = get_package_version(PACKAGE_NAME)
version = get_package_version(PACKAGE_NAME)
