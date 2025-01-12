from units.unit import Unit
from utils.stats import Stats
from abilities.enemy_ability_list import attack1, heal1, focus_attack, apply_buff, apply_regen, wound_attack, \
    weaken_attack, regen_heal, buff_heal

garius = Unit("Garius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
garius.abilities = [attack1, heal1]

glarius = Unit("Glarius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
glarius.abilities = [focus_attack, heal1]

larius = Unit("Larius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
larius.abilities = [apply_buff, apply_regen, heal1]
marius = Unit("Marius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
marius.abilities = [focus_attack, heal1]

barius = Unit("Barius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
barius.abilities = [wound_attack, weaken_attack, apply_regen, focus_attack]
blarius = Unit("Blarius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
blarius.abilities = [regen_heal, buff_heal, heal1, focus_attack]

harry = Unit("Harry", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
harry.abilities = [focus_attack, wound_attack, weaken_attack, regen_heal, buff_heal, heal1]
emanuel = Unit("Emanuel", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))
emanuel.abilities = [focus_attack, wound_attack, weaken_attack, regen_heal, buff_heal, heal1]

darius = Unit("Darius", Stats(100, 10, 10, 30, 10), Stats(100, 10, 10, 30, 10))
darius.abilities = [focus_attack, wound_attack, weaken_attack, regen_heal, buff_heal, heal1]


