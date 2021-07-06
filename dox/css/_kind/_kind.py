"""

    *Kind*

  Second kind.

  In HTML, instances include element, class, ident, pseudo-class, pseudo-element.

  Importantly, this allows the instantiation of custom XML types.

"""

from abc import ABCMeta

__all__ = ["Kind"]


class Kind:
    __metaclass__ = ABCMeta
