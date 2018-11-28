import random
import time

from helper import my_timer


# Book answer
# @my_timer
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot_idx = random.randint(0, len(arr)-1)
    pivot = arr[pivot_idx]

    # print(f'pivot_idx: {pivot_idx} pivot: {pivot}')

    left_team = []
    right_team = []

    for i in range(len(arr)):
        if i != pivot_idx:
            if arr[i] < pivot:
                left_team.append(arr[i])
            else:
                right_team.append(arr[i])
    # print(left_team)
    # print(right_team)

    return quick_sort(left_team) + [pivot] + quick_sort(right_team)


# 2018.11.28
# Quick sort doesn't work if it doesn't control pivot element well

def quick_sort2(arr):

    if len(arr) < 2:
        return arr

    # Big miss point
    # pivot = arr[random.randrange(len(arr))]
    pivot = random.randrange(len(arr))
    less_arr = []
    more_arr = []

    for i in range(len(arr)):
        if i == pivot:
            continue
        if arr[i] < arr[pivot]:
            less_arr.append(arr[i])
        elif arr[i] >= arr[pivot]:
            more_arr.append(arr[i])

    return quick_sort(less_arr) + [arr[pivot]] + quick_sort(more_arr)


if __name__ == '__main__':

    random_list =[]

    # input_str = input('정렬할 데이터의 수 : ')
    # input_num = int(input_str)
    input_num = 10

    for i in range(input_num):
        random_list.append(random.randint(1, input_num))

    print('<정렬 전>')
    print(random_list)

    # start_time = time.time()
    # sorted_list = quick_sort(random_list)
    # running_time = time.time() - start_time

    start_time = time.clock()
    sorted_list = quick_sort(random_list)
    running_time = time.clock() - start_time

    print('<정렬 후>')
    print(sorted_list)

    print(f'데이터의 크기 : {input_num}')
    # print(f'비교 횟수 : {running_time}')
    # print(f'교환 횟수 : {running_time}')
    print(f'실행 시간 : {running_time:.6f}')
