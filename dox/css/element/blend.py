class BlendMode:
    """
    Sets how element content should blend with element parent & background.

    """

    Normal = "normal"
    Multiply = "multiply"
    Screen = "screen"
    Overlay = "overlay"

    Darken = "darken"
    Lighten = "lighten"

    ColorDodge = "color-dodge"
    ColorBurn = "color-burn"

    HardLight = "hard-light"
    SoftLight = "soft-light"

    Difference = "difference"
    Exclusion = "exclusion"

    # hsva
    Hue = "hue"
    Saturation = "saturation"
    Color = "color"
    Luminosity = "luminosity"


class MixBlendMode(BlendMode):
    pass
