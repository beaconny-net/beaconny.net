
from operator import itemgetter

from lib.htmlephant import (
    Anchor,
    Article,
    Em,
    H2,
    Li,
    Main,
    Ol,
    Title,
)

from components import byline


Head = lambda site_title: (
    Title(site_title),
)


Body = lambda posts, authors: (
    Main(
        _class="index",
        children=(
            Ol(children=(
                Li(children=(
                    Article(children=(
                        Anchor(children=(H2(post["title"]),), href=post["slug"]),
                        *byline.Body(
                            post=post,
                            author=authors[post["author"]],
                            show_avatar=False,

                        )
                    )),
                ))
                for post in sorted(posts, key=itemgetter("datetime"), reverse=True)
            )),
        )
    ),
)
