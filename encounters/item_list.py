from items.display_item import DisplayItem
from items.item import Item
from utils.stats import Stats

sample_stats1 = Stats(10, 10, 10, 10, 10)
sample_stats2 = Stats(20, 20, 20, 20, 20)

tricou = DisplayItem(Item("Tricou", "Tricou", "armor", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")

helmet = DisplayItem(Item("Helmet", "Helmet", "helmet", sample_stats1, 0, 0), "sprites/items/metal_mask.png")
good_helmet = DisplayItem(Item("Good Helmet", "Good Helmet", "helmet", sample_stats2, 0, 0), "sprites/items/golden_mask.png")

gloves = DisplayItem(Item("Gloves", "Gloves", "gloves", sample_stats1, 0, 0), "sprites/items/gloves.png")
good_gloves = DisplayItem(Item("Good Gloves", "Good Gloves", "gloves", sample_stats2, 0, 0), "sprites/items/golden_gloves.png")

weapon1 = DisplayItem(Item("Weapon1", "Weapon1", "weapon1", sample_stats1, 0, 0), "sprites/items/curved_blade.png")
good_weapon1 = DisplayItem(Item("Good Weapon1", "Good Weapon1", "weapon1", sample_stats2, 0, 0), "sprites/items/straight_blade.png")

weapon2 = DisplayItem(Item("Weapon2", "Weapon2", "weapon2", sample_stats1, 0, 0), "sprites/items/broken_pipe.png")
good_weapon2 = DisplayItem(Item("Good Weapon2", "Good Weapon2", "weapon2", sample_stats2, 0, 0), "sprites/items/golden_pipe.png")

armor = DisplayItem(Item("Armor", "Armor", "armor", sample_stats1, 0, 0), "sprites/items/tricou_gucci.png")
good_armor = DisplayItem(Item("Good Armor", "Good Armor", "armor", sample_stats2, 0, 0), "sprites/items/tricou_gucci.png")

legs = DisplayItem(Item("Legs", "Legs", "legs", sample_stats1, 0, 0), "sprites/items/bleu_jeans.png")
good_legs = DisplayItem(Item("Good Legs", "Good Legs", "legs", sample_stats2, 0, 0), "sprites/items/bleu_jeans_with_drip.png")

boots = DisplayItem(Item("Boots", "Boots", "boots", sample_stats1, 0, 0), "sprites/items/adibos.png")
good_boots = DisplayItem(Item("Good Boots", "Good Boots", "boots", sample_stats2, 0, 0), "sprites/items/adibos2.png")


