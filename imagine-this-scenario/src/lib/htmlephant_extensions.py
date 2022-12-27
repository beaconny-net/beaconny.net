
from lib.htmlephant import (
    Div,
    Paragraph,
    Span,
)


class UnescapedDiv(Div):
    ESCAPE_TEXT = False


class UnescapedParagraph(Paragraph):
    ESCAPE_TEXT = False


class UnescapedSpan(Span):
    ESCAPE_TEXT = False
