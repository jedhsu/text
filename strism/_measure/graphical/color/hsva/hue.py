"""

    *Hue*

  n mod 360 forms a mathematical ring.

"""

from ....ring import Ring

# [TODO] metaclass?


class Hue(
    Ring[360],
):
    pass
