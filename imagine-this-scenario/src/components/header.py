
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


BODY_ELS = (
    Header(children=(
        Nav(children=(
            Ol(children=(
                Li(children=(
                    Anchor("beaconny.net", href="https://beaconny.net"),
                )),
            )),
        )),
        H1(children=(
            Span("Imagine This Scenario"),
        )),
        H2(children=(
            Em("Glimpses Into the Possible Futures of Beacon, New York"),
        ))
    )),
)
