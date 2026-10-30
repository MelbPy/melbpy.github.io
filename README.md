# MelbPy Static Site Generator

The MelbPy website uses Pelikan and Pagefind to create a static site with a
search bar. It uses only Markdown files for its content, and has responsive
design with device-based dark mode.

## Editing and Preview

Edit the `content` or `themes/melbpy` directories, while running:

```bash
make serve
```

Don't accidentally edit the output directory if modifying, say, `style.css`, or
your changes will be immediately overwritten.

## Deployment

```bash
make build
# Then commit, push to a branch or your own cloned repo on github, and create a
# Pull Request for the MelbPy.github.io main branch.
```

The idea is to have a Github action auto-deploy when the markdown content
changes, to host it at least initially using Github pages, and to point our
domain to that page.

## Categories

The site is designed around a set of colour-coded categories, each of which
defines a HERO colour for whichever page we are looking at. These can be seen in
the left sidebar. Links and logos will use this colour. Other page colour is
kept to a minimum.

| Category    | Name   | On Light | On Dark |
| ----------- | ------ | -------- | ------- |
| Meet-up     | Green  | #73d216  | #5f9b19 |
| Data & AI   | Aqua   | #0fc997  | #009D83 |
| Developers  | Blue   | #0db9ec  | #0092E7 |
| Humanities  | Purple | #db76f0  | #B15EC1 |
| Ops & Cloud | Red    | #fe4f60  | #D54E5A |
| Sci & Eng   | Orange | #ff5c9a  | #C36131 |
| Web         | Gold   | #b19d00  | #8E7E00 |

Note: Light-mode colours are generated in `pelicanconf.py` and the dark colours
are derived in `style.css`. These colours have been sampled from the browser
screen.

## Markup

Markdown files that work as partials and on all pages as part of the template
are named in all capitals: `MENU.md`, `NEWS.md`, `SPONSORS.md`.

- See the Pelican documentation for Markdown. You have to add title and
  category metadata to the top of each file, and so, don't use `#` to indicate
  the heading. Use '##' for the subheadings.
- When adding a link using `[]()` format, always put a `/` in front of the
  local page you are linking to and a `.html` suffix for the file. This
  prevents a link that appears on a categories or tags page from staying in a
  different directory in the URL, an ensures links work on the generated site,
  not just locally.
- There are three cases where we may want to use HTML in the Markdown.
  - If you need a link to open in a new window, you have to use HTML for the
    anchor tag, and include a `target="_blank"` property. See `index.md`,
    `SPONSORS.md`.
  - If you want to include a Google map or YouTube clip, you have to include the
    IFRAME embedding, as we do in `index.md`. (This is the security risk, so
    review all PRs carefully.)
  - If you need to tweak spacing, you might want to use an `&nbsp;` entity, as
    we do in `SMALL_PRINT.md`.

## Design

Fonts are Lato (Light and Ultra) and Lora, served from Google Fonts. These are
the Lato weights used in the logo SVGs.

See `theme/melbpy/templates/svg/` for logos.
