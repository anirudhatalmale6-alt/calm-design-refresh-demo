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


# In the PHP build these stay site-absolute ("/articles"). For this static
# demo they are prefixed so every menu item opens the real page rather than
# 404ing on the preview host.
DEMO_BASE = "https://www.calm.com.au"


def u(h):
    return DEMO_BASE + h if h.startswith("/") else h


def links(items):
    return "\n".join(f'          <a href="{u(h)}">{html.escape(t)}</a>'
                     for t, h in items)


def drawer_links(items):
    return "\n".join(f'        <a href="{u(h)}">{html.escape(t)}</a>'
                     for t, h in items)


def header(active=""):
    def cls(name):
        return ' class="is-active"' if name == active else ""

    return f"""<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="topbar-inner">
    <a href="{u('/')}" class="logo">CalmLifeSkills<span>.</span></a>

    <nav class="nav-links" aria-label="Main">
      <div class="has-mega">
        <a href="{u('/about')}"{cls('about')}>About</a>
        <div class="mega cols-1">
          <div>
            <h5>About</h5>
{links(ABOUT)}
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="{u('/topics')}"{cls('topics')}>Calm Topics</a>
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
            <a href="{u('/self-improvement')}">All self improvement &rarr;</a>
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="{u('/resources')}"{cls('resources')}>Resources</a>
        <div class="mega cols-1">
          <div>
            <h5>Resources</h5>
{links(RESOURCES)}
          </div>
        </div>
      </div>

      <div class="has-mega">
        <a href="{u('/shop')}"{cls('products')}>Products</a>
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

    <a class="drawer-link" href="{u('/')}">Home</a>

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
        <a href="{u('/getting-started/')}">Getting Started</a>
        <a href="{u('/articles')}">Articles</a>
        <a href="{u('/faq')}">FAQs</a>
        <a href="{u('/success-stories')}">Success Stories</a>
        <a href="{u('/videos')}">Videos</a>
        <a href="{u('/short-talks')}">Short Talks</a>
      </div>
      <div class="footer-col">
        <h4>Topics</h4>
        <a href="{u('/handling-life-issues')}">Handling Life Issues</a>
        <a href="{u('/health')}">Health</a>
        <a href="{u('/self-improvement')}">Self Improvement</a>
        <a href="{u('/how-to-guides')}">How-To Guides</a>
        <a href="{u('/stress-test')}">Stress Tester</a>
      </div>
      <div class="footer-col">
        <h4>More</h4>
        <a href="{u('/about/calm')}">About CALM</a>
        <a href="{u('/about/sandy-macgregor')}">Sandy's Story</a>
        <a href="{u('/seminars')}">Seminars</a>
        <a href="https://shop.calm.com.au/">Online Store</a>
        <a href="{u('/about/contact')}">Contact</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Calm Life Skills. Creative Accelerated Learning
        Methods.</span>
      <span><a href="{u('/terms')}">Terms</a> &nbsp;&middot;&nbsp;
        <a href="{u('/privacy')}">Privacy</a> &nbsp;&middot;&nbsp; Since 1989</span>
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


def shell(title, description, body, active="", extra_css=""):
    extra = (f'\n<link href="assets/{extra_css}" rel="stylesheet">'
             if extra_css else "")
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
<link href="assets/calm-theme.css" rel="stylesheet">{extra}
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
      <a href="{u('/')}">Home</a><span>&rsaquo;</span>
      <a href="{u('/articles')}">Articles</a><span>&rsaquo;</span>
      <a href="{u('/self-improvement/enhancing-creativity')}">Enhancing Creativity</a>
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
    <a href="{u('/articles')}" class="more" style="color:var(--honey-deep);font-weight:800">
      Read more articles &rarr;</a>
  </div>
</div>

<section class="related">
  <div class="wrap">
    <h2>Related reading</h2>
    <div class="card-grid">
      <a class="card" href="{u('/article/152')}">
        <span class="tag">Creativity</span>
        <h3>Enhance Creativity</h3>
        <p>How the subconscious mind generates ideas when you stop forcing
          them, and the simple practice that makes it repeatable.</p>
        <span class="more">Read the article &rarr;</span>
      </a>
      <a class="card" href="{u('/article/213')}">
        <span class="tag">Creativity</span>
        <h3>Enhancing Creativity</h3>
        <p>Creativity is a learned skill, not a gift you are born with.
          Sandy explains the technique behind developing it.</p>
        <span class="more">Read the article &rarr;</span>
      </a>
      <a class="card" href="{u('/article/276')}">
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
    "Creativity is a Skill that can be Developed | Calm Life Skills",
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

cards = "\n".join(f"""      <a class="card" href="{u(h)}">
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
      <a href="{u('/articles')}" class="is-active">All</a>
      <a href="{u('/handling-life-issues')}">Handling Life Issues</a>
      <a href="{u('/health')}">Health</a>
      <a href="{u('/self-improvement')}">Self Improvement</a>
      <a href="{u('/faq')}">FAQs</a>
      <a href="{u('/success-stories')}">Success Stories</a>
      <a href="{u('/how-to-guides')}">How-To Guides</a>
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
    "Articles | Calm Life Skills",
    "Articles on the subconscious mind, meditation and life issues from "
    "Sandy MacGregor and Calm Life Skills.",
    listing,
    active="resources",
))

