

class Stats:
    def __init__(self, vitality: int, strength: int, intelligence: int, speed: int, focus: int, elemental_piercing: int = 0, physical_piercing: int = 0, elemental_defence: int = 0, physical_defence: int = 0):
        self.vitality = vitality
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.focus = focus
        self.elemental_piercing = elemental_piercing
        self.physical_piercing = physical_piercing
        self.elemental_defence = elemental_defence
        self.physical_defence = physical_defence

    def __add__(self, other):
        return Stats(self.vitality + other.vitality, self.strength + other.strength,
                     self.intelligence + other.intelligence, self.speed + other.speed,
                     self.focus + other.focus,
                     self.elemental_piercing + other.elemental_piercing, self.physical_piercing + other.physical_piercing,
                     self.elemental_defence + other.elemental_defence, self.physical_defence + other.physical_defence)

    def __sub__(self, other):
        return Stats(self.vitality - other.vitality, self.strength - other.strength,
                     self.intelligence - other.intelligence, self.speed - other.speed,
                     self.focus - other.focus,
                     self.elemental_piercing - other.elemental_piercing, self.physical_piercing - other.physical_piercing,
                     self.elemental_defence - other.elemental_defence, self.physical_defence - other.physical_defence)

    # TO DO: implement piercing and defence stats
    # piercing - elemental/physical, improves damage and crit chance
    # defence - elemental/physical, reduces damage taken