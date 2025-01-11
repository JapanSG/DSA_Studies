'''binary_search_tree'''
from binary_tree import BinaryTree, Node
class BST(BinaryTree):
    '''BST class'''
    def insert(self, val):
        '''insert'''

        def insert_re(node : Node):
            '''recursion'''
            if val < node.val:
                if not node.left:
                    node.left = Node(val)
                    return
                insert_re(node.left)
            else:
                if not node.right:
                    node.right = Node(val)
                    return
                insert_re(node.right)

        if not self.root:
            self.root = Node(val)
            return
        insert_re(self.root)

    def find_min(node : Node):
        '''return the least value node in the subtree'''
        pointer = node
        while pointer.left:
            pointer = pointer.left
        return pointer.val
    
    def find_max(node : Node):
        '''return the most value node in the subtree'''
        pointer = node
        while pointer.right:
            pointer = pointer.right
        return pointer.val
def main():
    '''Driver Code'''
    print("start")
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(15)
    bst.insert(5)
    bst.insert(7)
    bst.insert(50)
    print(f"Preorder : {bst.preorder()}")
    print(f"Inorder : {bst.inorder()}")
    print(f"Height : {bst.max_height()}")

if __name__ == "__main__":
    main()
