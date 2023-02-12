"""Super dumb and simple Markdown-ish markup to HTMLephant element converter."""

import re

from lib import tests
from lib.htmlephant import (
    Anchor,
    BlockQuote,
    Em,
    HTMLElement,
    Img,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Li,
    Ol,
    Strong,
)


__all__ = ("parse",)


###############################################################################
# HTMLephant Subclasses
###############################################################################


class InlineFigure(HTMLElement):
    CHILD_INDENT = 0
    TAG_NAME = 'figure'


class InlineFigureCaption(HTMLElement):
    CHILD_INDENT = 0
    TAG_NAME = 'figcaption'


class InlineAnchor(Anchor):
    CHILD_INDENT = 0


class InlineEm(Em):
    CHILD_INDENT = 0


class InlineStrong(Strong):
    CHILD_INDENT = 0


class UnescapedLi(Li):
    ESCAPE_TEXT = False


###############################################################################
# Helper Functions
###############################################################################


gen_to_str = lambda gen: "".join(gen).replace("\n", "")

build_url = lambda base_path, path: \
    ((base_path.rstrip("/") + "/") if base_path else "") + path.lstrip("/")


###############################################################################
# Search Patterns
###############################################################################


ITALIC_PATTERN = "(?:^|(?<=\s))_(?P<text>[^_]+)_(?:$|(?=\s))"

STRONG_PATTERN = "(?:^|(?<=\s))\*\*(?P<text>[^\*]+)\*\*(?:$|(?=\s))"

HEADER_PATTERN = "^(?P<level>#+)\s*(?P<text>.+)"

Title = lambda name: f'(?:\s+"(?P<{name}>[^"]+)")'

Link = lambda text_pattern="(?P<text>[^\]]+)": \
    f"(?<!\!)\[{text_pattern}\]\((?P<href>[^\)\s]+){Title('link_title')}?\)"

LINK_PATTERN = Link()

LIST_PATTERN = "^-(?P<list_style_type>[^\[]+)?\[(?P<items>[^\]]+)]$"
LIST_ITEM_PATTERN = re.compile("(?P<item>[^|]+)(?:|\s*)?")

IMAGE_PATTERN = f"!\[(?P<alt_text>[^\]]+)\]\((?P<src>[^\)\s]+){Title('image_title')}?\)"

LINKED_IMAGE_PATTERN = f"^{Link(IMAGE_PATTERN)}"

BLOCK_QUOTE_PATTERN = "^\>(?:\((?P<cite>[^\)]+)\))?\s*(?P<text>.+)"


###############################################################################
# Replacement Handlers
###############################################################################


def italic_handler(context, match):
    return gen_to_str(InlineEm(match.group(1)).html())


def strong_handler(context, match):
    return gen_to_str(InlineStrong(match.group(1)).html())


def header_handler(context, match):
    match_d = match.groupdict()
    el = (H1, H2, H3, H4, H5, H6)[len(match_d["level"])]
    return gen_to_str(el(match_d["text"]).html())


def list_handler(context, match):
    match_d = match.groupdict()
    list_style_type = match_d["list_style_type"] or "disc"
    items_str = match_d["items"]
    items = [parse(x) for x in LIST_ITEM_PATTERN.findall(items_str)]
    return gen_to_str(Ol(
        children=(UnescapedLi(item) for item in items),
        style=f"list-style-type: {list_style_type};"
    ).html())


def image_handler(context, match):
    match_d = match.groupdict()
    alt_text = match_d["alt_text"]
    image_title = match_d["image_title"]
    src = build_url(context["href_base_path"], match_d["src"])
    return gen_to_str(
        InlineFigure(children=(
            Img(src=src, alt=alt_text, title=image_title or alt_text),
            InlineFigureCaption(image_title or alt_text),
        )).html()
    )


def link_handler(context, match):
    match_d = match.groupdict()
    text = match_d["text"]
    href = build_url(context["href_base_path"], match_d["href"])
    return gen_to_str(InlineAnchor(text, href=href, title=match_d["link_title"]).html())


def linked_image_handler(context, match):
    match_d = match.groupdict()
    alt_text = match_d["alt_text"]
    href = build_url(context["href_base_path"], match_d["href"])
    image_title = match_d["image_title"]
    src = build_url(context["href_base_path"], match_d["src"])
    return gen_to_str(
        InlineAnchor(
            href=href,
            title=match_d["link_title"],
            children=(
                InlineFigure(children=(
                    Img(src=src, alt=alt_text, title=image_title or alt_text),
                    InlineFigureCaption(image_title or alt_text),
                )),
            )
        ).html()
    )


def block_quote_handler(context, match):
    match_d = match.groupdict()
    return gen_to_str(BlockQuote(match_d["text"], cite=match_d["cite"]).html())


###############################################################################
# Pattern => Replacer Map and parse() Function
###############################################################################


PATTERN_REPLACER_PAIRS = tuple((
    (re.compile(k), v) for k, v in (
        (HEADER_PATTERN, header_handler),
        (IMAGE_PATTERN, image_handler),
        (ITALIC_PATTERN, italic_handler),
        (LINKED_IMAGE_PATTERN, linked_image_handler),
        (LINK_PATTERN, link_handler),
        (LIST_PATTERN, list_handler),
        (STRONG_PATTERN, strong_handler),
        (BLOCK_QUOTE_PATTERN, block_quote_handler),
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
        '<figure><img src="images/test.png" alt="alt text" title="alt text"><figcaption>alt text</figcaption></figure>'),
    (
        ('![alt text](images/test.png "with title")',),
        '<figure><img src="images/test.png" alt="alt text" title="with title"><figcaption>with title</figcaption></figure>'
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
