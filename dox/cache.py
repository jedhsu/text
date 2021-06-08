class Cache:
    templates: dict[str, Template]


class _Build_:
    def build_sections(self, page: Page):
        pass

    def build_chapter_list(self, part: Page):
        pass

    def build_part_data(self, book: Book, part_index: int):
        pass


class _Render_:
    pass