print("built article.html and articles.html")

# ---------------------------------------------------------------- demo index

index = """
<div class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Demo &mdash; for Sandy</div>
    <h1>The new home page, <em>plus the templates</em> the design does not
      cover</h1>
    <p>Built in the design's own visual language, using real content and real
      destinations from calm.com.au. Try them on a phone as well &mdash; the
      navigation works there.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="card-grid">
      <a class="card" href="approach.html">
        <span class="tag">Read first</span>
        <h3>How I would run this</h3>
        <p>The approach, in six stages, with what each one risks &mdash;
          written in place of the call. Covers how payment works, how to
          revert, what is not included, and why the domain move must be its
          own step.</p>
        <span class="more">Open the page &rarr;</span>
      </a>
      <a class="card" href="home.html">
        <span class="tag">Your design</span>
        <h3>Home page</h3>
        <p>The supplied home page design, with every placeholder anchor
          replaced by its real destination and each of the 19 meditation
          chips linked to its own product in the shop. Prices are not
          reprinted here &mdash; see the note below.</p>
        <span class="more">Open the page &rarr;</span>
      </a>
      <a class="card" href="article.html">
        <span class="tag">Template</span>
        <h3>Article detail page</h3>
        <p>Real content from calm.com.au/article/294. Covers 152 article
          URLs, and the same template serves the 118 FAQs and 344 success
          stories. Shows how 15 years of pasted WYSIWYG copy is normalised
          into the new type scale.</p>
        <span class="more">Open the page &rarr;</span>
      </a>
      <a class="card" href="articles.html">
        <span class="tag">Template</span>
        <h3>Content listing page</h3>
        <p>Card grid, topic filters and pagination. One template serves
          Articles, FAQs, Success Stories and How-To Guides &mdash; together
          about 614 of the site's 776 URLs.</p>
        <span class="more">Open the page &rarr;</span>
      </a>
    </div>

    <div class="lead" style="margin-top:64px">
      <p><strong>Open the menu on a phone.</strong> The supplied design hides
        the navigation below 820px and ships nothing in its place, so on a
        phone the site would have no menu at all. The drawer here is the fix.</p>
      <p><strong>Hover &ldquo;Calm Topics&rdquo; on a desktop.</strong> Your
        supplied nav has 5 links; the live site has about 70 destinations.
        All of them are still reachable, without changing how the bar looks.</p>
      <p><strong>About the prices.</strong> The supplied home page prints
        &ldquo;$14.95 USD&rdquo; for PP#2. Your shop sells it for $20.00 AUD.
        A price typed into a page drifts the moment you change it in Shopify,
        so the buttons here link to the product instead of restating a
        number. Worth deciding which figure is the correct one.</p>
      <p><strong>Three chip names do not match the shop.</strong> The design
        lists PP#3 as &ldquo;Releasing Physical Pain&rdquo;, PP#5 as
        &ldquo;Deeper Meditation&rdquo; and PP#20 as &ldquo;Preparation for a
        Peaceful Birth&rdquo;. The shop sells those as Releasing Hurt,
        Meditation, and Handling The Labour Of Childbirth. I used the shop's
        names so nobody clicks through to a different title than they
        expected.</p>
    </div>
  </div>
</section>
"""

