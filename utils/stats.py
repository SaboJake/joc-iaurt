

class Stats:
    def __init__(self, vitality: int, strength: int, intelligence: int, speed: int, focus: int):
        self.vitality = vitality
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.focus = focus

    def __add__(self, other):
        return Stats(self.vitality + other.vitality, self.strength + other.strength, self.intelligence + other.intelligence, self.speed + other.speed, self.focus + other.focus)

    # TO DO: implement piercing and defence stats
    # piercing - elemental/physical, improves damage and crit chance
    # defence - elemental/physical, reduces damage taken