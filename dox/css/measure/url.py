from dataclasses import dataclass


@dataclass
class Url:
    url: type
    url_: Callable
