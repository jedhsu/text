from dataclasses import dataclass


@dataclass
class Frequency:
    frequency: type
    percentage: type


@dataclass
class FrequencyUnits:
    Hz = "#Hz"
    kHz = "#kHz"
