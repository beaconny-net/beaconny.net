
from lib.htmlephant import (
    Div,
    HTMLElement,
    Paragraph,
    Span,
)


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
