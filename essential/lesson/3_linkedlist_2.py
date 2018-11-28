
# p.29
# 3.1.1 노드(Node)와 링크(Link)
# 파이썬에서 연결 리스틀를 사용하기 위해서는 노드(Ndde)를
# 다음과 같이 클래스로 정의하여 사용


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Wrong Answer
# d = Node('D')
# c = Node('C', next=d)
# b = Node('B', next=c)
# a = Node('A', next=b)


# p.31
# 3.2.1 연결 리스트의 초기화
def init_list():

    global node_A

    node_A = Node('A')
    node_B = Node('B')
    node_C = Node('C')
    node_D = Node('D')

    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D


# def print_list():
#
#     # global node_A
#
#     node = node_A
#     while node:
#         print(node.data)
#         node = node.next
#     print()


# if __name__ == '__main__':
#     init_list()
#     print_list()


# p.33
# 3.2.1 연결 리스트의 삽입 알고리즘
# def insert_list(str, obj):
#
#     # global node_A
#     node = node_A
#
#     while node:
#         print(node)
#         if node.data == str:
#             obj.next = node.next
#             node.next = obj
#             return
#         node = node.next
#
#
# if __name__ == '__main__':
#     init_list()
#     print_list()
#
#     node_E = Node('E')
#     insert_list('B', node_E)
#
#     print_list()


# 181127
# Try again and made a better code

def print_list():
    global node_A

    node = node_A
    while node:
        print(node.data, end=' -> ' if node.next is not None else '')
        node = node.next
    print()


# p.35
# Book answer cannot pass the case of inserting node in the first place
# and not existing node.

# def insert_list(data):
#     global node_A
#     new_node = Node(data)
#     node_P = node_A
#     node_T = node_A
#     while node_T.data <= data:
#         node_P = node_T
#         node_T = node_T.next
#     new_node.next = node_T
#     node_P.next = new_node


def insert_list(data):
    global node_A

    new_node = Node(data)
    node = node_A

    # first
    if new_node.data < node.data:
        new_node.next = node
        node_A = new_node
        return

    while node:

        # middle
        if node.data <= new_node.data < node.next.data:
            new_node.next = node.next
            node.next = new_node
            break

        # end
        if node.next.next is None:

            # redundant code

            # if new_node.data < node.next.data:
            #     new_node.next = node.next
            #     node.next = new_node
            #     break
            # else:
            node.next.next = new_node
            break

        node = node.next


def delete_list(data):

    global node_A
    node = node_A

    # first
    if node.data == data:
        node_A = node.next
        del node
        return

    while node:

        next_node = node.next

        # middle
        if next_node.data == data:
            node.next = next_node.next
            del next_node
            break

        # when data does not exist in the list
        if next_node.next is None:
            print('The node you input does not exist!')
            break
        node = node.next


if __name__ == '__main__':

    # initialize
    init_list()
    print_list()

    # insert node
    insert_list('1')
    print_list()

    insert_list('AB')
    print_list()

    insert_list('CD')
    print_list()

    insert_list('E')
    print_list()

    insert_list('DE')
    print_list()

    insert_list('E')
    print_list()

    # delete node
    delete_list('C')
    print_list()

    delete_list('E')
    print_list()

    delete_list('E')
    print_list()

    delete_list('E')
    print_list()

    delete_list('1')
    print_list()

    delete_list('A')
    print_list()
