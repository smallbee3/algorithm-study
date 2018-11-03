import random


def quick_sort(arr):

    if len(arr) < 2:
        return arr
    # elif len(arr) == 2:
    #     arr.sort()
    #     return arr
    else:
        pivot = random.randrange(len(arr))
        a = []
        b = []
        for i in range(len(arr)):
            if arr[i] < arr[pivot]:
                a.append(arr[i])
            elif i == pivot:
                pass
            else:
                b.append(arr[i])

        return quick_sort(a) + [arr[pivot]] + quick_sort(b)


print(quick_sort([33, 10, 15, 7]))
print(quick_sort([3, 5, 2, 1, 4]))
