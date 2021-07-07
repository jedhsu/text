"""

Text Rendering Precedence

Specifies an ordering for element rendering.

Note that this feels similar to operator precedence in language theory.

"""

__all__ = ["TextRenderingPrecedence"]


class TextRenderingPrecedenceOption:
    Auto = "auto"

    OptimizeSpeed = "optimizeSpeed"
    OptimizeLegibility = "optimizeLegibility"
    GeometricPrecision = "geometricPrecision"
