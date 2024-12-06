'''Lab 01.06 - Rectangle'''
class Rectangle:
    '''Rectangle Class'''
    def __init__(self, height, width):
        '''Constructor'''
        self.height = height
        self.width = width

    def calculate_area(self):
        '''Calculate Area'''
        return self.height*self.width

    def calculate_perimeter(self):
        '''Calculate Perimeter'''
        return (self.height+self.width)*2
    
def main():
    '''Driver Code'''
    rec = Rectangle(float(input()), float(input()))
    func = input()
    if func == "area":
        print(f"{rec.calculate_area():.2f}")
    else:
        print(f"{rec.calculate_perimeter():.2f}")

if __name__ == "__main__":
    main()
