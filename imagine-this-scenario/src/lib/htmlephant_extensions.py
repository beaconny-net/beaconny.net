
from lib.htmlephant import (
    Anchor,
    Div,
    HTMLElement,
    Paragraph,
    Span,
)


class UnescapedAnchor(Anchor):
    ESCAPE_TEXT = False


class UnescapedDiv(Div):
    ESCAPE_TEXT = False


class UnescapedParagraph(Paragraph):
    ESCAPE_TEXT = False


class UnescapedSpan(Span):
    ESCAPE_TEXT = False


class RawHTML(HTMLElement):
    def __init__(self, html):
        self._html = html

    def html(self, indent):
        return " " * (indent + self.CHILD_INDENT) + self._html
