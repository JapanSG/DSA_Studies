'''Lab 04.01 - Create BSTNode'''
class BSTNode:
    def __init__(self, data : int = None):
        '''Constructor'''
        self.data = data
        self.left : BSTNode= None
        self.right : BSTNode= None

def main():
    data = int(input())
    my_node = BSTNode(data)
    print(my_node.data)
    print(my_node.left)
    print(my_node.right)

main()
