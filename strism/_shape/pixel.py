"""

    *Pixel*

"""


class Pixel(
    int,
):
    def __init__(
        self,
        integer: int,
    ):
        super(Pixel, self).__new__(
            int,
            integer,
        )
