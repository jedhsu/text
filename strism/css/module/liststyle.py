from dataclasses import dataclass


@dataclass
class ListStyle(Module):
    liststyle: ShorthandProperty

    image: Property
    position: Property
    type: Property
