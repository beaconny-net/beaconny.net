
from lib.frowntown import parse
from lib.htmlephant_extensions import (
    RawHTML,
    UnescapedParagraph,
)

from lib.htmlephant import (
    Article,
    H2,
    Main,
    Paragraph,
    Style,
    Title,
)

from components import byline


def Head(context, post):
    base_path = context["site"]["base_path"]
    background_image = post["header_background_image"]
    return (
        Title(post["title"]),
        Style(f"""
@media screen and (min-width: 1024px) {{
  header {{
    background-image: url("{base_path}/images/{background_image}");
  }}
}}
        """)
    )



Body = lambda context, post, author: (
    Main(
        _class=f"post _{post['slug'].lstrip('/')}",
        children=(
            Article(children=(
                *byline.Body(
                    context,
                    post=post,
                    author=author,
                    show_avatar=True,

                ),
                H2(post["title"]),
                *(RawHTML(parsed)
                  if (parsed:=parse(block)).startswith("<")
                  else UnescapedParagraph(parsed)
                  for block in post["blocks"]
                ),
            )),
        )
    ),
)
