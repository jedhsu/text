from dataclasses import dataclass
from typing import Any, Optional

from .page import Page


@dataclass
class _Cache:
    templates: dict[str, Template]


class _Build_(_Cache):

    @staticmethod
    def build_chapter_list(part: Page):
        for chapter in part.chapters():
            dct = {
                "title": chapter.title,
                "number": chapter.number_string,
                "file": chapter.file_name,
                "design_note": chapter.design_note.replace_all("'", "&rsquo"),
            }

    def build_part_data(self, book: Book, part_index: int):
        pass

    def build_sections(self, page: Page):
        pass

class _Render_(_Cache):
    @staticmethod
    def render(
        book: Book,
        page: Page,
        body: str,
        template: Optional[str],
    ):
        _data: dict[str, Any]
        _data = {
            "has_title": not self.page.title,
            "title": self.page.title,

            "has_part": part != null,
            "part": part,

            "body": body,

            "sections": _makeSections(page),
            "chapters": chapters,

            "design_note": page.designNote,

            "has_design_note": page.designNote != null,
            "has_challenges": page.hasChallenges,
            "has_challenges_or_design_note":
              # page.hasChallenges || page.designNote != null,
            
            "has_number": page.numberString != "",
            "number": page.numberString,

            "has_prev": previousPage != null,
            "prev": previousPage?.title,
            "prev_file": previousPage?.fileName,

            "has_next": nextPage != null,
            "next": nextPage?.title,
            "next_file": nextPage?.fileName,
            "next_type": nextType,

            "has_up": up != null,
            "up": up,
            "up_file": up != null ? toFileName(up) : null,

            "part_1": _makePartData(book, 0),
            "part_2": _makePartData(book, 1),
            "part_3": _makePartData(book, 2),
        };

    pass
