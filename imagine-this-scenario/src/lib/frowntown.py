"""Super dumb and simple Markdown-ish markup to HTMLephant element converter."""

import re

from lib.htmlephant import (
    Anchor,
    Img,
)


IMAGE_PATTERN = r"!\[(?P<alt_text>[^\]]+)\]\((?P<url>[^\)]+)\)"


gen_to_str = lambda gen: "".join(gen).replace("\n", "")

build_url = lambda base_path, path: \
    ((base_path.rstrip("/") + "/") if base_path else "") + path.lstrip("/")


def image_handler(href_base_path, match):
    match_d = match.groupdict()
    alt_text = match_d["alt_text"]
    url = build_url(href_base_path, match_d["url"])
    return gen_to_str(
        Anchor(
            href=url,
            _class="image",
            children=(
                Img(src=url, alt=alt_text),
            )
        ).html()
    )


pattern_replacer_pairs = tuple((
    (re.compile(k), v) for k, v in (
        (IMAGE_PATTERN, image_handler),
    )
))


def parse(text, href_base_path=None):
    for pattern, replacer in pattern_replacer_pairs:
        text = pattern.sub(lambda m: replacer(href_base_path, m), text)
    return text