(OUT / "index.html").write_text(shell(
    "Calm Life Skills design refresh \u2014 demo",
    "Home page plus article and listing templates built in the supplied "
    "Calm Life Skills theme.",
    index,
))

print("built index.html")


# ---------------------------------------------------------------- home page
# The supplied homepage design, with every placeholder anchor ("#program",
# "#shop", "#about") replaced by the real destination on the live site, and
# every meditation chip turned into a link to its own product.

SHOP = "https://shop.calm.com.au"


def prod(handle):
    return f"{SHOP}/products/{handle}"


# Titles here are the SHOP's titles, not the design's. Three chips in the
# supplied file name a different track to the one actually sold:
#   PP#3  design "Releasing Physical Pain"      shop "Releasing Hurt"
#   PP#5  design "Deeper Meditation"            shop "Meditation"
#   PP#20 design "Preparation for a Peaceful Birth"
#                                               shop "Handling The Labour Of
#                                                     Childbirth"
# Flagged to the client; the shop is treated as the source of truth so a
# visitor never clicks a name that does not exist when they get there.
PEACEFUL_PLACE = [
    (2, "Guided Imagery", "peaceful-place-series-cd-no-2-guided-imagery-download"),
    (3, "Releasing Hurt", "peaceful-place-series-no-3-releasing-hurt-download"),
    (4, "Healing Yourself", "peaceful-place-series-no-4-healing-yourself-download"),
    (5, "Meditation", "peaceful-place-series-no-5-meditation-download"),
    (6, "Forgiveness", "peaceful-place-series-no-6-forgiveness-download"),
    (7, "Tapping Your Creativity",
     "peaceful-place-series-no-7-tapping-your-creativity-download"),
    (8, "Weight Release", "peaceful-place-series-no-8-weight-release-download"),
    (9, "Letting Go Anger", "peaceful-place-series-no-9-letting-go-anger-download"),
    (10, "Self Worth and Confidence",
     "peaceful-place-series-no-10-self-worth-and-confidence-download"),
    (11, "Achieving In Exams and Effective Study",
     "peaceful-place-series-no-11-achieving-in-exams-and-effective-study-download"),
    (12, "Making Sleep Easy and Useful",
     "peaceful-place-series-no-12-making-sleep-easy-and-useful-download"),
    (13, "Inner Peace and Harmony",
     "peaceful-place-series-no-13-inner-peace-and-harmony-download"),
    (14, "Improving Relationships",
     "peaceful-place-series-no-14-improving-relationships-download"),
    (15, "Overcoming Fear", "peaceful-place-series-no-15-overcoming-fear-download"),
    (16, "Acceptance and Letting Go",
     "peaceful-place-series-no-16-acceptance-and-letting-go-download"),
    (17, "Unconditional Love",
     "peaceful-place-series-no-17-unconditional-love-download"),
    (18, "Overcoming Worry &amp; Anxiousness",
     "peaceful-place-series-no-18-overcoming-worry-anxiousness-download"),
    (19, "Moving Through Depression",
     "peaceful-place-series-no-19-moving-through-depression-download"),
    (20, "Handling The Labour Of Childbirth",
     "peaceful-place-series-no-20-handling-the-labour-of-childbirth-download"),
    (21, "Quit Smoking", "peaceful-place-series-no-21-quit-smoking-download"),
]

PP2 = prod(PEACEFUL_PLACE[0][2])

med_chips = "\n".join(
    f'      <a class="med-chip" href="{prod(h)}">{t} PP#{n}</a>'
    for n, t, h in PEACEFUL_PLACE[1:]
)

