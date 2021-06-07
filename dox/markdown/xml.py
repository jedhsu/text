from __future__ import annotations
from dataclasses import dataclass
from io import StringIO
import re
from typing import Optional, Pattern

@dataclass(frozen=True)
class _Patterns:
    image_path: Pattern = re.compile(r'"([^"]+.png)"')
    tag: Pattern = re.compile(r"<([a-z-_0-9]+)")
    span: Pattern = re.compile(r'<span\s+name="[^"]+">')
    small_caps: Pattern = re.compile(r'<span\s+class="small-caps">([A-Z]+)</span>')


@dataclass
class _Xml:
    _patterns: _Patterns
    buffer: StringIO

    paragraphs: list[_Paragraph]
    
    _pending_paragraph: bool

    inlines: list[_Inline]

    context: _Context = _Context("main")
    

# class _Apply_:
#     def change_span_locators_to_visible_markers(self):
#         pass

#     def discard_design_note_divs(self):
#         pass

#     def covnert_image_tags_to_paths(self):
#         pass

class _Visit_(_Xml):
    def visit(node: Text):
        pass

    def has_visited_previous_element(el: Element) -> bool:
        pass
    
    def visit_prev(self, elt: Element):
        pass
    def visit_next(self, elt: Element):
        pass

class _Render_:
    @staticmethod
    def render(nodes: list[Node]) -> str:
        for node in nodes:
            node.accept(self)

        buffer = StringIO()
        buffer.write("<chapter>")




class Xml:
    BitwiseOps = {
        "&eacute;": "&#233;",
        "&ensp;": "&#8194;",
        "&ldquo;": "&#8220;",
        "&nbsp;": "&#160;",
        "&rdquo;": "&#8221;",
        "&rsquo;": "&#8217;",
        "&rarr;": "&#8594;",
        "&sect;": "&#167;",
        "&thinsp;": "&#8201;",
        "&times;": "&#215;",
        "<br>": "<br/>",
    }
    
    TableSubs = {
        "<table>": "[table]",
        "</table>": "[/table]",
        "<thead>": "[thead]",
        "</thead>": "[/thead]",
        "<tbody>": "[tbody]",
        "</tbody>": "[/tbody]",
        "<tr>": "[tr]",
        "</tr>": "[/tr]",
        "<td>": "[td]",
        "</td>": "[/td]",
    }

    def custom_bitwise_ops(self):
        # text = text.replaceAllMapped(
        #     _smallCapsPattern, (match) => "<bitwise>${match[1]}</bitwise>");

        # text = text

    def table_substitutions():
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
