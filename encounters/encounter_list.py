from encounters.encounter import Encounter
from encounters.enemy_list import garius, glarius, larius, marius, barius, blarius, darius, harry, emanuel
from encounters.item_list import helmet, gloves, weapon1, weapon2, armor, boots, legs, good_helmet, good_gloves, \
    good_weapon1, good_armor, good_legs, good_boots, good_weapon2
from inventory import tricou

encounters = [
    Encounter([garius], 25, 14, [helmet, gloves, weapon1, weapon2, armor, legs, boots], [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7], 1),
    Encounter([glarius], 35, 20, [helmet, gloves, weapon1, weapon2, armor, legs, boots], [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7], 2),
    Encounter([larius, marius], 50, 30, [helmet, gloves, weapon1, weapon2, armor, legs, boots, good_helmet, good_gloves, good_weapon1, good_weapon2, good_armor, good_legs, good_boots], [1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14], 2),
    Encounter([barius, blarius], 100, 60, [helmet, gloves, weapon1, weapon2, armor, legs, boots, good_helmet, good_gloves, good_weapon1, good_weapon2, good_armor, good_legs, good_boots], [1/28, 1/28, 1/28, 1/28, 1/28, 1/28, 1/28, 3/28, 3/28, 3/28, 3/28, 3/28, 3/28, 3/28], 2),
    Encounter([harry, emanuel], 200, 100, [good_helmet, good_gloves, good_weapon1, good_weapon2, good_armor, good_legs, good_boots], [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7], 3),
    Encounter([darius], 250, 150, [good_helmet, good_gloves, good_weapon1, good_weapon2, good_armor, good_legs, good_boots], [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7], 3),
]