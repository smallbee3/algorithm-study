import random
import time


# 1) 책 답안
# def selection_sort(my_list):
#
#     my_list.insert(0, -1)
#     for i in range(2, len(my_list)):
#         temp = my_list[i]
#         i2 = i
#
#         while my_list[i2 - 1] > temp:
#             my_list[i2] = my_list[i2 - 1]
#             i2 = i2 - 1
#         my_list[i2] = temp
#     del my_list[0]


# 2) my_list.insert(0, -1)을 제거하여 좀 더 간결해진 코드
from helper import my_timer


# This sort is normally faster than selection sort
@my_timer
def insertion_sort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        # i2 = i

        while arr[i - 1] > temp:
            arr[i] = arr[i - 1]
            i -= 1

            # arr.insert(0, -1) 없어도 작동하도록 설계
            if i == 0:
                # arr[0]에 위치한 element보다도 작으면
                # 그 밑으로 내려갈 필요 없이(arr[-1])
                # 그냥 break 때린다.
                break
        arr[i] = temp


if __name__ == '__main__':

    random_list = []

    # input_str = input('정렬할 데이터의 수 : ')
    # input_num = int(input_str)
    input_num = 100

    for i in range(input_num):
        random_list.append(random.randint(1, input_num))
    # random_list =[4,3,1,2,6]

    print('<정렬 전>')
    print(random_list)

    start_time = time.time()
    insertion_sort(random_list)
    running_time = time.time() - start_time

    print('<정렬 후>')
    print(random_list)

    print(f'데이터의 크기 : {input_num}')
    # print(f'비교 횟수 : {running_time}')
    # print(f'교환 횟수 : {running_time}')
    print(f'실행 시간 : {running_time}')
