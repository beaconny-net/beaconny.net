
from lib.htmlephant import (
    Address,
    Anchor,
    Div,
    Img,
    Span,
    Time,
)


Head = lambda post, author: ()

Body = lambda post, author: (
    Div(
        _class="byline",
        children=(
            Img(src=author["avatarUrl"], alt="author avatar"),
            Address(
                _class="author",
                children=(
                    Span("By "),
                    Anchor(
                        author["name"],
                        rel="author",
                        href=author["url"]
                    )
                )
            ),
            Span(" on "),
            Time(post["datetime"], pubtime="", datetime=post["datetime"])
        )
    ),
)
