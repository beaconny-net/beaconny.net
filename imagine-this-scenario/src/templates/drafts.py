
from lib.htmlephant import (
    Main,
    Paragraph,
    Section,
    Style,
    Title,
)

from components import post_list


Head = lambda context: (
    Title((site:=context["site"])["title"]),
    Style(f"""
@media screen and (min-width: 1024px) {{
  header {{
    background-image: url("{context.image_url(site['drafts_header_background_image'])}");
  }}
}}
    """)
)


def Body(context):
    posts = context["posts"]
    authors = context["authors"]
    return (
        Main(
        _class="drafts",
        children=(
            Section(children=(
                Paragraph("These posts are in various states of development."),
                post_list.Body(context, (x for x in posts if x["draft"]), authors),
            )),
        )),
    )
