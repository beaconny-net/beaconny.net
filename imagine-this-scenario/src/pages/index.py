
from lib.htmlephant import (
    Anchor,
    Article,
    Em,
    H2,
    Li,
    Main,
    Ol,
)

from components import (
    byline,
    page,
)


Head = lambda context: (
    *page.HEAD_ELS,
)


Body = lambda context: (
    *page.BODY_ELS,
    Main(
        _class="index",
        children=(
            Ol(children=(
                Li(children=(
                    Article(children=(
                        *byline.Body(post, context["authors"][post["author"]]),
                        Anchor(children=(H2(post["title"]),), href=post["slug"])
                    )),
                ))
                for post in context["posts"]
            )),
        )
    ),
)
