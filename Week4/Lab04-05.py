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
        '''preorder recursive'''
        if not pointer:
            return
        print("-> " + str(pointer.data), end = " ")
        BST.preorder_re(pointer.left)
        BST.preorder_re(pointer.right)

    def is_empty(self) -> bool:
        '''Return true if empty else return false'''
        return not bool(self.root)
    
    def inorder(self):
        '''print node in inorder traversal'''
        BST.inorder_re(self.root)
        print()

    def inorder_re(pointer : BSTNode):
        '''inorder recursive'''
        if not pointer:
            return
        BST.inorder_re(pointer.left)
        print("-> " + str(pointer.data), end = " ")
        BST.inorder_re(pointer.right)

    def postorder(self):
        '''print node in postorder traversal'''
        BST.postorder_re(self.root)
        print()
    
    def postorder_re(pointer : BSTNode):
        if not pointer:
            return
        BST.postorder_re(pointer.left)
        BST.postorder_re(pointer.right)
        print("-> " + str(pointer.data), end = " ")

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return

        print("Preorder: ", end = "")
        self.preorder()
        print("Inorder: ", end = "")
        self.inorder()
        print("Postorder: ", end = "")
        self.postorder()

    def find_min(self):
        "find min value"
        pointer = self.root
        while pointer.left:
            pointer = pointer.left
        return pointer.data
    
    def find_max(self):
        '''find max value'''
        pointer = self.root
        while pointer.right:
            pointer = pointer.right
        return pointer.data

    def delete(self, data):
        '''delete data'''
        pointer = self.root
        if pointer.data == data:
            if pointer.right:
                self.root = pointer.right
            elif pointer.left:
                self.root = pointer.left
            else:
                self.root = None
            return
        while pointer:
            if pointer.right and pointer.right.data == data:
                parent = pointer
                pointer = pointer.right
                if pointer.left:
                    parent.right = pointer.left
                elif pointer.right:
                    parent.right = pointer.right
                else:
                    parent.right = None
                return data
            elif pointer.left and pointer.left.data == data:
                parent = pointer
                pointer = pointer.left
                if pointer.left:
                    parent.left = pointer.left
                elif pointer.right:
                    parent.left = pointer.right
                else:
                    parent.left = None
                return data
            else:
                if data < pointer.data:
                    pointer = pointer.left
                else:
                    pointer = pointer.right
        print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
        return None
def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()