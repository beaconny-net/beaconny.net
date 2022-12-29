
from lib.htmlephant import Link
from components import header


Head = lambda context: (
    Link(rel="stylesheet", href=f"{context['site']['base_path']}/css/page.css"),
)


Body = lambda context: header.Body(context)
