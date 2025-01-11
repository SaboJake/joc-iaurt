from units.unit import Unit
from utils.stats import Stats
from abilities.enemy_ability_list import attack1, heal1

garius = Unit("Garius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
garius.abilities = [attack1, heal1]