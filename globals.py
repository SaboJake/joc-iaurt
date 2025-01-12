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

def set_money(new_money):
    global money
    money = new_money

save_data = {}

def get_save_data():
    return save_data

def set_save_data(new_save_data):
    global save_data
    save_data = new_save_data