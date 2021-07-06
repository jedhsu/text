"""

    *Phantom-Class*

"""


class PhantomClass(
    PhantomKind,
):
    ident: str

    @property
    @classmethod
    def syntax(cls) -> str:
        return f":{cls.ident}"