FOUNDATION = [
    ("Video 01", "There&rsquo;s a part of your mind you were never taught to use.",
     "The subconscious runs the majority of what you do. Most people never get "
     "shown how to speak to it deliberately."),
    ("Video 02",
     "It&rsquo;s already being used successfully by athletes, doctors and students.",
     "The same mental training turns up wherever performance under pressure "
     "matters. It is not fringe, it is just not taught."),
    ("Video 03", "You can do this yourself, right now.",
     "The entry technique takes thirty seconds and needs no equipment, no "
     "teacher and no belief system."),
    ("Video 04", "There&rsquo;s measurable science behind it.",
     "Brainwave states are measurable. So are blood pressure and pulse. The "
     "demonstrations show the change as it happens."),
    ("Video 05",
     "This works for life&rsquo;s hardest moments, not just minor ones.",
     "Grief, trauma, chronic pain. The technique was built under real pressure, "
     "not in a seminar room."),
    ("Video 06", "Now you understand enough. Take the next step.",
     "Once the idea makes sense, the practice is what changes things. That "
     "starts with PP#2."),
]

foundation_cards = "\n".join(f"""      <div class="foundation-card">
        <div class="foundation-label">{lbl}</div>
        <h3>{h}</h3>
        <p>{p}</p>
      </div>""" for lbl, h, p in FOUNDATION)

STORIES = [
    ("I finally sleep through the night. It took two weeks of the sleep "
     "meditation, not months.", "M.T., Ohio"),
    ("I used the fear meditation before my surgery. I went in steadier than I "
     "thought possible.", "R.K., Queensland"),
    ("Quitting smoking finally stuck once I understood why I reached for it in "
     "the first place.", "D.P., Surrey"),
    ("My exam anxiety used to wreck my grades. The study performance track "
     "changed that completely.", "A.S., California"),
]

story_cards = "\n".join(f"""      <div class="story-card">
        <p class="story-quote">&ldquo;{q}&rdquo;</p>
        <p class="story-name">{n}</p>
      </div>""" for q, n in STORIES)

