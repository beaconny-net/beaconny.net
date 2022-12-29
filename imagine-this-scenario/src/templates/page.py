
from lib.htmlephant import Link
from components import header


Head = lambda: (
    Link(rel="stylesheet", href="css/page.css"),
)


Body = lambda base_path, site_title, site_subtitle: header.Body(
    base_path=base_path,
    title=site_title,
    subtitle=site_subtitle
)
