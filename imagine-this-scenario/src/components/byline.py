
from lib.htmlephant import (
    Address,
    Anchor,
    Div,
    Img,
    NOEL,
    Span,
    Time,
)


def Body(context, post, author, show_avatar=True):
    base_path = context["site"]["base_path"]
    return (
        Div(
            _class="byline",
            children=(
                (Img(
                    src=f"{base_path}/{author['avatarUrl']}",
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
                Time(post["datetime"], pubtime="", datetime=post["datetime"])
            )
        ),
    )
