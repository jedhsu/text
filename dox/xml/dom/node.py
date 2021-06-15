from __future__ import annotations
from typing import Optional, Sequence


class Node:
    def name(self):
        pass

    @property
    def value(self):
        pass

    @property
    def type(self):
        pass

    @property
    def parent(self) -> Node:
        pass

    @property
    def children(self) -> Sequence[Node]:
        pass

    @property
    def first_child(self) -> Optional[Node]:
        pass

    @property
    def last_child(self) -> Optional[Node]:
        pass

    @property
    def previous_sibling(self) -> Optional[Node]:
        pass

    @property
    def next_sibling(self) -> Optional[Node]:
        pass

    @property
    def attributes(self) -> NamedNodeMap:
        pass

    @property
    def owner_document(self) -> Document:
        pass

    def namespace_uri(self) -> Optional[str]:
        pass

    @property
    def prefix(self) -> str:
        """
        Namespace prefix.

        """
        pass

    def insert_before(self):
        pass

    def replace_child(self):
        pass

    def append_child(self):
        pass

    def has_child_nodes(self):
        pass

    def clone_node(self):
        pass
