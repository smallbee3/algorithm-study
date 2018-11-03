# # 4-1 처음 나왔던 sum 함수를 작성해 보세요.
# -> 2_recursion.py 에서 풀이


# # 181027
# # 복습하다가 sum 함수에서부터 막힘
#
# def sum1(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
#
#
# # 처참하게 박살남.
# # def sum1(arr):
# #     if len(arr) > 0:
# #         sum_num = sum_num + arr[0]
# #     return sum_num + sum1(arr[1:])
#
#
# def sum2(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum1(arr[1:])
#
#
# print(sum1([1, 2, 3, 100]))
# print(sum2([1, 2, 3, 100]))


def sum(arr):
    if arr != []:
        return arr[0] + sum(arr[1:])
    else:
        return 0


print('4-1')
print(sum([1, 2, 3, 4]))


# # 4-2 리스트에 포함된 원소의 숫자를 세는 재귀 함수를 작성해 보세요.


from helper import my_timer


@my_timer
def count_num(arr):
    if arr == []:
        return 0
    else:
        del arr[0]
        return 1 + count_num(arr)


print('4-2')
print(count_num([1, 2, 3, 4, 5, 100]))


@my_timer
def count_num2(arr):
    return len(arr)


print('4-2(2)')
print(count_num2([1, 2, 3, 4, 5, 100]))


def count_num3(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_num(arr[1:])


print('4-2(3)')
print(count_num3([1, 2, 3, 4, 5, 100]))


# # 4-3 리스트에서 가장 큰 수를 찾아보세요.


def find_big_element(arr):
    max = arr[0]
    for i in range(len(arr)-1):
        if max < arr[i+1]:
            max = arr[i+1]

    return max


print('4-3')
print(find_big_element([3, 10, -33, 100000, 1, 100, 2, 3]))


# 재귀 활용
def find_big_element2(arr):
    if len(arr) == 0:
        pass
    elif len(arr) == 1:
        return arr[0]
    else:
        # max = arr[0]
        # if max < arr[1]:
        #     max = arr[1]
        max = arr[0] if arr[0] > arr[1] else arr[1]

        result = find_big_element2(arr[2:])
        # if result != None and max < result:
        #     max = result
        max = result if result is not None and max < result else max
        return max


# 바로 위 내가 푼 풀이를 책 답안 처럼 list가 0, 1개 일 때 제외하면 아래 처럼 깔끔
def find_big_element3(arr):
    # max = arr[0]
    # if max < arr[1]:
    #     max = arr[1]
    max = arr[0] if arr[0] > arr[1] else arr[1]

    result = find_big_element2(arr[2:])
    if max < result:
        max = result
    return max


# find_big_element2 에서 len(arr) == 2 일 때 오류 예외처리
def find_big_element4(arr):
    if len(arr) == 0:
        pass
    elif len(arr) == 1:
        return arr[0]
    else:
        # max = arr[0]
        # if max < arr[1]:
        #     max = arr[1]
        max = arr[0] if arr[0] > arr[1] else arr[1]

        result = None
        if len(arr) != 2:
            result = find_big_element2(arr[2:])
        if result != None and max < result:
            max = result
        return max


print('4-3(2)')
print(find_big_element2([11, 10, -33, 100, 1, 101, 2, 3]))
print(find_big_element3([11, 10, -33, 100, 1, 101, 2, 3]))
print(find_big_element4([321, 10, 122]))
print(find_big_element2([]))


# 책 답안
# def max(list):
#     if len(list) == 2:
#         return list[0] if list[0] > list[1] else list[1]
#     sub_max = max(list[1:])
#     return list[0] if list[0] > sub_max else sub_max


# 책 답안 수정 (list가 1개 일 때도 가능하도록, 0개 일 때는 []가 'sub_max = ...' 에 걸리지 않도록 return으로 함수를 종료시킨다.)
def max(list):
    if len(list) == 0:
        return
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print('4-3(3)')
print(max([7, 7777777, 366, 3, 11, 11111]))
print(max([1]))
print(max([]))


# 책 답안이 뭔가 느낌이 이상해서 만들어본 초 심플 모델
def max3(list):
    if len(list) == 0:
        pass
    elif len(list) == 1:
        return list[0]
    else:
        sub_max = max3[1:]
        return list[0] if list[0] > sub_max else sub_max


print('4-3(4)')
print(max([7, 366, 3, 11, 11111]))
print(max([1]))
print(max([]))

# ----------------------------------------------------------------- #
# 위 max3 함수를 만들고 나서 보니..
# 책의 답안은 결과적으로 len(list) == 2 일 때 원소 2개를 비교하는 (비교적 효율적인) 코드가 맨 마지막에 한번만 실행되는데 비해
# 내가 작성한 코드는 매번 2개의 원소를 비교하고 맨 마지막에 원소 1개일 때 len(list) == 1 에 한번 걸려서 반환하는 코드이기 때문에
# 효율성으로 보자면
# 최초 내 답안 -> n번 실행 -> O(n)
# 책 답안 -> n번 실행 -> O(n)
# 내 답안 -> n/2번 실행 -> O(n)
# 빅오표기법으로는 같으나 그 실행속도의 차이가 2배 정도 벌어진다고 볼 수 있다.

# 180929 추가
# 애초에 'elif len(list) == 2:' 이 부분이 왜 있는지 모르겠다.

# 180929 추가(2)
# 내가 작성한 코드에서 len(list) == 2인 케이스를 넣어보았더니 오류가 난다.
# 책에서 len(list) == 2: 이 부분이 아예 의미가 없지는 않은 것 같다.
# ----------------------------------------------------------------- #


# # 4-5
# > O(n)

# # 4-6
# > O(n)

# # 4-7
# > O(1)

# # 4-8
# > O(n²)
