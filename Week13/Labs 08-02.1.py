'''Labs 08.02 - (1)Item Class'''
import json
class Item:
    def __init__(self, name : str, price : int, weight : float):
        self.name = name
        self.price = price
        self.weight = weight

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price/self.weight

def main():

    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
