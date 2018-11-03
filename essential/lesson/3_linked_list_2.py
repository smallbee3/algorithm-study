# p.38
# 3.2.3 연결 리스트의 삭제 알고리즘


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init_list():

    global node_A

    node_A = Node('A')
    node_B = Node('B')
    node_D = Node('D')
    node_E = Node('E')

    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E


def print_list():

    # global node_A

    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


# def insert_list(obj):
#
#     # global node_A
#     node = node_A
#
#     while node:
#
#         if node.next is not None \
#                 and obj.data < node.next.data:
#             obj.next = node.next
#             node.next = obj
#             return
#         elif node.next is None:
#             node.next = obj
#             return
#         node = node.next


def insert_list(str_data):

    global node_A
    node = node_A

    obj = Node(str_data)

    while node:

        if node.next is not None \
                and obj.data < node.next.data:
            obj.next = node.next
            node.next = obj
            return
        elif node.next is None:
            node.next = obj
            return
        node = node.next


def delete_list(str_data):

    print(dir(delete_list))

    global node_A

    print()
    print(dir(delete_list))
    print(delete_list.__globals__)
    print(type(delete_list.__globals__))

    node = node_A

    # 첫번 째 node를 삭제할 때
    if node.data == str_data:
        # temp_data = node.next.data
        # temp_node = node.next.next
        #
        # # B = A
        # node.next = node
        #
        # node.data = temp_data
        # node.next = temp_node
        # del node
        # 위 방법은 뭔가 이상하다. 그냥 억지로 답을 맞춘느낌.

        node_A = node.next
        del node
        return

    while node:

        # print(f'print: {node.next.data}')
        # print(f'print: {obj.data}')
        # print(f'print: {obj.next}')
        # print()

        # if node.next.data == obj.data:
        # 왜 위처럼 data 값은 비교할 수 있는데
        # 주소값 비교를 하면 안되는 것일까?
        # -> 아니다 상관없다. 아래서 Node('D')로 새로 객체를 생성하는 바람에 생긴 문제다.

        # [Upgrade 2]
        # if node.next == obj:
        #     node.next = obj.next
        #     del obj
        #     return
        if node.next.data == str_data:
            obj = node.next
            node.next = node.next.next
            del obj
            return

        node = node.next


if __name__ == '__main__':
    init_list()
    # print_list()

    # node_C = Node('C')
    # insert_list(node_C)
    insert_list('C')
    # print_list()

    insert_list('G')
    # print_list()

    insert_list('F')
    print_list()

    # node_D = Node('D')
    # 문제의 원인은 바로 위 코드에 있었음.
    # Node('D')로 새로 객체를 생성하는 바람에 생긴 문제.

    # 새로 생성하지 않고 객체를 전달하면 잘 된다.
    # delete_list(node_F)

    # [Upgrade 2]
    # obj가 아니라 책에서처럼 DATA를 전달하게 해보자.
    # 그러면 바로 위와 같은 문제도 사라지고, node_D도 쉽게 삭제 할 수 있다.
    delete_list('F')
    # delete_list('B')
    # delete_list('A')
    print_list()
