'''Lab 03.01 - Create DataNode'''
class DataNode:
    '''DataNode class'''
    def __init__(self, data = None):
        '''Constructor'''
        self.data = data
        self.next = None

def main():
    '''Driver Code'''
    data = input()
    node = DataNode(data)
    print(node.data)
    print(node.next)
main()
