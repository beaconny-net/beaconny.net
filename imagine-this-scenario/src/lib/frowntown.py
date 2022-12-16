"""Super dumb and simple Markdown-ish markup to HTMLephant element converter."""

import re

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


ITALIC_PATTERN = r"_(?P<text>[^_]+)_"

IMAGE_PATTERN = r"!\[(?P<alt_text>[^\]]+)\]\((?P<url>[^\)]+)\)"


###############################################################################
# Replacement Handlers
###############################################################################


def image_handler(context, match):
    match_d = match.groupdict()
    alt_text = match_d["alt_text"]
    url = build_url(context["href_base_path"], match_d["url"])
    return gen_to_str(
        InlineAnchor(
            href=url,
            _class="image",
            children=(
                Img(src=url, alt=alt_text),
            )
        ).html()
    )


def italic_handler(context, match):
    return gen_to_str(InlineEm(match.group(1)).html())


###############################################################################
# Patter => Replacer Map and parse() Function
###############################################################################


PATTERN_REPLACER_PAIRS = tuple((
    (re.compile(k), v) for k, v in (
        (ITALIC_PATTERN, italic_handler),
        (IMAGE_PATTERN, image_handler),
    )
))


def parse(text, href_base_path=None):
    context = {
        "href_base_path": href_base_path
    }
    for pattern, replacer in PATTERN_REPLACER_PAIRS:
        text = pattern.sub(lambda m: replacer(context, m), text)
    return text
