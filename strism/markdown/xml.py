from __future__ import annotations
from dataclasses import dataclass
from io import StringIO
import re
from typing import Final, Optional, Pattern


@dataclass(frozen=True)
class _Patterns:
    image_path: Pattern = re.compile(r'"([^"]+.png)"')
    tag: Pattern = re.compile(r"<([a-z-_0-9]+)")
    span: Pattern = re.compile(r'<span\s+name="[^"]+">')
    small_caps: Pattern = re.compile(r'<span\s+class="small-caps">([A-Z]+)</span>')


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
    context: _Context
    contents: list[_Inline]

    next_tags = {
        "aside",
        "challenges-p",
        "challenges-list-p",
        "design-p",
        "design-list-p",
        "list-p",
        "p",
    }

    def _is_next(self, tag: str, previous_tag: str) -> bool:
        if tag == previous_tag:
            return tag in self.next_tags

        if tag.endswith("list-p"):
            return "ordered-" in previous_tag

        # if tag != "xml":
        #     buffer.write(f"<{tag}>")


@dataclass
class _Inline:
    tag: Optional[str]
    text: str

    @classmethod
    def create(cls, tag: str, text: str = ""):
        return cls(tag, text)

    def is_text(self):
        return self.tag is not None

    def __repr__(
        self,
        buffer: StringIO,
        context: _Context,
    ):
        if not self.tag:
            buffer.write(self.text)
            return

        # [TODO] finish

    def pprint(self):
        pass


@dataclass
class _Xml:
    _patterns: _Patterns
    buffer: StringIO

    paragraphs: list[_Paragraph]

    _pending_paragraph: bool

    inlines: list[_Inline]

    context: _Context = _Context("main", None)


# class _Apply_:
#     def change_span_locators_to_visible_markers(self):
#         pass

#     def discard_design_note_divs(self):
#         pass

#     def covnert_image_tags_to_paths(self):
#         pass

class _Visit_(_Xml):
    @staticmethod
    def visit(node: Text):
        text = node.text

        # if (text.isEmpty) return;

        # // There are a couple of hand-coded HTML ellipses inside an HTML table.
        # text = text.replaceAll(
        #     '<span class="ellipse">&thinsp;.&thinsp;.&thinsp;.</span>', "&#8230;");

        # // Convert the small-caps bitwise operator spans in "Optimization" to
        # // custom tags.
        # text = text.replaceAllMapped(
        #     _smallCapsPattern, (match) => "<bitwise>${match[1]}</bitwise>");

        for key, val in Xml.BitwiseOps():
            text = text.replace(key, val)

    def has_visited_previous_element(self, elt: Element) -> bool:
        if elt.tag == "p":
            self._reset_paragraph()

#         if elt.tag == "blockquote":
#             self._push("quote")

#         if elt.tag == "a":
#             return 

#         if elt.tag in ["li", "p"]:
#             pass

    def visit_prev(self, elt: Element):
        pass

    def visit_next(self, elt: Element):
        if elt.tag in ["blockquote", "h2", "h3", "pre"]:
            self._pop()
        
        elif elt.tag in ["ol", "ul"]:
            if self._context.name in ["first", "item"]:
                self._pop()

        elif elt.tag in ["code", "em", "small", "strong"]:
            self._add_inline(self.inlines.remove_last())

        # [TODO] fiish


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
