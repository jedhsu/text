from dataclasses import dataclass


@dataclass
class FontVariant:
    decorated_font_face: type
    alternates: type
    caps: type
    east_asian: type
    ligatures: type
    numeric: type
    position: type
