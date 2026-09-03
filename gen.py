#!/usr/bin/env python3
"""Builds the two demo templates the supplied design does not cover:
an article detail page and a content listing page, both carrying the
full site navigation. Real content is pulled from the live site."""

import html
import re
import pathlib

OUT = pathlib.Path("/var/lib/freelancer/projects/40686239/build")
SRC = pathlib.Path(
    "/tmp/claude-1007/-home-freelancer/892ef565-e94f-4a10-af80-14fbdb84a1b1"
    "/scratchpad/calm"
)

LIFE_ISSUES = [
    ("Acceptance & Letting Go", "/handling-life-issues/acceptance-and-letting-go"),
    ("Anger", "/handling-life-issues/dealing-with-anger"),
    ("Children", "/handling-life-issues/children"),
    ("Depression", "/handling-life-issues/moving-through-depression"),
    ("Fear", "/handling-life-issues/stop-fear"),
    ("Forgiveness", "/handling-life-issues/forgiveness"),
    ("Gratefulness", "/handling-life-issues/gratefulness"),
    ("Grief, Trauma & Loss", "/handling-life-issues/grief-trauma-loss"),
    ("Life Purpose", "/handling-life-issues/life-purpose"),
    ("Meditation", "/handling-life-issues/meditation"),
    ("Peace & Harmony", "/handling-life-issues/peace-and-harmony"),
    ("Procrastination & Motivation",
     "/handling-life-issues/procrastination-and-motivation"),
    ("Prosperity & Abundance", "/handling-life-issues/prosperity-and-abundance"),
    ("Relationships", "/handling-life-issues/improving-relationships"),
    ("Science of the Mind", "/handling-life-issues/science-of-the-mind"),
    ("Self-Worth & Confidence", "/handling-life-issues/self-worth-and-confidence"),
    ("Sleep", "/handling-life-issues/sleep-made-easy"),
    ("Smoking", "/handling-life-issues/quit-smoking"),
    ("Spirituality", "/handling-life-issues/spirituality"),
    ("Stress", "/handling-life-issues/stress"),
    ("Subconscious Mind", "/handling-life-issues/subconscious-mind"),
    ("Technique", "/handling-life-issues/technique"),
    ("Unconditional Love", "/handling-life-issues/unconditional-love"),
    ("Weight Loss", "/handling-life-issues/weight-loss"),
    ("Worry & Anxiety", "/handling-life-issues/worry-and-anxiety"),
]

HEALTH = [
    ("Childbirth", "/health/labour-and-childbirth"),
    ("Depression", "/health/moving-through-depression"),
    ("Health & Healing", "/health/health-and-healing"),
    ("Meditation", "/health/meditation"),
    ("Sleep", "/health/sleep-made-easy"),
    ("Smoking", "/health/quit-smoking"),
    ("Stress", "/health/stress"),
    ("Subconscious Mind", "/health/subconscious-mind"),
    ("Weight Loss", "/health/weight-loss"),
    ("Worry & Anxiety", "/health/worry-and-anxiety"),
]

SELF_IMP = [
    ("Creativity", "/self-improvement/enhancing-creativity"),
    ("Goal Setting", "/self-improvement/goal-setting"),
    ("Leadership", "/self-improvement/personal-leadership"),
    ("Life Purpose", "/self-improvement/life-purpose"),
    ("Meditation", "/self-improvement/meditation"),
    ("Memory", "/self-improvement/memory-and-learning"),
    ("Prosperity & Abundance", "/self-improvement/prosperity-and-abundance"),
    ("Sales & Productivity", "/self-improvement/sales-and-productivity"),
    ("Science of the Mind", "/self-improvement/science-of-the-mind"),
    ("Self-Worth & Confidence", "/self-improvement/self-worth-and-confidence"),
    ("Spirituality", "/self-improvement/spirituality"),
    ("Sports", "/self-improvement/sports"),
    ("Subconscious Mind", "/self-improvement/subconscious-mind"),
    ("Technique", "/self-improvement/technique"),
]

ABOUT = [
    ("About CALM", "/about/calm"),
    ("Sandy's Story", "/about/sandy-macgregor"),
    ("All the Latest", "/about/all-the-latest"),
    ("Contact", "/about/contact"),
    ("My Charity", "/charity-and-others/my-charity"),
    ("My Tours to Vietnam", "/charity-and-others/tours-to-vietnam"),
]

