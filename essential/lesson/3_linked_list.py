
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


def print_list():

    # global node_A

    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


# if __name__ == '__main__':
#     init_list()
#     print_list()


# p.33
# 3.2.1 연결 리스트의 삽입 알고리즘


def insert_list(str, obj):

    # global node_A
    node = node_A

    while node:
        print(node)
        if node.data == str:
            obj.next = node.next
            node.next = obj
            return
        node = node.next


if __name__ == '__main__':
    init_list()
    print_list()

    node_E = Node('E')
    insert_list('B', node_E)

    print_list()
