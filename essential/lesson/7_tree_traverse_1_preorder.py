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

    # new_node_1 = Node('D')
    # new_node_2 = Node('E')
    # node = root.left
    # node.left = new_node_1
    # node.right = new_node_2
    #
    # new_node_1 = Node('F')
    # new_node_2 = Node('G')
    # node = root.right
    # node.left = new_node_1
    # node.right = new_node_2

    # 2018.11.28
    # Expand tree

    new_node_1 = Node('D')
    new_node_2 = Node('E')
    node1 = root.left
    node1.left = new_node_1
    node1.right = new_node_2

    new_node_1 = Node('F')
    new_node_2 = Node('G')
    node2 = root.right
    node2.left = new_node_1
    node2.right = new_node_2

    # 'H', 'I'
    new_node_1 = Node('H')
    new_node_2 = Node('I')
    node3 = node1.left
    node3.left = new_node_1
    node3.right = new_node_2

    # 'J', 'K'
    new_node_1 = Node('J')
    new_node_2 = Node('K')
    node4 = node1.right
    node4.left = new_node_1
    node4.right = new_node_2


# My first code was not bad
# in that it can work without any return statement.

# def preorder_traverse(node):
#     print(node.data, end='-> ') if node.data != 'G' else print(node.data)
#
#     if node.left:
#         preorder_traverse(node.left)
#
#     if node.right:
#         preorder_traverse(node.right)


def preorder_traverse(node):

    if node is None:
        return

    # print(node.data, end='-> ') if node.data != 'G' else print(node.data)

    # 2018.11.28
    # refactored
    print(node.data, end='' if node.data == 'G' else ' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# 2018.11.28
# Without recursion
def preorder_traverse_without_recursion(node):

    while True:
        pass
        # Is it really possible to traverse tree without recurson?
        # At the moment, it seems there is no way.
        # Because the scope of while loop cannot remember the node in the previous loop.
        # And this is related to two recursions in the above code, I guess.


if __name__ == '__main__':

    init_tree()
    node = root

    preorder_traverse(node)
    # preorder_traverse_without_recursion(node)