RESOURCES = [
    ("Getting Started", "/getting-started/"),
    ("Articles", "/articles"),
    ("FAQs", "/faq"),
    ("How-To Guides", "/how-to-guides"),
    ("Success Stories", "/success-stories"),
    ("Videos", "/videos"),
    ("Short Talks", "/short-talks"),
    ("Stress Tester", "/stress-test"),
    ("Mind Matters News", "/mmn/signup"),
    ("MMN Archive", "/mmn/archive"),
]

PRODUCTS = [
    ("Seminar Information", "/seminars"),
    ("Online Store", "https://shop.calm.com.au/"),
    ("Books", "https://shop.calm.com.au/collections/books"),
    ("Seminars on DVD", "https://shop.calm.com.au/collections/seminar"),
    ("Audio CDs", "https://shop.calm.com.au/collections/audio"),
    ("DVDs", "https://shop.calm.com.au/collections/dvd"),
    ("Packs", "https://shop.calm.com.au/collections/packs"),
    ("Coaching", "https://shop.calm.com.au/collections/personal-coaching"),
    ("Meditation", "https://shop.calm.com.au/collections/meditation"),
]


def links(items):
    return "\n".join(f'          <a href="{h}">{html.escape(t)}</a>'
                     for t, h in items)


def drawer_links(items):
    return "\n".join(f'        <a href="{h}">{html.escape(t)}</a>'
                     for t, h in items)


def header(active=""):
    def cls(name):
        return ' class="is-active"' if name == active else ""

    return f"""<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="topbar-inner">
    <a href="/" class="logo">CalmLifeSkills<span>.</span></a>

    <nav class="nav-links" aria-label="Main">
      <div class="has-mega">
        <a href="/about"{cls('about')}>About</a>
        <div class="mega cols-1">
          <div>
            <h5>About</h5>
{links(ABOUT)}
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="/topics"{cls('topics')}>Calm Topics</a>
        <div class="mega cols-3">
          <div>
            <h5>Handling Life Issues</h5>
{links(LIFE_ISSUES[:13])}
          </div>
          <div>
            <h5>&nbsp;</h5>
{links(LIFE_ISSUES[13:])}
          </div>
          <div>
            <h5>Health</h5>
{links(HEALTH)}
            <h5 style="margin-top:18px">Self Improvement</h5>
{links(SELF_IMP[:5])}
            <a href="/self-improvement">All self improvement &rarr;</a>
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="/resources"{cls('resources')}>Resources</a>
        <div class="mega cols-1">
          <div>
            <h5>Resources</h5>
{links(RESOURCES)}
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="/shop"{cls('products')}>Products</a>
        <div class="mega cols-1">
          <div>
            <h5>Products</h5>
{links(PRODUCTS)}
          </div>
        </div>
      </div>
    </nav>

    <a href="https://shop.calm.com.au/" class="nav-cta">Visit the Shop</a>

    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"
            aria-controls="site-drawer" data-drawer-open>
      <span></span><span></span><span></span>
    </button>
  </div>
</div>

<div class="drawer" id="site-drawer">
  <div class="drawer-scrim" data-drawer-close></div>
  <div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="drawer-head">
      <span class="logo">CalmLifeSkills<span>.</span></span>
      <button class="drawer-close" aria-label="Close menu" data-drawer-close>
        &times;
      </button>
    </div>

    <a class="drawer-link" href="/">Home</a>

    <details>
      <summary>About</summary>
      <div class="drawer-sub">
{drawer_links(ABOUT)}
      </div>
    </details>

    <details>
      <summary>Calm Topics</summary>
      <div class="drawer-sub">
        <h5>Handling Life Issues</h5>
{drawer_links(LIFE_ISSUES)}
        <h5>Health</h5>
{drawer_links(HEALTH)}
        <h5>Self Improvement</h5>
{drawer_links(SELF_IMP)}
      </div>
    </details>

    <details>
      <summary>Resources</summary>
      <div class="drawer-sub">
{drawer_links(RESOURCES)}
      </div>
    </details>

    <details>
      <summary>Products</summary>
      <div class="drawer-sub">
{drawer_links(PRODUCTS)}
      </div>
    </details>

    <a href="https://shop.calm.com.au/" class="nav-cta">Visit the Shop</a>
  </div>
</div>
"""


