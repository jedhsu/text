"""

    *Cascade: Phantom-Class*

"""

__all__ = ["CascadePhantomClass"]


class CascadePhantomClass(
    CascadePhantomKind,
):
    ident: str

    @property
    @classmethod
    def syntax(cls) -> str:
        return f":{cls.ident}"
