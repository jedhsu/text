"""
A keyword added to a selector that specifices special state.

"""


class PseudoClass(Keyword, type):
    pass


class Linguistic:
    dir: PseudoClass
    lang: PseudoClass


class Location:
    any_link: PseudoClass
    link: PseudoClass
    visited: PseudoClass
    local_link: PseudoClass
    target: PseudoClass
    target_within: PseudoClass
    scope: PseudoClass


class UserAction:
    hover: PseudoClass
    active: PseudoClass
    focus: PseudoClass
    focus_visible: PseudoClass
    focus_within: PseudoClass


class Timing:
    current: PseudoClass
    past: PseudoClass
    future: PseudoClass


class ResourceState:
    # call run state instead?

    playing: PseudoClass
    paused: PseudoClass


class Input:
    autofill: PseudoClass

    enabled: PseudoClass
    disabled: PseudoClass

    read_only: PseudoClass
    read_write: PseudoClass

    placeholder_shown: PseudoClass

    default: PseudoClass

    checked: PseudoClass

    indeterminate: PseudoClass

    blank: PseudoClass

    valid: PseudoClass
    invalid: PseudoClass

    in_range: PseudoClass
    out_of_range: PseudoClass

    required: PseudoClass
    optional: PseudoClass

    user_valid: PseudoClass
    user_invalid: PseudoClass


class Selectors:
    # [TODO] clarify this one!
    # [Logical]?
    has: PseudoClass
    __is: PseudoClass
    where: PseudoClass
    __not: PseudoClass
    empty: PseudoClass

    # [Directional]?
    top: PseudoClass
    right: PseudoClass
    bottom: PseudoClass
    left: PseudoClass

    # [Graphical]?
    fullscreen: PseudoClass
    picture_in_picture: PseudoClass


defined: PseudoClass  # [TODO] where?
supports: AtRule