FOOTER = """
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">Calm Life Skills</div>
        <div style="max-width: 260px; font-size: 13.5px;">
          Creative Accelerated Learning Methods. Building resilience through
          the subconscious mind since 1989.
        </div>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <a href="/getting-started/">Getting Started</a>
        <a href="/articles">Articles</a>
        <a href="/faq">FAQs</a>
        <a href="/success-stories">Success Stories</a>
        <a href="/videos">Videos</a>
        <a href="/short-talks">Short Talks</a>
      </div>
      <div class="footer-col">
        <h4>Topics</h4>
        <a href="/handling-life-issues">Handling Life Issues</a>
        <a href="/health">Health</a>
        <a href="/self-improvement">Self Improvement</a>
        <a href="/how-to-guides">How-To Guides</a>
        <a href="/stress-test">Stress Tester</a>
      </div>
      <div class="footer-col">
        <h4>More</h4>
        <a href="/about/calm">About CALM</a>
        <a href="/about/sandy-macgregor">Sandy's Story</a>
        <a href="/seminars">Seminars</a>
        <a href="https://shop.calm.com.au/">Online Store</a>
        <a href="/about/contact">Contact</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 CALM Research Centre. Creative Accelerated Learning
        Methods.</span>
      <span><a href="/terms">Terms</a> &nbsp;&middot;&nbsp;
        <a href="/privacy">Privacy</a> &nbsp;&middot;&nbsp; Since 1989</span>
    </div>
  </div>
</footer>

<script>
(function () {
  var body = document.body;
  var toggle = document.querySelector('[data-drawer-open]');

  function close() {
    body.classList.remove('drawer-open');
    if (toggle) { toggle.setAttribute('aria-expanded', 'false'); toggle.focus(); }
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      body.classList.add('drawer-open');
      toggle.setAttribute('aria-expanded', 'true');
    });
  }

  document.querySelectorAll('[data-drawer-close]').forEach(function (el) {
    el.addEventListener('click', close);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && body.classList.contains('drawer-open')) close();
  });

  /* 15 years of WYSIWYG editing left <div>&nbsp;</div> spacers between
     every paragraph. They were invisible under Bootstrap's tighter
     leading; under the new type scale they open large gaps. Shown here
     client-side so the effect is visible — in the PHP build this same
     collapse happens once, server-side, when the article body renders. */
  document.querySelectorAll('.article-body > div, .article-body > p')
    .forEach(function (el) {
      if (!el.querySelector('img') &&
          el.textContent.replace(/\\u00a0|\\s/g, '') === '') {
        el.remove();
      }
    });
})();
</script>
"""


