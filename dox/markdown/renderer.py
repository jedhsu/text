from dataclasses import dataclass


class BlockTags:
    blockquote = "blockquote"
    div = "div"

    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"

    hr = "hr"
    li = "li"
    ol = "ol"
    p = "p"
    pre = "pre"
    ul = "ul"


@dataclass
class HtmlRenderer:
    buffer: str  # [TODO] string buffer ugh
