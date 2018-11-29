import random
import time

from helper import my_timer


# Book answer
# @my_timer
# def bubble_sort(my_list):
#     for i in range(len(my_list)-1):
#         for j in range(1, len(my_list)-i):
#             if my_list[j-1] > my_list[j]:
#                 # temp = my_list[j-1]
#                 # my_list[j-1] = my_list[j]
#                 # my_list[j] = temp
#                 # print(my_list)
#
#                 # swap values through tuple
#                 my_list[j-1], my_list[j] = my_list[j], my_list[j-1]

# Myway
# @my_timer
# def bubble_sort(my_list):
#     for i in range(len(my_list)-1):
#         for j in range(len(my_list)-1-i):
#             if my_list[j] > my_list[j+1]:
#                 temp = my_list[j+1]
#                 my_list[j+1] = my_list[j]
#                 my_list[j] = temp
#                 print(my_list)


# 2018.11.28
# '-1' is still a key point of this algorithm

def bubble_sort(arr):

    for num in range(len(arr)-1):
        for i in range(len(arr) - num - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


if __name__ == '__main__':

    random_list = []

    # input_str = input('정렬할 데이터의 수 : ')
    # input_num = int(input_str)
    input_num = 30

    for i in range(input_num):
        random_list.append(random.randint(1, input_num))

    print('<정렬 전>')
    print(random_list)

    start_time = time.time()
    bubble_sort(random_list)
    running_time = time.time() - start_time

    print('<정렬 후>')
    print(random_list)

    print(f'데이터의 크기 : {input_num}')
    # print(f'비교 횟수 : {running_time}')
    # print(f'교환 횟수 : {running_time}')
    print(f'실행 시간 : {running_time}')
