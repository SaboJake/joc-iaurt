from abilities.ability_list import FocusAttack, ApplyWoundAbility, ApplyWeakenAbility, ApplyStunAbility, \
    ApplyRegenAbility, ApplyBuffAbility, WoundAttack, WeakenAttack, StunAttack, RegenHeal, BuffHeal
from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal
from effects.effect_list import Wound, Weaken, Stun, Regen, Buff
from units.unit import Unit
from utils.stats import Stats

coeffs1 = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

attack1 = BasicAttack(coeffs1, "WHO", "CARES", 0, 0, "physical", 'sprites/abilities/slash.png')
heal1 = BasicHeal(coeffs1, "heal", "WHO CARES", 0, 0, "physical", 'sprites/abilities/heal.png')

focus_attack = FocusAttack(coeffs1, "Focus Attack", "Gain focus when attacking", 0, 0, "physical", 'sprites/abilities/quick_strike.png')

sample = Unit("Garius", Stats(10, 10, 10, 30, 10), Stats(10, 10, 10, 30, 10))

effect_coeffs = {
    'strength': 0.3,
}

wound_effect = Wound("Wound", "Deal damage over time", 3, "physical", True, effect_coeffs, sample)
weaken_effect = Weaken("Weaken", "Reduce stats", 3, "physical", True, effect_coeffs, sample)
stun_effect = Stun("Stun", "Stun the target", 2, "physical", True)
regen_effect = Regen("Regen", "Regenerate health", 3, "physical", True, effect_coeffs, sample)
buff_effect = Buff("Buff", "Buff stats", 3, "physical", True, effect_coeffs, sample)

apply_wound = ApplyWoundAbility(wound_effect, "Wound", "Applies wound effect", 0, 2, "physical", 'sprites/abilities/wound.png')
apply_weaken = ApplyWeakenAbility(weaken_effect, "Weaken", "Applies weaken effect", 0, 2, "physical", 'sprites/abilities/weaken.png')
apply_stun = ApplyStunAbility(stun_effect, "Stun", "Applies stun effect", 0, 3, "physical", 'sprites/abilities/break.png')
apply_regen = ApplyRegenAbility(regen_effect, "Regen", "Applies regen effect", 0, 2, "physical", 'sprites/abilities/regen.png')
apply_buff = ApplyBuffAbility(buff_effect, "Buff", "Applies buff effect", 0, 2, "physical", 'sprites/abilities/buff.png')

wound_attack = WoundAttack(coeffs1, wound_effect, "Wound Attack", "Deal damage and apply wound effect", 0, 0, "physical", 'sprites/abilities/slash.png')
weaken_attack = WeakenAttack(coeffs1, weaken_effect, "Weaken Attack", "Deal damage and apply weaken effect", 0, 0, "physical", 'sprites/abilities/slash.png')
stun_attack = StunAttack(coeffs1, stun_effect, "Stun Attack", "Deal damage and apply stun effect", 0, 0, "physical", 'sprites/abilities/slash.png')

regen_heal = RegenHeal(coeffs1, regen_effect, "Regen Heal", "Heal and apply regen effect", 0, 0, "physical", 'sprites/abilities/heal.png')
buff_heal = BuffHeal(coeffs1, buff_effect, "Buff Heal", "Heal and apply buff effect", 0, 0, "physical", 'sprites/abilities/heal.png')

