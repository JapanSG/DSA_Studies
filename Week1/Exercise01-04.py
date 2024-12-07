'''Exercise 01.04 - Laew Tae App V.2'''
import random
class LaewTaeApp:
    '''LaewTaeApp class'''
    def __init__(self, *foods : str) -> None:
        '''Constructor'''
        self.count = 0
        self.foods = sorted(foods)

    def random_food(self) -> str:
        '''Return a random food on foods list'''
        self.count += 1
        return random.choice(self.foods)

    def list_foods(self) -> None:
        '''Print all food in foods list'''
        print(self.foods)

    def add_food_item(self, food : str) -> None:
        '''Insert a food item while keeping foods list sorted'''
        length = len(self.foods)
        i = 0
        while i < length :
            if self.foods[i] > food:
                self.foods.insert(i, food)
                return
            i += 1
        self.foods.append(food)

def main():
    '''Driver Code'''
    app = LaewTaeApp('Pizza', 'Fried Chicken', 'Hamburger', 'Steak')
    num_food = int(input())
    for _ in range(num_food):
        app.add_food_item(input())
    app.list_foods()

if __name__ == "__main__":
    main()