home = f"""
<section class="hero">
  <div class="hero-inner">
    <div>
      <div class="eyebrow">Creative Accelerated Learning Methods, Since 1989</div>
      <h1>Resilience isn&rsquo;t willpower. <em>It&rsquo;s trained</em>, in the
        quiet of your own mind.</h1>
      <p class="hero-sub">Calm Life Skills teaches you to work with your
        subconscious mind, through guided imagery and targeted meditation, so
        calm becomes a skill you carry, not a moment you wait for.</p>
      <div class="hero-actions">
        <a href="#start" class="btn-primary">Learn to Relax in 30 Seconds</a>
        <a href="{u('/about/sandy-macgregor')}" class="btn-secondary">Meet Sandy</a>
      </div>
      <div class="hero-trust">
        <div><strong>1989</strong>Program founded</div>
        <div><strong>19</strong>Targeted meditations</div>
        <div><strong>6</strong>Foundational short videos</div>
        <div><strong>3</strong>Continents taught on</div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="brainwave-flow">
        <svg viewBox="0 0 760 200" preserveAspectRatio="xMidYMid meet"
             xmlns="http://www.w3.org/2000/svg" role="img"
             aria-label="A brainwave tracing slowing from Beta through Alpha and
                         Theta into Delta">
          <path class="flow-line" d="M0,100
            Q6,0 12,100 Q18,200 24,100 Q30,2 36,100 Q42,198 48,100 Q54,0 60,100 Q66,200 72,100 Q78,2 84,100 Q90,198 96,100 Q102,0 108,100 Q114,200 120,100 Q126,4 132,100 Q138,196 144,100 Q150,0 156,100 Q162,200 168,100 Q174,4 180,100
            C189,44 196,44 205,100 C214,156 221,156 230,100 C239,40 246,40 255,100 C264,158 271,158 280,100 C289,46 296,46 305,100 C314,154 321,154 330,100 C339,43 346,43 355,100 C364,157 371,157 380,100
            C393,56 403,56 416,100 C429,144 439,144 452,100 C465,54 475,54 488,100 C501,146 511,146 524,100 C537,56 547,56 560,100
            C578,85 592,85 610,100 C628,115 642,115 660,100 C678,86 692,86 710,100 C728,114 742,114 760,100"/>
        </svg>
        <div class="flow-labels">
          <div class="flow-label">
            <div class="wave-name">Beta</div>
            <div class="wave-state">Alert</div>
          </div>
          <div class="flow-label">
            <div class="wave-name">Alpha</div>
            <div class="wave-state">Relaxed</div>
          </div>
          <div class="flow-label">
            <div class="wave-name">Theta</div>
            <div class="wave-state">Meditative</div>
          </div>
          <div class="flow-label">
            <div class="wave-name">Delta</div>
            <div class="wave-state">Deep sleep</div>
          </div>
        </div>
        <div class="brainwave-caption">Calm Life Skills teaches you to create the
          habits you want by using the Theta state of your subconscious mind</div>
      </div>
    </div>
  </div>
  <div class="wave-divider">
    <svg viewBox="0 0 1600 80" preserveAspectRatio="none" aria-hidden="true"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M0,40 C100,10 200,70 300,40 C400,10 500,70 600,40 C700,10 800,70 900,40 C1000,10 1100,70 1200,40 C1300,10 1400,70 1500,40 C1550,25 1580,40 1600,40 L1600,80 L0,80 Z
                M1600,40 C1700,10 1800,70 1900,40 C2000,10 2100,70 2200,40 C2300,10 2400,70 2500,40 C2600,10 2700,70 2800,40 C2900,10 3000,70 3100,40 C3150,25 3180,40 3200,40 L3200,80 L1600,80 Z"
            fill="#A8D5C5" opacity="0.55"/>
    </svg>
  </div>
</section>

<section class="tracks" id="start">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Two ways to begin</div>
      <h2>Wherever you&rsquo;re starting from, there&rsquo;s a path to success</h2>
      <p>Everyone starts in the same place. PP#2, Guided Imagery, teaches your
        mind to relax and release stress in 30 seconds. Only once that skill is
        in place do the targeted meditations work as they should.</p>
    </div>
    <div class="track-grid">
      <div class="track-card quick">
        <span class="track-tag">I want help now</span>
        <h3>Start with Guided Imagery</h3>
        <p>A guided imagery track that teaches your mind to relax and release
          stress in 30 seconds, no experience required. This is step one, before
          any targeted meditation.</p>
        <a href="{PP2}" class="track-link">Start with PP#2 Guided Imagery &rarr;</a>
      </div>
      <div class="track-card learn">
        <span class="track-tag">I want to understand first</span>
        <h3>See how Calm Life Skills works</h3>
        <p>Do the 6 foundational short videos, read about the man who built it
          under fire, and why the subconscious mind responds to this kind of
          training.</p>
        <a href="{u('/getting-started/')}" class="track-link">Start here &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="foundation" id="videos">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Learn why this works</div>
      <h2>The six foundation short videos.</h2>
      <p>Six short videos, in order. By the end you will understand what the
        subconscious mind does, why it responds to imagery, and what to do next.</p>
    </div>
    <div class="foundation-grid">
{foundation_cards}
    </div>
    <a href="{u('/videos')}" class="foundation-cta">Watch the six videos</a>
  </div>
</section>

<section class="program" id="program">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">The Program</div>
      <h2>Two steps, moving into Alpha and then into Theta</h2>
      <p>Guided Imagery first, to teach the entry. Then whichever targeted
        meditation matches what you are working on.</p>
    </div>
    <div class="program-grid">
      <div class="program-card">
        <div class="program-step">PP#2</div>
        <h3>Guided Imagery</h3>
        <p>The foundation track. Teaches your mind to reach a relaxed state in
          about thirty seconds, which is the skill everything else rests on.</p>
        <a href="{PP2}" class="track-link">See it in the shop &rarr;</a>
      </div>
      <div class="program-card">
        <div class="program-step">PP#3 to PP#21</div>
        <h3>The 19 Meditations</h3>
        <p>One track per issue, from sleep and pain to confidence, grief and
          quitting smoking. Take the one you need, when you need it.</p>
        <a href="{SHOP}/collections/meditation" class="track-link">Browse all
          meditations &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="meditations" id="meditations">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">19 Targeted Meditations</div>
      <h2>Whatever you want to achieve, there&rsquo;s a track for it</h2>
      <p>Every one of these opens its own page in the shop.</p>
    </div>
    <div class="med-grid">
{med_chips}
    </div>
  </div>
</section>

<section class="about" id="about">
  <div class="wrap about-grid">
    <div>
      <a class="video-frame" href="{u('/videos')}"
         aria-label="Watch: Who Is Sandy MacGregor?">
        <div class="play-btn">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div class="video-caption">Who Is Sandy MacGregor?</div>
      </a>
      <div class="archive-tag">Videos covering seminar snippets, a four part
        series of Resilience Lectures, the Brainwave Proof demonstrations, Sandy's
        Vietnam experiences and more.
        <a href="{u('/videos')}">Watch More &rarr;</a></div>
    </div>
    <div class="about-copy">
      <div class="eyebrow">About Sandy</div>
      <h2>Trained under fire. Now teaching calm.</h2>
      <p>Sandy MacGregor served in Vietnam, was decorated for it, and later lost
        three daughters to a single act of violence. What he built afterwards was
        not a theory about resilience. It was the thing that got him through.</p>
      <p>Since 1989 he has taught these techniques on three continents, to
        boardrooms, classrooms and people in the worst week of their lives.</p>
      <div class="credentials">
        <span class="credential-pill">Royal Military College Duntroon</span>
        <span class="credential-pill">Military Cross</span>
        <span class="credential-pill">US Bronze Star</span>
        <span class="credential-pill">Chartered Civil Engineer</span>
      </div>
      <a href="{u('/about/sandy-macgregor')}" class="btn-secondary">Read Sandy's
        story</a>
    </div>
  </div>
</section>

<section class="stories" id="stories">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Real Results</div>
      <h2>Four of hundreds of stories like these</h2>
    </div>
    <div class="stories-grid">
{story_cards}
    </div>
    <p class="stories-disclaimer">Individual results vary. These accounts reflect
      personal experiences and are not guarantees of outcome.
      <a href="{u('/success-stories')}">Read more success stories &rarr;</a></p>
  </div>
</section>

<section class="final-cta">
  <div class="wrap">
    <h2>Why Calm Life Skills Exists?</h2>
    <p>To help you understand and deliberately use the other 88% of your mind,
      being the subconscious mind. Using this power means you can deal more
      effectively with challenges and create positive change in your life.</p>
    <p class="mission">Our Mission is to teach about the subconscious mind and
      encourage people to use it to their own advantage.</p>
    <a href="{PP2}" class="btn-primary">Begin with PP#2 Guided Imagery</a>
  </div>
</section>
"""

