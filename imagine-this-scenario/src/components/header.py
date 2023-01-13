
from lib.frowntown import parse
from lib.htmlephant import (
    Anchor,
    Em,
    H1,
    H2,
    Header,
    Li,
    Nav,
    Ol,
    Span
)
from lib.htmlephant_extensions import (
    UnescapedAnchor,
    UnescapedSpan,
)


def Body(context, page_name):
    base_path = context["site"]["base_path"]
    title = context["site"]["title"]
    subtitle = context["site"]["subtitle"]
    return (
        Header(
            _class=page_name,
            children=(
                Nav(children=(
                    Ol(children=(
                        Li(children=(
                            (Anchor("home", href=base_path)
                             if page_name != "index" else
                             Span("home")),
                        )),
                        Li(children=(
                            (Anchor("drafts", href=f"{base_path}/drafts")
                             if page_name != "drafts" else
                             Span("drafts")),
                        )),
                        Li(children=(
                            Anchor("beaconny.net", href="https://beaconny.net"),
                        )),
                    )),
                )),
                H1(children=(
                    UnescapedAnchor(parse(title), href=base_path),
                )),
                H2(children=(
                    UnescapedSpan(parse(subtitle)),
                ))
            )),
        )
