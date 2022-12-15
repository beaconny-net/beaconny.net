
from lib.frowntown import parse
from lib.htmlephant import (
    Article,
    H2,
    Main,
    Paragraph,
    Title,
)

from components import byline


class UnescapedParagraph(Paragraph):
    ESCAPE_TEXT = False


Head = lambda post_title: (
    Title(post_title),
)


Body = lambda post, author: (
    Main(
        _class=f"post _{post['slug'].lstrip('/')}",
        children=(
            Article(children=(
                *byline.Body(
                    post=post,
                    author=author,
                    show_avatar=True,

                ),
                H2(post["title"]),
                *(UnescapedParagraph(parse(x)) for x in post["paragraphs"]),
            )),
        )
    ),
)
