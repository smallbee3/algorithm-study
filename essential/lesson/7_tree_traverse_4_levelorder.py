class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    global root

    new_node = Node('A')
    root = new_node

    new_node = Node('B')
    root.left = new_node

    new_node = Node('C')
    root.right = new_node

    new_node_1 = Node('D')
    new_node_2 = Node('E')
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node('F')
    new_node_2 = Node('G')
    node = root.right
    node.left = new_node_1
    node.right = new_node_2


# def levelorder_traverse(node):
#
#     if node == root:
#         print(node.data, end='-> ')
#
#     if node.left:
#         print(node.left.data, end='-> ')
#     if node.right:
#         print(node.right.data, end='-> ') if node.right.data != 'G' else print(node.right.data)
#
#     if node.left:
#         levelorder_traverse(node.left)
#     if node.right:
#         levelorder_traverse(node.right)


def levelorder_traverse(node):

    if node == root:
        print(node.data, end=' -> ')

    if node.left is None or node.right is None:
        return

    print(node.left.data, end=' -> ')
    print(node.right.data, end=' -> ' if node.right.data != 'G' else '')
    levelorder_traverse(node.left)
    levelorder_traverse(node.right)


if __name__ == '__main__':

    init_tree()
    node = root

    levelorder_traverse(node)
