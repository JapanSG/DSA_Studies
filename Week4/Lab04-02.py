'''Lab 04.01 - Create BSTNode'''
class BSTNode:
    '''Binary search tree node class'''
    def __init__(self, data : int = None):
        '''Constructor'''
        self.data = data
        self.left : BSTNode= None
        self.right : BSTNode= None

class BST:
    '''Binary search tree class'''
    def __init__(self):
        '''Constructor'''
        self.root : BSTNode = None

    def insert(self, data):
        '''Insert node with data at the correct position'''
        if not self.root:
            self.root = BSTNode(data)
            return
        def recursion(pointer: BSTNode):
            '''recursion'''
            if data < pointer.data :
                if not pointer.left:
                    pointer.left = BSTNode(data)
                    return
                pointer = pointer.left
            else:
                if not pointer.right:
                    pointer.right = BSTNode(data)
                    return
                pointer = pointer.right
            recursion(pointer)
        recursion(self.root)

    def preorder(self):
        '''Print node in preorder traversal'''
        BST.preorder_re(self.root)
        print()

    def preorder_re(pointer : BSTNode):
        if not pointer:
            return
        print("-> " + str(pointer.data), end = " ")
        BST.preorder_re(pointer.left)
        BST.preorder_re(pointer.right)

    
def main():
    '''Driver Code'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
        
    print("Preorder: ", end="")
    my_bst.preorder()
main()
