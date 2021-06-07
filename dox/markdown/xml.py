from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Optional, Pattern


@dataclass(frozen=True)
class _Patterns:
    image_path: Pattern = re.compile(r'"([^"]+.png)"')
    tag: Pattern = re.compile(r"<([a-z-_0-9]+)")
    span: Pattern = re.compile(r'<span\s+name="[^"]+">')
    small_caps: Pattern = re.compile(r'<span\s+class="small-caps">([A-Z]+)</span>')


# @dataclass
# class _Xml:
#     _patterns: _Patterns

# class _Apply_:
#     def change_span_locators_to_visible_markers(self):
#         pass

#     def discard_design_note_divs(self):
#         pass

#     def covnert_image_tags_to_paths(self):
#         pass

# class _Visit_:
#     def visit(node: Text):
#         pass

#     def has_visited_previous_element(el: Element) -> bool:
#         pass

#     def visit_next_element(elt: Element):
#         pass

# class _Render_:
#     def render(Sequence[Node]) -> str:
#         pass


class Xml:
    pass


@dataclass
class _Context:
    name: str
    parent: Optional[_Context]

    def __contains__(self, name: str) -> bool:
        # [TODO] this ugly-ish but practical procedural stuff would be good candidate for macro
        node = self
        while node:
            if node.name == name:
                return True
            node = node.parent
        return False

    def __in__(self, name: str) -> bool:
        return self.parent and name in self.parent

    def depth(self):
        depth = 0

        # [TODO] finish...


@dataclass
class _Paragraph:
    pass


@dataclass
class _Inline:
    tag: str
    text: str

    def is_text(self):
        pass

    def pprint(self):
        pass
