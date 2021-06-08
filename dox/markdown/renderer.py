from collections import deque
from dataclasses import dataclass
from io import StringIO
from typing import Sequence
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
    buffer: StringIO

    _elements: deque[Element]
    _last_visited_tag: Optional[str]

    def render(nodes: Sequence[Node]):
        buffer = StringIO()

        for node in nodes:
            node.accept(self)

        buffer.write()  # [TODO] write lines?

        if self._last_visited_tag in ["p", "li"]:
            content = content.trimleft()

        buffer.write(content)

        self._last_visited_tag = None

    def visit_element_before(elt: Element) -> bool:
        if buffer and elt.tag in self._block_tags:
            buffer.write()

        buffer.write(f"<{elt.tag}")

    def visit_element_after(elt: Element):jKA
        assert self._elements[-1] is elt

        if elt.children and elt.tag in self._block_tags:
            buffer.write()

        # [TODO] blah sems like same pattern