def shell(title, description, body, active=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,72,400;0,72,500;0,72,600;1,72,400;1,72,500&family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="assets/calm-theme.css" rel="stylesheet">
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


# ---------------------------------------------------------------- article page

article_body = (SRC / "body294.html").read_text()

article = f"""
<div class="article-hero">
  <div class="wrap">
    <div class="crumbs">
      <a href="/">Home</a><span>&rsaquo;</span>
      <a href="/articles">Articles</a><span>&rsaquo;</span>
      <a href="/self-improvement/enhancing-creativity">Enhancing Creativity</a>
    </div>
    <span class="tag">Self Improvement</span>
    <h1>Creativity is a Skill that can be Developed</h1>
    <div class="article-meta">
      <span>By Sandy MacGregor</span>
      <span>&middot;</span>
      <time datetime="2011-05-16">16th May 2011</time>
      <span>&middot;</span>
      <span>7 min read</span>
    </div>
  </div>
</div>

<article class="article-body">
{article_body}
</article>

<div class="article-foot">
  <div class="share-row">
    <strong style="color:var(--teal)">Found this useful?</strong>
    <a href="/articles" class="more" style="color:var(--honey-deep);font-weight:800">
      Read more articles &rarr;</a>
  </div>
</div>

<section class="related">
  <div class="wrap">
    <h2>Related reading</h2>
    <div class="card-grid">
      <a class="card" href="/article/152">
        <span class="tag">Creativity</span>
        <h3>Enhance Creativity</h3>
        <p>How the subconscious mind generates ideas when you stop forcing
          them, and the simple practice that makes it repeatable.</p>
        <span class="more">Read the article &rarr;</span>
      </a>
      <a class="card" href="/article/213">
        <span class="tag">Creativity</span>
        <h3>Enhancing Creativity</h3>
        <p>Creativity is a learned skill, not a gift you are born with.
          Sandy explains the technique behind developing it.</p>
        <span class="more">Read the article &rarr;</span>
      </a>
      <a class="card" href="/article/276">
        <span class="tag">Goal Setting</span>
        <h3>Goal Setting</h3>
        <p>Why goals written into the subconscious mind behave differently
          from goals you simply resolve to achieve.</p>
        <span class="more">Read the article &rarr;</span>
      </a>
    </div>
  </div>
</section>
"""

(OUT / "article.html").write_text(shell(
    "Creativity is a Skill that can be Developed | CALM Research Centre",
    "Creativity is such a diverse word and can have a whole spectrum of "
    "meaning. There is the sheer joy of the feeling of achievement of having "
    "created something.",
    article,
    active="topics",
))

# ---------------------------------------------------------------- listing page

ARTICLES = [
    ("Acceptance And Letting Go", "/article/203", "Acceptance",
     "Letting go is not giving up. Sandy separates the two and shows what "
     "acceptance actually asks of you."),
    ("Ruminating", "/article/333", "Acceptance",
     "The loop of turning a problem over and over, and the technique that "
     "interrupts it."),
    ("Aspects of Forgiveness", "/article/211", "Forgiveness",
     "Forgiveness is not condoning what happened. What it is, and why it "
     "matters most to the person doing it."),
    ("Never Forgive - until you're ready", "/article/191", "Forgiveness",
     "Being told to forgive before you are ready does more harm than good."),
    ("Self Forgiveness", "/article/185", "Forgiveness",
     "The hardest forgiveness of all, and the one that unlocks the rest."),
    ("Children and Peaceful Place", "/article/237", "Children",
     "How children take to the Peaceful Place technique faster than adults do."),
    ("Aspects of Anger", "/article/181", "Anger",
     "Anger as a signal rather than a failing, and what it is pointing at."),
    ("Overcoming Anger", "/article/149", "Anger",
     "Practical steps for the moment anger arrives, before it takes over."),
    ("Creativity is a Skill that can be Developed", "/article/294",
     "Creativity",
     "Creativity is a skill, like riding a bicycle, that can be learned and "
     "developed with practice."),
    ("Enhance Creativity", "/article/152", "Creativity",
     "How the subconscious mind generates ideas when you stop forcing them."),
    ("Goal setting", "/article/276", "Goal Setting",
     "Why goals written into the subconscious behave differently from goals "
     "you simply resolve to achieve."),
    ("An Attitude of Gratitude", "/article/226", "Gratefulness",
     "Gratitude as a daily practice, and the measurable difference it makes."),
]

cards = "\n".join(f"""      <a class="card" href="{h}">
        <span class="tag">{html.escape(tag)}</span>
        <h3>{html.escape(t)}</h3>
        <p>{html.escape(d)}</p>
        <span class="more">Read the article &rarr;</span>
      </a>""" for t, h, tag, d in ARTICLES)

listing = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Resources</div>
    <h1>Articles</h1>
    <p>Fifteen years of writing on the subconscious mind, from Sandy
      MacGregor and the CALM community.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="filter-bar">
      <a href="/articles" class="is-active">All</a>
      <a href="/handling-life-issues">Handling Life Issues</a>
      <a href="/health">Health</a>
      <a href="/self-improvement">Self Improvement</a>
      <a href="/faq">FAQs</a>
      <a href="/success-stories">Success Stories</a>
      <a href="/how-to-guides">How-To Guides</a>
    </div>

    <div class="card-grid">
{cards}
    </div>

    <nav class="pager" aria-label="Pagination">
      <span class="is-current">1</span>
      <a href="#">2</a>
      <a href="#">3</a>
      <a href="#">4</a>
      <span class="gap">&hellip;</span>
      <a href="#">16</a>
      <a href="#">Next &rarr;</a>
    </nav>
  </div>
</section>
"""

(OUT / "articles.html").write_text(shell(
    "Articles | CALM Research Centre",
    "Articles on the subconscious mind, meditation and life issues from "
    "Sandy MacGregor and the CALM Research Centre.",
    listing,
    active="resources",
))

print("built article.html and articles.html")
