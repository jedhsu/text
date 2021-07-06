"""

    *Box-Ratios*

  Box ratios, as percentage of content area.

  Assumes (1, 1) for content area.

"""

from dataclasses import dataclass

from ._ratio import BoxRatio


@dataclass
class BoxRatios:
    padding: BoxRatio
    border: BoxRatio
    margin: BoxRatio
