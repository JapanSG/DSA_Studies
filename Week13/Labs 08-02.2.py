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

def knapsack(item_list : list, amount : float):
    amount_left = amount
    sack = []
    priority = sorted(item_list, key = lambda item : (item.get_cost()),reverse = True)
    index = 0
    while amount_left > 0 and index < len(priority) and priority[index].get_weight() <= amount_left:
        sack.append(priority[index])
        amount_left -= priority[index].get_weight()
        index += 1

    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    total = 0
    for item in sack:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
        total += item.get_price()
    print(f"Total: {total} THB")
    return sack

def main():
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
