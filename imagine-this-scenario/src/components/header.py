
from lib.frowntown import parse
from lib.htmlephant_extensions import UnescapedSpan
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
                    UnescapedSpan(parse(title)),
                )),
                H2(children=(
                    UnescapedSpan(parse(subtitle)),
                ))
            )),
        )
