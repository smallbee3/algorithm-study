# factorial 구현
def factorial(num):
    if num == 1:
        return 1
    # if num > 1:
    else:
        return num * factorial(num-1)


print(factorial(5))


# Array 안의 원소 값 모두 더하기 through Recursion
# (p.95 PRACTICE 4-1 sum 함수)

# (1) 최 뒷단의 원소 제거
def fact_array(array):

    if array != []:
        num = len(array)
        result = array[num-1]
        del array[num-1]
        # print(array)
        return result + fact_array(array)
    else:
        return 0


print(fact_array([1, 2, 3, 4, -1, 100]))


# (2) 최 앞단의 원소 제거
def fact_array2(array):

    if array != []:
        result = array[0]
        del array[0]
        # print(array)
        return result + fact_array2(array)
    else:
        return 0


print(fact_array2([1, 2, 3, 4, -1, 100]))


# (3) 한 단계씩 이동하면서
def fact_array3(array, index):
    if index != len(array):
        result = array[index]
        # print(result)
        index += 1
        return result + fact_array3(array, index)
    else:
        return 0


print(fact_array3([1, 2, 3, 4, -1, 100], 0))


# (4) 한 단계씩 이동하면서 (함수호출 인자에서 최초 index인 0 제거)
def fact_array4(array, index=0):
    if index != len(array):
        result = array[index]
        print(result)
        index += 1
        return result + fact_array4(array, index)
    else:
        return 0


print(fact_array4([1, 2, 3, 4, -1, 100]))


# 181125
# Sum of array just like an answer of the book
def sum_arr(arr):

    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_arr(arr[1:])


print(sum_arr([1,2,3,3, -1]))


# 181125
# factorial for both positive and negative number
def factorial(num):
    if num > 0:
        if num == 1:
            return num
        else:
            return num * factorial(num - 1)
    else:
        if num == -1:
            return num
        else:
            return num * factorial(num+1) if num < 0 else factorial(-(num-1))


print(factorial(-4))
