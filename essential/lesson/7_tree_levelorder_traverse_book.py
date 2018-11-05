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


def levelorder_traverse(node):

    levelq = []
    levelq.append(node)

    while levelq:
        node = levelq.pop(0)
        print(node.data, end='-> ') if node.data != 'G' else print(node.data)

        if node.left:
            levelq.append(node.left)
        if node.right:
            levelq.append(node.right)


if __name__ == '__main__':

    init_tree()
    node = root

    levelorder_traverse(node)
