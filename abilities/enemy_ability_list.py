from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal

coeffs1 = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

attack1 = BasicAttack(coeffs1, "WHO", "CARES", 0, 0, "physical", 'sprites/abilities/slash.png')
heal1 = BasicHeal(coeffs1, "heal", "WHO CARES", 0, 0, "physical", 'sprites/abilities/heal.png')