(OUT / "home.html").write_text(shell(
    "Calm Life Skills \u2014 resilience trained, not willed",
    "Calm Life Skills teaches you to work with your subconscious mind through "
    "guided imagery and targeted meditation. Founded by Sandy MacGregor, 1989.",
    home,
    active="home",
    extra_css="calm-home.css",
), encoding="utf-8")

print("built home.html")


# ------------------------------------------------------------- approach page
# Written in place of the initial call the client asked for. Same content a
# call would have covered, but she can re-read it and forward it.

STAGES = [
    ("now", "Templates, before anything is touched",
     "There is no design yet for most of the site. Rather than discover that "
     "halfway through integration, I build each missing template first, in "
     "your theme's own visual language, and you approve it on a link like the "
     "ones you already have.",
     ["Home page &mdash; <a href=\"home.html\">built</a>",
      "Article detail &mdash; <a href=\"article.html\">built</a>, covers "
      "articles, FAQs and success stories",
      "Content listing &mdash; <a href=\"articles.html\">built</a>, one "
      "template for about 614 of the 776 URLs",
      "Topic section pages (Handling Life Issues, Health, Self Improvement)",
      "Seminars, Contact, Videos, Short Talks, Stress Tester, Getting Started",
      "Terms and Privacy"],
     "<strong>Why first:</strong> a template approved on a static page costs "
     "minutes to change. The same change after it is woven into PHP costs "
     "hours, on a site that is live while you look at it."),

    ("later", "Access and a staging copy",
     "Your son gives me FTP or SSH and a database user, plus a staging "
     "subdomain &mdash; something like staging.calm.com.au that is closed to "
     "search engines. Nothing I do touches the live site until you have "
     "clicked it on staging and said yes.",
     ["Read-only look at the codebase first, so I can see how the templates "
      "are actually assembled",
      "A copy of the site running on the staging subdomain",
      "A full backup of files and database taken before I change anything"],
     "<strong>Risk if skipped:</strong> editing a live site with 776 indexed "
     "pages means every mistake is public and is being crawled while it is "
     "wrong."),

    ("later", "Integration",
     "The real work. The new stylesheet goes in, Bootstrap 3 comes out, and "
     "every PHP template is rewired to the new markup. Content, links and the "
     "back end are untouched &mdash; only the visual layer changes.",
     ["Remove Bootstrap 3.0.3, jQuery UI and the shims for Internet "
      "Explorer 8 that the site still loads",
      "Replace the five per-page stylesheets with the one shared theme",
      "Remove the iContact newsletter signup, as you asked",
      "Keep every existing URL exactly as it is"],
     "<strong>The thing to watch:</strong> your menu has about 70 "
     "destinations and the supplied design has 5. Every one of the 70 stays "
     "reachable, or roughly 600 pages quietly drop out of Google."),

    ("later", "Cross-browser and device QA",
     "Chrome, Firefox, Safari and Edge, at phone, tablet and desktop widths, "
     "with screenshots at each breakpoint so you can see it rather than take "
     "my word for it.",
     ["Screenshots of every template at each breakpoint",
      "Every internal link checked, not sampled",
      "The pages that only exist on demand checked too, not just the home page"],
     "<strong>Note:</strong> a home page that looks right proves almost "
     "nothing. The pages that break are the ones nobody thinks to open."),

    ("later", "Go live on calm.com.au",
     "The design goes live on the domain you already have, with the old "
     "theme kept intact so a revert is one step, not a rebuild. Then we leave "
     "it alone for a week or two and watch that nothing moved.",
     ["A hand-over note listing every file touched",
      "Exact revert instructions",
      "The old theme kept in place, not deleted"],
     "<strong>Why not do the rename here:</strong> see the next stage."),

    ("later", "The move to calmlifeskills.com &mdash; separately",
     "This is the part that can actually cost you traffic, and it has nothing "
     "to do with how the site looks. Some of your pages have been indexed "
     "since 2014. If they move address without a redirect, that history does "
     "not move with them.",
     ["A permanent redirect for each of the 776 addresses to its new one",
      "calm.com.au stays registered and pointing at the new site "
      "indefinitely &mdash; not a year, permanently",
      "Canonical tags, sitemap and Search Console change-of-address updated",
      "The /article/23 to /faq/23 quirk carried across, or Google sees two "
      "copies of everything"],
     "<strong>Do not combine this with the redesign.</strong> If both land "
     "at once and traffic dips, there is no way to tell which one did it and "
     "no clean way to undo either."),
]

