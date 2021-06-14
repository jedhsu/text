from dataclasses import dataclass


@dataclass
class Time:
    time: type
    time_percentage: type
    timing_function: type


@dataclass
class TimeUnit:
    s = "#s"
    ms = "#ms"
