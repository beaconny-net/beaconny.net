
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


Body = lambda base_path, title, subtitle: (
    Header(children=(
        Nav(children=(
            Ol(children=(
                Li(children=(
                    Anchor("home", href=base_path),
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
