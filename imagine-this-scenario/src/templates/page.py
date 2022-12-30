
from lib.htmlephant import Link
from components import header


Head = lambda context: (
    Link(rel="stylesheet", href=context.css_url("page.css")),
)


Body = lambda context, page_type: header.Body(context, page_type)
