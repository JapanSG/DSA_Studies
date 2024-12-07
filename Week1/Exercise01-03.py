'''Exercise 01.03 - Laew Tae App V.1'''
import random
class LaewTaeApp:
    '''LaewTaeApp class'''
    def __init__(self, *foods : str) -> None:
        '''Constructor'''
        self.count = 0
        self.foods = foods

    def random_food(self) -> str:
        '''Return a random food on foods list'''
        self.count += 1
        return random.choice(self.foods)

    def list_foods(self) -> None:
        '''Print all food in foods list'''
        print(sorted(self.foods))

def main():
    '''Driver Code'''
    app = LaewTaeApp('Pizza', 'Fried Chicken', 'Hamburger', 'Steak')
    app.list_foods()

if __name__ == "__main__":
    main()
