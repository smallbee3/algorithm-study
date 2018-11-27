
# 8-1
# -> 집합 커버링 문제, set_covering problem

# box size
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7

# test binary search working in a different situation
a = 6
b = 3
c = 7
d = 2
e = 5
f = 1
g = 3


# truck size
truck_size = 20


# def min_box(list):
#
#     if len(list) == 0:
#         return
#     elif len(list) == 1:
#         return list[0]
#     else:
#         # if list[0] < list[1]:
#         #     min = list[0]
#         # else:
#         #     min = list[1]
#         min = list[0] if list[0] < list[1] else list[1]
#
#         sub_min = None
#         if len(list) != 2:
#             sub_min = min_box(list[2:])
#         if sub_min != None and sub_min < min:
#             min = sub_min
#         return min
#
#
# def max_box(list):
#
#     if len(list) == 0:
#         return
#     elif len(list) == 1:
#         return list[0]
#     else:
#         # if list[0] < list[1]:
#         #     min = list[0]
#         # else:
#         #     min = list[1]
#         max = list[0] if list[0] > list[1] else list[1]
#
#         sub_max = None
#         if len(list) != 2:
#             sub_max = max_box(list[2:])
#         if sub_max != None and sub_max > max:
#             max = sub_max
#         return max
#
#
# def binary_search(list, item):
#
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None


def max_box(arr):

    max = 0
    index = None
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            index = i
    # return max, index
    return arr[index], index


def min_box(arr):

    min = float('inf')
    index = None
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    return arr[index]


def greedy():

    box_needed = [a, b, c, d, e, f, g]

    truck_occupied_space = 0
    truck_stuff = []

    while truck_size - truck_occupied_space > min_box(box_needed):
        # for box in box_needed:
            # if biggest_box < box:
            #     biggest_box = box
        print(box_needed)
        biggest_box, biggest_box_index = max_box(box_needed)
        # biggest_box_index = binary_search(box_needed, biggest_box)

        if biggest_box <= truck_size - truck_occupied_space:
            truck_occupied_space += biggest_box
            truck_stuff.append(biggest_box)
        del box_needed[biggest_box_index]

    return truck_stuff


print(greedy())


# 8-2

europe = {}
europe['a'] = [2, 60]
europe['b'] = [3, 40]
europe['c'] = [2, 50]
europe['d'] = [1, 10]
europe['e'] = [1, 10]
# 아래처럼 값이 주어지면 탐욕알고리즘의 한계를 보여준다. (만족이 더 낮아짐)
# europe['e'] = [1, 15]
europe['f'] = [1, 10]


# def greedy_travel():
#
#     traveling_days = 7
#     traveling_nation_list = []
#     not_traveling_nation_list = []
#
#     satisfiction = 0
#     days_sum = 0
#
#     # 총 합산 여행 일 수가 여행 가능 일 수와 같을 때 (넘는 것은 아래 코드에서 이미 제외됨)
#     # 또는 모든 여행가능 국가를 고려해서 더 이상 고려할 국가가 없을 때 while문 종료
#     while days_sum < traveling_days and\
#             len(traveling_nation_list + not_traveling_nation_list) != len(europe):
#
#         # 계산한 value가 가장 큰 best_nation 찾기
#         max_value = 0
#         best_nation = None
#         for nation in europe:
#             # 만족 / 여행 일수를 통해 얻은 value값으로 best_nation 판단
#             # (책 답안에서는 만족만으로 추측)
#             value = europe[nation][1] / europe[nation][0]
#             if nation not in (traveling_nation_list + not_traveling_nation_list) \
#                     and value > max_value:
#                 max_value = value
#                 best_nation = nation
#
#         # best_nation의 여행 일수가 남은 여행 일수보다 적으면 여행하고
#         if traveling_days - days_sum >= europe[best_nation][0]:
#             days_sum += europe[best_nation][0]
#             satisfiction += europe[best_nation][1]
#             traveling_nation_list.append(best_nation)
#         # 그렇지 않다면 현재 여행 일정 상 여행을 가지 못하는 국가 리스트에 추가한다.
#         else:
#             not_traveling_nation_list.append(best_nation)
#
#     print(f'여행 일수: {days_sum}')
#     print(f'여행 만족도: {satisfiction}')
#     print(f'여행 국가: {traveling_nation_list}')
#     print(f'여행 가려다가 고려했지만 일정상 못간 국가: {not_traveling_nation_list}')
#
#
# greedy_travel()


# 8-3
# No

# 8-4
# No -> Yes
# 탐욕 알고리즘의 여부는 근사 알고리즘(approximate algorithm)인지 아닌지 여부와
# 관계없이 문제를 해결해가는 알고리즘의 방법과 관계가 있다.

# 8-5
# No -> Yes

# 8-6
# NP-complete problem > 외판원문제, traveling salesperson problem

# 8-7
# NP-complete problem > 집합 커버링 문제, set_covering problem

# 8-8
# NP-complete problem > 외판원문제, traveling salesperson problem
