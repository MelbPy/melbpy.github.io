# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Static MelbPy website: Pelican (Markdown → HTML) plus Pagefind (static search), managed with `uv`. There are no tests or linters.

- `make build`: runs Pelican into `docs/`, then Pagefind (`uv run python -m pagefind --site docs`).
- `make serve`: builds, then serves at <http://localhost:8000> with autoreload. Autoreload only reruns Pelican, and `DELETE_OUTPUT_DIRECTORY = True` wipes `docs/` (including `docs/pagefind/`) on each rebuild, so search breaks after an autoreload until you run `make search`.
- `make publish`: same as build but with `publishconf.py`, which sets `SITEURL = "https://melbpy.github.io"` for absolute URLs.
- `make clean`: deletes `docs/`. Rarely needed, since every Pelican build already clears the output directory.

Edit `content/` and `themes/melbpy/`, never `docs/`.

## Architecture

**Content** (`content/`):

- `articles/`: posts (talks, plus site pages such as `contacts.md`, `melbourne.md`, `sponsors.md`) with `category` and `tags` metadata. Categories come only from metadata (`USE_FOLDER_AS_CATEGORY = False`).
- `pages/`: `index.md` is the home page (`save_as: index.html`); `index` is removed from `DIRECT_TEMPLATES`.
- `partials/`: ALL-CAPS Markdown files (`MENU.md`, `NEWS.md`, `SPONSORS.md`, `SMALL_PRINT.md`) rendered into every page by the `markdown_file` Jinja filter defined in `pelicanconf.py`. Pelican doesn't read them as content. The filter enables the same Markdown extensions as Pelican's reader (e.g. `{.class}` attribute lists).
- `images/`: published as-is to `/images/`.

**Categories and colour** drive the whole theme:

- `CATEGORIES` in `pelicanconf.py` is the single source: `(slug, name, colour)`. Slugs must equal Pelican's slugify of the name. It overrides the category table in `README.md`, which may be out of date.
- `base.html` turns it into an inline `<style>` of `.cat-<slug> { --base: … }` rules. Each template sets `{% block cat %}` to the page's category slug, which goes into `<body class="cat cat-<slug>">`.
- In `style.css`, `.cat` derives `--hero` from `--base` (darkened in dark mode via `light-dark()`). Links, rules, buttons and logos use `var(--hero)`, so any element with `cat cat-<slug>` classes gets that category's colour (e.g. sidebar buttons, the `.menu` block forced to Uncategorised grey).
- Inline SVG logos in `templates/svg/` are included into templates with `fill:var(--hero)` replacing their category colour; keep that when adding or editing SVGs. The header logo is chosen per category: `svg/melbourne-python-logo-<slug>-light-bg.svg`, falling back to `melbourne-python-logo.svg`. The favicon is a separate fixed-colour copy in `static/favicon.svg`.
- To add a category: add it to `CATEGORIES`, and add a `melbourne-python-logo-<slug>-light-bg.svg` with its category fills changed to `var(--hero)`.

**Layout** (`base.html` + `style.css`):

- `.layout` is a CSS grid. Areas: `tl`/`tr` header cells, a full-width coloured `rule`, `bl` main column / `br` sidebar, then `foot`.
- `.bl` and `.br` are subgrids sharing a title row and a body row, so sidebar content aligns with the start of body text. Page templates therefore split the title into `{% block heading %}` and the body into `{% block content %}`; anything extra added directly inside `.bl` would overlap the body row.
- Mobile/desktop breakpoint is `87rem`. It's hard-coded in several media queries (also used by the `.desktop-only`/`.mobile-only` utility classes). Below it, `#sidebar` becomes a slide-in drawer toggled by `static/js/menu.js`, which also focuses the search box on open.
- Category buttons with counts come from the `cat_button` macro in `_cat_button.html`, imported `with context`.

**Styling details:**

- Dark mode follows the system setting only (no toggle).
- `.light-only`/`.dark-only` classes swap images by colour scheme. Their selectors start with `:root` to win specificity over rules like `.sponsors img`.
- Fonts: Lato 300/900 and Lora 400 (italic too) from Google Fonts. The body text area (`.page-body`) is Lora; headings, bold text and links there are Lato.

**Search:**

- Uses Pagefind's Component UI (`<pagefind-searchbox>`).
- `article.html` and `page.html` put `data-pagefind-body` on `<main>`, so only articles and pages are indexed.
- Pagefind components reset styles (`all: initial`), so they're themed only via `--pf-*` variables in `style.css`, and need `color-scheme: inherit` for `light-dark()` colours to resolve.

## Content conventions (from README)

- Markdown files start with YAML front matter (`---` … `---`, via `pelican-yaml-metadata`) with lowercase keys (`title`, `category`, `author`, `date`, `tags: [a, b]`) instead of a `#` heading; use `##` for subheadings.
- Local links must be absolute with `.html`, e.g. `[About](/melbourne.html)`, so they work from category/tag subdirectories.
- Raw HTML is used for `target="_blank"` links, `<iframe>` embeds (YouTube/Google Maps; review these carefully in PRs) and `&nbsp;` spacing.
- Deployment is planned via GitHub Pages (PR to the `MelbPy.github.io` repo). `pelicanconf.py` leaves `SITEURL` empty, so local builds use root-relative URLs; `make publish` sets the real one.
