from dataclasses import dataclass


@dataclass
class Cue:
    """
    Matches WebVTT cues.

    """

    cue: PseudoElement
    cue_region: PseudoElement
