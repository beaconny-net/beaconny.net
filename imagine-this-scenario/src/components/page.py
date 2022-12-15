
from lib.htmlephant import Link
from . import header


HEAD_ELS = (
    Link(rel="stylesheet", href="css/page.css"),
)

BODY_ELS = (
    *header.BODY_ELS,
)
