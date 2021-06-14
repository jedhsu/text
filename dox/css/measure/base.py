from abc import ABCMeta


class Measure:

    __metaclass__ = ABCMeta


class AbsoluteMeasure(Measure):

    __metaclass__ = ABCMeta


class RelativeMeasure(Measure):

    __metaclass__ = ABCMeta


class PercentageMeasure(RelativeMeasure, float):

    __metaclass__ = ABCMeta
