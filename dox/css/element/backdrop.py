from dataclasses import dataclass


@dataclass
class Backdrop:
    backdrop: PseudoElement
    backdrop_filter: property  # Applies graphical effects *behind* element
    backface_visibility: property  # Sets whether back face of element is visible

    Global = [
        "inherit",
        "initial",
        "unset",
    ]
