
from lib.frowntown import parse
from lib.htmlephant_extensions import (
    UnescapedDiv,
    UnescapedParagraph,
)

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
        _class=f"post _{post['slug'].lstrip('/')}",
        children=(
            Article(children=(
                *byline.Body(
                    post=post,
                    author=author,
                    show_avatar=True,

                ),
                H2(post["title"]),
                *(UnescapedDiv(parsed, _class="figure")
                  if (parsed:=parse(x)).startswith("<")
                  else UnescapedParagraph(parsed)
                  for x in post["paragraphs"]
                ),
            )),
        )
    ),
)
