from typing import Sequence


class _Path:
    points: Sequence[Point]


class _Optimize_:
    def optimize(paths: Paths):
        pass


class PathSpace:
    def get_score(self):
        pass


class _Initialize_:
    def initialize(self, point: Point):
        return Path([point])


class Path:
    ...
