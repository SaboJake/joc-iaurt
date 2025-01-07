

class Item:
    def __init__(self, name, description, slot, stats, price, sell_price):
        self.description = description
        self.slot = slot
        self.name = name
        self.price = price
        self.sell_price = sell_price
        self.stats = stats
