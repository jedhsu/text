from ..base import AtRule


class ViewPort(AtRule):
    viewport_fit: property
    user_zoom: property
    orientation: property
    min_zoom: property

    height_at_viewport: type
    width_at_viewport: type
    zoom_at_viewport: type
