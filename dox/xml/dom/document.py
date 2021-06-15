from abc import ABCMeta, abstractmethod
from typing import Optional


class Document:

    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def doctype(self):
        """
        Document Type Declaration.

        """
        pass

    @property
    @abstractmethod
    def document_element(self):
        pass

    def create_element(self):
        pass

    def create_text_node(self):
        pass

    def create_comment(self):
        pass

    def create_cdata_section(self):
        pass

    def create_processing_instruction(self):
        pass

    def create_attribute(self):
        pass

    def create_entity_reference(self):
        pass

    def create_element_namespace(self):
        pass

    def create_attribute_namespace(self):
        pass

    def create_document_fragment(self):
        pass

    def get_elements_by_tag_name(self):
        pass

    def get_elements_by_tag_name_namespace(self):
        pass

    def get_elements_by_id(self):
        pass

    def import_node(self):
        pass


class DocumentType:

    __metaclass__ = ABCMeta

    def name(self) -> str:
        pass

    @property
    def entities(self) -> NamedNodeMap:
        pass

    @property
    def notation(self) -> NamedNodeMap:
        pass

    @property
    def internal_subset(self) -> str:
        pass

    @property
    def public_id(self):
        pass