stage_html = "\n".join(f"""    <div class="stage">
      <div class="stage-no">{i:02d}</div>
      <div>
        <span class="status {st}">{'Done' if st == 'done' else
                                    'In progress' if st == 'now' else
                                    'Once access arrives'}</span>
        <h3>{title}</h3>
        <p>{body}</p>
        <ul>{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
        <div class="risk">{risk}</div>
      </div>
    </div>""" for i, (st, title, body, bullets, risk) in enumerate(STAGES, 1))

approach = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="eyebrow">For Sandy &mdash; instead of a call</div>
    <h1>How I would run the <em>Calm Life Skills</em> refresh</h1>
    <p>You asked for a call to talk through the approach. I do not do calls,
      so here is the same conversation written down, which has the advantage
      that you can re-read it, forward it to your son, and hold me to it.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="lead">
      <p>Everything below is based on what your site actually does today,
        measured rather than assumed. The numbers come from your sitemap,
        your page source and your Shopify store.</p>
    </div>

    <div class="facts">
      <div class="fact"><strong>776</strong><span>addressable pages in your
        sitemap</span></div>
      <div class="fact"><strong>~13</strong><span>page templates behind
        them</span></div>
      <div class="fact"><strong>~70</strong><span>destinations in your current
        menu</span></div>
      <div class="fact"><strong>5</strong><span>links in the supplied
        design's menu</span></div>
      <div class="fact"><strong>4</strong><span>pages the supplied design
        covers</span></div>
      <div class="fact"><strong>2014</strong><span>last date stamped on your
        sitemap</span></div>
    </div>
  </div>
