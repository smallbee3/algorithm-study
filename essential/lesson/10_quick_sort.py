import random
import time

from helper import my_timer


# Book answer
# @my_timer
def quick_sort(my_list):

    if len(my_list) <= 1:
        return my_list

    pivot_idx = random.randint(0, len(my_list)-1)
    pivot = my_list[pivot_idx]

    print(f'pivot_idx: {pivot_idx} pivot: {pivot}')

    left_team = []
    right_team = []

    for i in range(len(my_list)):
        if i != pivot_idx:
            if my_list[i] < pivot:
                left_team.append(my_list[i])
            else:
                right_team.append(my_list[i])
    print(left_team)
    print(right_team)

    # left = quick_sort(left_team)
    # right = quick_sort(right_team)
    #
    # sorted_list = left + [pivot] + right
    # return sorted_list

    # 위 4줄 -> 1줄
    return quick_sort(left_team) + [pivot] + quick_sort(right_team)


if __name__ == '__main__':

    random_list =[]

    # input_str = input('정렬할 데이터의 수 : ')
    # input_num = int(input_str)
    input_num = 10

    for i in range(input_num):
        random_list.append(random.randint(1, input_num))

    print('<정렬 전>')
    print(random_list)

    start_time = time.time()
    sorted_list = quick_sort(random_list)
    running_time = time.time() - start_time

    print('<정렬 후>')
    print(sorted_list)

    print(f'데이터의 크기 : {input_num}')
    # print(f'비교 횟수 : {running_time}')
    # print(f'교환 횟수 : {running_time}')
    print(f'실행 시간 : {running_time}')
