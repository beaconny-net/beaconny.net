
from operator import itemgetter

from lib.htmlephant import (
    Anchor,
    Article,
    H2,
    Ol,
    Li,
)

from components import byline


Body = lambda context, posts, authors: Ol(children=(
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
))