</section>

<section style="background:var(--cream-warm)">
  <div class="wrap">
    <div class="section-head" style="text-align:left;max-width:none">
      <div class="eyebrow">The plan</div>
      <h2 style="font-size:34px">Six stages, in this order</h2>
    </div>
{stage_html}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head" style="text-align:left;max-width:none">
      <div class="eyebrow">The awkward questions, answered up front</div>
      <h2 style="font-size:34px">Things you would have asked on the call</h2>
    </div>

    <dl class="qa">
      <dt>How do I pay you?</dt>
      <dd>As we go. I do a piece, you look at it, and if you are happy I ask
        for a small release for that piece. I do not quote a lump sum up
        front and I do not ask for money for work you have not seen. The
        three pages you already have were free, and I said so at the time.</dd>

      <dt>What happens if I do not like a template?</dt>
      <dd>You say so and I change it, before it goes anywhere near your
        codebase. That is the entire reason the templates come first.</dd>

      <dt>Can we undo this if it goes wrong?</dt>
      <dd>Yes. The old theme stays on the server rather than being deleted,
        and the hand-over note tells you exactly which files to put back. A
        revert should be minutes, not a rebuild.</dd>

      <dt>Will my Google rankings survive?</dt>
      <dd>Through the redesign, yes &mdash; no URL changes, no content
        changes, and every one of the roughly 70 menu destinations stays
        linked. Through the domain move, only if the redirects are done
        properly, which is why it is its own stage.</dd>

      <dt>How long?</dt>
      <dd>Honestly, it depends mostly on how fast approvals and access come
        back, not on how fast I work. The templates I can keep producing now.
        Integration cannot start until there is a staging copy to do it on.</dd>
    </dl>

    <div class="notbuilt">
      <h3>What this project does not include</h3>
      <ul>
        <li><strong>Your Shopify shop.</strong> It lives on a different
          system at shop.calm.com.au and is not part of the PHP codebase. You
          said to leave it as is, so it keeps its current theme. The new pages
          link into it and those links all work, but the shop itself will not
          look like the new design until it is done as its own project.</li>
        <li><strong>New content.</strong> Words, articles and images stay as
          they are. This is a visual layer change.</li>
        <li><strong>The domain move itself</strong>, unless you ask for it.
          It is listed above as stage six because it needs to be planned, but
          it is a separate piece of work from the refresh.</li>
        <li><strong>Email on the new domain.</strong> calmlifeskills.com
          currently points its mail at the registrar's free forwarding. If you
          want real mailboxes there, that is worth sorting separately, before
          anything is printed with the new name on it.</li>
      </ul>
    </div>
  </div>
</section>

<section style="background:var(--cream-warm)">
  <div class="wrap">
    <div class="section-head" style="text-align:left;max-width:none">
      <div class="eyebrow">Over to you</div>
      <h2 style="font-size:34px">What I need to keep moving</h2>
    </div>
    <div class="lead">
      <p><strong>Nothing, to carry on building templates.</strong> I can keep
        producing those on my own side and you approve them as they appear.</p>
      <p><strong>To start integration:</strong> FTP or SSH plus a database
        user from your son, and a staging subdomain closed to search
        engines.</p>
      <p><strong>Decisions I am waiting on:</strong> whether PP#2 is $14.95
        USD or $20.00 AUD; whether the three meditation names that differ
        between the design and your shop should follow the design or the shop;
        whether the design's &ldquo;How It Works&rdquo; replaces Getting
        Started or sits beside it; and which template you want next.</p>
    </div>
  </div>
</section>
"""

(OUT / "approach.html").write_text(shell(
    "How I would run the Calm Life Skills refresh",
    "The approach, sequencing and risks for the Calm Life Skills design "
    "refresh, written in place of a call.",
    approach,
    extra_css="calm-approach.css",
), encoding="utf-8")

print("built approach.html")
