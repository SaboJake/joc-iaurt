from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal
from units.friendly_unit import FriendlyUnit
from units.player_unit import PlayerUnit
from utils.stats import Stats

friendly_units = {}
money = 100

player_unit = PlayerUnit("Darius", "Warrior", Stats(10, 10, 10, 35, 10, 10, 10, 10), Stats(10, 10, 10, 35, 10, 10, 10, 10))

def get_money():
    return money

def add_money(new_money):
    global money
    money += new_money
    print(money)

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

ally_stats = Stats(5, 5, 5, 5, 5)
ally1 = FriendlyUnit("Ally1", "Combat Medic", ally_stats, ally_stats)
ally1.abilities.append(BasicAttack(coeffs, "attack", "WHO CARES", 0, 0, "physical", 'sprites/abilities/slash.png'))
ally1.abilities.append(BasicHeal(coeffs, "heal", "WHO CARES", 0, 0, "physical", 'sprites/abilities/heal.png'))


def set_money(new_money):
    global money
    money = new_money

save_data = {}

def get_save_data():
    return save_data

def set_save_data(new_save_data):
    global save_data
    save_data = new_save_data