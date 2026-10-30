from pathlib import Path

import markdown
from pelican.settings import DEFAULT_CONFIG

SITENAME = "MelbPy"
SITEURL = ""
AUTHOR = "MelbPy"
TIMEZONE = "Australia/Melbourne"
DEFAULT_LANG = "en"

PATH = "content"
ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]
THEME = "themes/melbpy"

OUTPUT_PATH = "docs/"

DEFAULT_CATEGORY = "Uncategorised"
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = False

# index.md (a page) is the home page, so no generated article index.
DIRECT_TEMPLATES = ["categories", "tags", "archives"]
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Create a colour spectrum
L = 65.0
C = 70.0


def lch(l: float, c: float, h: float) -> str:
    return f"lch({l} {c} {h})"


CATEGORIES = [
    ("meet-up", "Meet-up", lch(L * 1.1, C * 1.1, 123.0)),
    ("data-ai", "Data & AI", lch(L * 1.05, C, 180.0)),
    ("developers", "Developers", lch(L * 1.05, C, 250.0)),
    ("humanities", "Humanities", lch(L, C, 320.0)),
    ("ops-cloud", "Ops & Cloud", lch(L, C, 23.0)),
    ("sci-eng", "Sci & Eng", lch(L, C, 50.0)),
    ("web", "Web", lch(L, C, 92.0)),
    ("uncategorised", "Uncategorised", lch(L * 1.1, C * 1.1, 123.0)),
]

PARTIALS_DIR = Path(__file__).parent / PATH / "partials"


def markdown_file(name):
    """Render a Markdown file from content/partials/ to HTML."""
    config = DEFAULT_CONFIG["MARKDOWN"]
    # Enable the configured extensions, as Pelican's own Markdown reader does.
    md = markdown.Markdown(extensions=list(config["extension_configs"]), **config)
    return md.convert((PARTIALS_DIR / name).read_text(encoding="utf-8"))


JINJA_FILTERS = {"markdown_file": markdown_file}
