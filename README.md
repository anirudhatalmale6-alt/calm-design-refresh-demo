# CALM — design refresh, template extension demo

A working demonstration for calm.com.au, built from the 4-page HTML/CSS theme
supplied by the client.

The supplied theme covers 4 pages: homepage, how-it-works, shop, six-videos.
The live site runs on roughly 12–15 templates covering 776 URLs. This repo
contains two of the templates the theme does **not** cover, built in the
theme's own visual language:

| File | What it demonstrates |
|---|---|
| `article.html` | Article detail. Real content from `calm.com.au/article/294`. |
| `articles.html` | Content listing (serves articles, FAQs, success stories). |
| `assets/calm-theme.css` | The theme's CSS extracted into one shared stylesheet, plus the added components. |

## Also fixed here

- **Mobile navigation.** The supplied design hides `.nav-links` below 820px
  and ships no replacement, so on a phone the site has no navigation at all.
  Added an accessible drawer (button, scrim, Escape-to-close, focus return).
- **The full menu is preserved.** The supplied nav has 5 items; the live site
  has ~70 destinations. The mega menu carries all of them without changing
  how the top bar looks.
- **15 years of WYSIWYG content.** Old article bodies carry inline
  `color: #0d850d` and `font-size: 15pt`, plus `<div>&nbsp;</div>` spacers.
  These are normalised so old copy cannot fight the new palette, without
  anyone re-editing 776 pages.

Built by Anirudha Talmale.
