from pathlib import Path
from typing import Optional

from .codetag import CodeTag
from .page import Page


class Chapter(Page):
    pass


class _Split_(Chapter):
    async def split_chapter(self, tag: Optional[CodeTag]):
        splits = []

        for file in [chapter.language]:
            splits.append(self.split_source_file())  # [TODO] finish

        await splits

    async def split_source(self, sourcepath: Path):
        pass


class _Generate_(Chapter):
    pass
