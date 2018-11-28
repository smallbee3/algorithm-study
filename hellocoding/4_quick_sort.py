import random

import time


# comment (2018.11.28)
# The first quick sort has a problem of not sorting the duplicate elements.

def quick_sort(arr):

    # if arr == []:
    #     return []
    # elif len(arr) == 1:
    #     return arr
    if len(arr) < 2:
        return arr

    pivot = arr[random.randrange(len(arr))]
    arr_left = []
    arr_right = []

    for i in arr:
        if i == pivot:
            pass
        elif i > pivot:
            arr_right.append(i)
        elif i < pivot:
            arr_left.append(i)
    # print(arr_left)
    # print(arr_right)

    return quick_sort(arr_left) + [pivot] + quick_sort(arr_right)


t1 = time.time()
print(quick_sort([33, 10, 15, 7, 3, 53, 13, 5, 12, 76, 1, 6, 8, 66, 83, 24, 13]))
# print(quick_sort([3, 5, 2, 1, 4]))
# time.sleep(1)
t2 = time.time() - t1
print(t2)


def quick_sort(arr):

    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        arr.sort()
        return arr

    pivot = random.randrange(len(arr))
    a = []
    b = []
    for i in range(len(arr)):
        if i == pivot:
            pass
        elif arr[i] < arr[pivot]:
            a.append(arr[i])
        else:
            b.append(arr[i])

    return quick_sort(a) + [arr[pivot]] + quick_sort(b)


t1 = time.time()
print(quick_sort([33, 10, 15, 7, 3, 53, 13, 5, 12, 76, 1, 6, 8, 66, 83, 24, 13]))
# time.sleep(1)
t2 = time.time() - t1
print(t2)

# print(quick_sort([3, 5, 2, 1, 4]))
