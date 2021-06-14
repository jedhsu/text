@dataclass
class Animation(Property):

    # -- Subproperties
    name: Property
    duration: Property

    timing_function: Property
    delay: Property

    iteration_count: Property
    direction: Property

    fill_mode: Property
    play_state: Property
