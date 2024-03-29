
from lib.htmlephant import (
    Address,
    Anchor,
    Div,
    Img,
    NOEL,
    Span,
    Time,
)


Body = lambda context, post, author, show_avatar=True: (
    Div(
        _class="byline",
        children=(
            (Img(
                src=context.image_url(author['avatar_image']),
                alt="author avatar"
            ) if show_avatar else NOEL),
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
            Time(post["datetime"], datetime=post["datetime"])
        )
    ),
)
