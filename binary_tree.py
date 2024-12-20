'''binary_tree'''
class Node:
    '''Node Class'''
    def __init__(self, val):
        '''Constructor'''
        self.val = val
        self.left : Node = None
        self.right : Node = None

class BinaryTree:
    '''BinaryTree Class'''
    def __init__(self):
        '''Constructor'''
        self.root : Node = None

    def inorder(self):
        '''Start recursion'''
        values = []
        def recursion(pointer : Node):
            '''inorder traversal'''
            if not pointer:
                return
            recursion(pointer.left)
            values.append(pointer.val)
            recursion(pointer.right)

        recursion(self.root)
        return values

    def preorder(self):
        '''Start recursion'''
        values = []
        def recursion(pointer : Node):
            '''preorder traversal'''
            if not pointer:
                return
            values.append(pointer.val)
            recursion(pointer.left)
            recursion(pointer.right)

        recursion(self.root)
        return values

    def postorder(self):
        '''Start recursion'''
        values = []
        def recursion(pointer : Node):
            '''postorder traversal'''
            if not pointer:
                return
            recursion(pointer.left)
            recursion(pointer.right)
            values.append(pointer.val)

        recursion(self.root)
        return values

    def level_order(self):
        '''Start'''
        values = []
        def recursion(*roots : Node):
            '''Level order traversal'''
            level = []
            new_root = []
            for root in roots:
                root : Node = root
                if root.left:
                    level.append(root.left.val)
                    new_root.append(root.left)
                if root.right:
                    level.append(root.right.val)
                    new_root.append(root.right)
            if not new_root:
                return
            values.append(level)
            recursion(*new_root)

        values.append(self.root.val)
        recursion(self.root)
        return values

    def max_height(self) -> int:
        '''Return the max height of the tree'''
        def recursion(pointer = self.root) -> int:
            '''Recursion'''
            if not pointer:
                return 0
            left_height = recursion(pointer.left)+ 1
            right_height = recursion(pointer.right)+ 1
            return max(left_height, right_height)
        return recursion()

    def insert(self, val) -> int:
        '''Insert by level order'''
        def recursion(*parents):
            '''recursion'''
            children = []
            for parent in parents:
                parent : Node = parent
                if not parent.left:
                    parent.left = Node(val)
                    return
                children.append(parent.left)
                if not parent.right:
                    parent.right = Node(val)
                    return
                children.append(parent.right)
            recursion(*children)
        recursion(self.root)

def main():
    '''Driver Code'''
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(6)
    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())
    print(tree.level_order())
    print(tree.max_height())
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    print(tree.level_order())
if __name__ == "__main__":
    main()
