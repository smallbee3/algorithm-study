from collections import deque
import queue

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# 181126 Simple answer

def breadth_first_algorithm(name):

    q = deque()
    # q.extend(graph['you'])
    q += graph[name]
    searched_list = []

    while q:
        person = q.popleft()
        if person == 'jonny':
            return f'"{person}" is mango seller!'
        searched_list.append(person)

        print(person)
        print(graph[person])
        print(q)
        print(searched_list)

        # q.extend(graph[person])
        for i in graph[person]:
            if i not in q and i not in searched_list:
                q.append(i)
                print(i)
                # searched_list.append(i)  -> no need
        print()

    print('There is no mango seller!')


print(breadth_first_algorithm('you'))

# Key point of Breadth first search

# 1. Using graph dict (append values which are connected nodes)
#
# 2. Eradicate duplicate element




# (1) q 중복 제거 전

# def func(q):
#     while q.queue:
#         print(q.queue)
#         person = q.get()
#
#         if person.endswith('y'):
#             return print(f'{person} is mango sales person.')
#         # for person in graph[person]:
#         #     q.put(person)
#         q.queue += graph[person]
#     return print("There is no mango sales person.")
#
#
# q = queue.Queue()
#
# for person in graph['you']:
#     q.put(person)
# func(q)


# (2) 망고 판매상 검사 중복 제거 + q 중복 원소 제거

# import queue
#
#
# def func(name):
#
#     searched = []
#
#     q = queue.Queue()
#     q.queue += graph[name]
#     # 이유는 모르나 위 문장이 PEP8 error 일으킴.
#     # 아래 코드는 PEP8 에러를 일으키지 않지만 정작 컴파일 시 TypeError: can only concatenate deque (not "list") to deque 발생
#
#     # q.queue = q.queue + graph[name]
#
#     print(q.queue)
#     print(type(q.queue))
#
#     # while q:
#     # -> q는 참이기 때문에 CLI 에서 확인하면 무한 loop를 도는 것으로 확인할 수 있음.
#     while q.queue:
#         print(q.queue)
#         print(searched)
#         person = q.get()
#
#         # (1) 무한 반복 예외 사항을 처리
#         if person not in searched:
#             if person.endswith('m'):
#                 return print(f'{person} is mango sales person.')
#
#         # searched += person
#         # -> ['a','l','i','c','e'] 가 들어가는 문제 발생.
#
#             else:
#                 for p in graph[person]:
#                     # if p not in searched:
#
#                     # (2) queue에 'peggy' 중복 들어가는 것 해결
#                     if p not in searched and p not in q.queue:
#                         q.put(p)
#                 searched.append(person)
#
#     return print("There is no mango sales person.")
#
#
# func('you')




# # Book answer (1)

def person_is_seller(name):
    return name[-1] == 'y'


# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     while search_queue:
#         person = search_queue.popleft()
#         if person_is_seller(person):
#             print(f'{person} is a mango seller!')
#             return True
#         else:
#             search_queue += graph[person]
#     return False
#
#
# search('you')


# # Book answer (2) - Redundancy eradicated

# def search2(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         print(searched)
#         print(search_queue)
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(f'{person} is a mango seller!')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# search2("you")


# # Book answer (2) - Redundancy eradicated + search path

def search3(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        print(searched)
        print(search_queue)
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                # search_queue += graph[person]
                for p in graph[person]:
                    if p not in search_queue:
                        search_queue.append(p)
                searched.append(person)
    return False


search3("you")
