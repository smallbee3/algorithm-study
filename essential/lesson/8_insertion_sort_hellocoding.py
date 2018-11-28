import random

import time


# 새로운 list에 순서대로 넣으면서 정렬함.
# 방식은 insertion_sort이긴하지만 새로운 리스트에 넣는 것과
# 기존의 정렬하고자 하는 리스트에서 자리만 바꾸는 책의 답안과 비교할 때
# 아래 코드가 좀 더 이해하기 편하지만 성능 차이가 심하다!

# This is not insertion_sort as you might expect.
def insertion_sort(arr):

    sorted_list = []
    sorted_list.append(arr.pop(0))

    for i in range(len(arr)):
        for j in range(len(sorted_list)):

            # 원소가 하나만 있을 때
            # if i == 0 and j == 0:
            #     if arr[i] < sorted_list[j]:
            #         sorted_list.insert(j, arr[i])
            #     sorted_list.insert(j+1, arr[i])
            #     break
            # 아래 elif 문으로 위 case까지 커버
            print(arr[i], sorted_list[j])
            if arr[i] < sorted_list[j]:
                sorted_list.insert(j, arr[i])
                print(sorted_list)
                break
            elif j == len(sorted_list) - 1:
                sorted_list.insert(j+1, arr[i])
                print(sorted_list)
                break

    return sorted_list


# 2018.11.28
# The code above is sorting after insertion
# and the code below insert the minimum value, so there isn't sorting.

def find_the_min(arr):
    min_value = float('inf')
    min_idx = None
    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_idx = i
    return min_idx


def insertion_sort2(arr):

    sorted_arr = []
    arr_length = len(arr)
    for i in range(arr_length):
        min_idx = find_the_min(arr)
        sorted_arr.append(arr[min_idx])
        del arr[min_idx]
    arr = sorted_arr
    print(arr)


# 2018.11.28
# Example of why 'random_list' has not been changed.

def test_num(num):
    print(num)
    num = 3
    print(num)

j = 1
test_num(j)
print(j)


if __name__ == '__main__':

    random_list = []

    random_data_size = 100
    for i in range(random_data_size):
        result = random.randint(1, 100)
        random_list.append(result)

    # input_str = input('정렬할 데이터의 수 : ')
    # input_num = int(input_str)
    # for i in range(input_num):
    #     result = random.randint(1, input_num)
    #     random_list.append(result)

    print(random_list)

    start_time = time.time()
    sorted_list = insertion_sort(random_list)
    running_time = time.time() - start_time

    print(len(sorted_list))
    print(f'실행 시간 : {running_time}')
