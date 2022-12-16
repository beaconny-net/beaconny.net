
from lib.htmlephant import (
    Paragraph,
    Span,
)


class UnescapedParagraph(Paragraph):
    ESCAPE_TEXT = False

class UnescapedSpan(Span):
    ESCAPE_TEXT = False
