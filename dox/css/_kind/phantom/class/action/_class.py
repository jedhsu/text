"""

    *Action*

  A user-action phantom-class type.

"""

from .._class import PhantomClass


class UserActionPhantomClass(
    PhantomClass,
):

    focus: PseudoClass
    focus_visible: PseudoClass
    focus_within: PseudoClass
