
from lib.htmlephant import (
    Article,
    H2,
    Main,
    Paragraph,
    Title,
)

from components import byline


Head = lambda post_title: (
    Title(post_title),
)


Body = lambda post, author: (
    Main(
        _class="post",
        children=(
            Article(children=(
                *byline.Body(
                    post=post,
                    author=author,
                    show_avatar=True,

                ),
                H2(post["title"]),
                *(Paragraph(x) for x in post["paragraphs"]),
            )),
        )
    ),
)
