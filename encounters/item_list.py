from items.display_item import DisplayItem
from items.item import Item
from utils.stats import Stats

sample_stats1 = Stats(10, 10, 10, 10, 10)
sample_stats2 = Stats(20, 20, 20, 20, 20)

tricou = DisplayItem(Item("Tricou", "Tricou funny", "armor", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")

helmet = DisplayItem(Item("Helmet", "Helmet funny", "helmet", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_helmet = DisplayItem(Item("Good Helmet", "Good Helmet funny", "helmet", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

gloves = DisplayItem(Item("Gloves", "Gloves funny", "gloves", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_gloves = DisplayItem(Item("Good Gloves", "Good Gloves funny", "gloves", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

weapon1 = DisplayItem(Item("Weapon1", "Weapon1 funny", "weapon1", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_weapon1 = DisplayItem(Item("Good Weapon1", "Good Weapon1 funny", "weapon1", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

weapon2 = DisplayItem(Item("Weapon2", "Weapon2 funny", "weapon2", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_weapon2 = DisplayItem(Item("Good Weapon2", "Good Weapon2 funny", "weapon2", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

armor = DisplayItem(Item("Armor", "Armor funny", "armor", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_armor = DisplayItem(Item("Good Armor", "Good Armor funny", "armor", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

legs = DisplayItem(Item("Legs", "Legs funny", "legs", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_legs = DisplayItem(Item("Good Legs", "Good Legs funny", "legs", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

boots = DisplayItem(Item("Boots", "Boots funny", "boots", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_boots = DisplayItem(Item("Good Boots", "Good Boots funny", "boots", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")


