
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


Head = lambda context: (
    Title(context["site"]["title"]),
)


def Body(context):
    base_path = context["site"]["base_path"]
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
                            href=f"{base_path}/{post['slug']}"
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
