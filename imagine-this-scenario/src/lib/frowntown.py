"""Super dumb and simple Markdown-ish markup to HTMLephant element converter."""

import re

from lib import tests
from lib.htmlephant import (
    Anchor,
    Em,
    Img,
)


__all__ = ("parse",)


###############################################################################
# HTMLephant Subclasses
###############################################################################


class InlineAnchor(Anchor):
    CHILD_INDENT = 0


class InlineEm(Em):
    CHILD_INDENT = 0


###############################################################################
# Helper Functions
###############################################################################


gen_to_str = lambda gen: "".join(gen).replace("\n", "")

build_url = lambda base_path, path: \
    ((base_path.rstrip("/") + "/") if base_path else "") + path.lstrip("/")


###############################################################################
# Search Patterns
###############################################################################


ITALIC_PATTERN = r"(?:^|(?<=\s))_(?P<text>[^_]+)_(?:$|(?=\s))"

Title = lambda name: f'(?:\s+"(?P<{name}>[^"]+)")'

Link = lambda text_pattern="(?P<text>[^\]]+)": \
    f"(?<!\!)\[{text_pattern}\]\((?P<href>[^\)\s]+){Title('link_title')}?\)"

LINK_PATTERN = Link()

IMAGE_PATTERN = f"!\[(?P<alt_text>[^\]]+)\]\((?P<src>[^\)\s]+){Title('image_title')}?\)"

LINKED_IMAGE_PATTERN = Link(IMAGE_PATTERN)


###############################################################################
# Replacement Handlers
###############################################################################


def italic_handler(context, match):
    return gen_to_str(InlineEm(match.group(1)).html())


def image_handler(context, match):
    match_d = match.groupdict()
    alt_text = match_d["alt_text"]
    src = build_url(context["href_base_path"], match_d["src"])
    return gen_to_str(
        Img(src=src, alt=alt_text, title=match_d["image_title"] or alt_text).html()
    )


def link_handler(context, match):
    match_d = match.groupdict()
    text = match_d["text"]
    href = build_url(context["href_base_path"], match_d["href"])
    return gen_to_str(InlineAnchor(text, href=href, title=match_d["link_title"]).html())


def linked_image_handler(context, match):
    match_d = match.groupdict()
    href = build_url(context["href_base_path"], match_d["href"])
    src = build_url(context["href_base_path"], match_d["src"])
    alt_text = match_d["alt_text"]
    return gen_to_str(
        InlineAnchor(
            href=href,
            title=match_d["link_title"],
            children=(
                Img(src=src, alt=alt_text, title=match_d["image_title"] or alt_text),
            )
        ).html())


###############################################################################
# Pattern => Replacer Map and parse() Function
###############################################################################


PATTERN_REPLACER_PAIRS = tuple((
    (re.compile(k), v) for k, v in (
        (LINKED_IMAGE_PATTERN, linked_image_handler),
        (ITALIC_PATTERN, italic_handler),
        (LINK_PATTERN, link_handler),
        (IMAGE_PATTERN, image_handler),
    )
))


@tests(
    (("Plain text",), "Plain text"),
    (("Some _italic_ text",), "Some <em>italic</em> text"),
    (("_leading_ italic text",), "<em>leading</em> italic text"),
    (("trailing italic _text_",), "trailing italic <em>text</em>"),
    (
        ("[test](http://example.com)",),
        '<a href="http://example.com">test</a>'),
    (
        ('[test](http://example.com "with title")',),
        '<a href="http://example.com" title="with title">test</a>'
    ),
    (
        ("![alt text](images/test.png)",),
        '<img src="images/test.png" alt="alt text" title="alt text">'),
    (
        ('![alt text](images/test.png "with title")',),
        '<img src="images/test.png" alt="alt text" title="with title">'
    ),
)
def parse(text, href_base_path=None):
    context = {
        "href_base_path": href_base_path
    }

    # Iterate through patterns by pattern length descending in an attempt to
    # match the largest patterns first.
    for pattern, replacer in sorted(
            PATTERN_REPLACER_PAIRS,
            key=lambda p: len(p[0].pattern),
            reverse=True
    ):
        text = pattern.sub(lambda m: replacer(context, m), text)
    return text
