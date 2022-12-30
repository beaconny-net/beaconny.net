
from operator import itemgetter

from lib.htmlephant import (
    Anchor,
    Article,
    Em,
    H2,
    Li,
    Main,
    Ol,
    Style,
    Title,
)

from components import byline


Head = lambda context: (
    Title((site:=context["site"])["title"]),
    Style(f"""
@media screen and (min-width: 1024px) {{
  header {{
    background-image: url("{context.image_url(site['header_background_image'])}");
  }}
}}
    """)
)


def Body(context):
    posts = context["posts"]
    authors = context["authors"]
    return (
        Main(
        _class="index",
        children=(
            Ol(children=(
                Li(children=(
                    Article(children=(
                        Anchor(
                            children=(H2(post["title"]),),
                            href=context.post_url(post["slug"]),
                        ),
                        *byline.Body(
                            context,
                            post=post,
                            author=authors[post["author"]],
                            show_avatar=False,

                        )
                    )),
                ))
                for post in sorted(posts, key=itemgetter("datetime"), reverse=True)
            )),
        )),
    )
