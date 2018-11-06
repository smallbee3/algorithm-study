# sorting이 되어 있지 않기 때문에 binary search를 사용할 수 없다.
# -> 무슨소리??

# def binary_search(arr, item):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#
#         if guess == item:
#             return mid
#         elif guess < item:
#             low = mid + 1
#         else:
#             high = mid - 1


# min finder 조금 다른 방식으로 품. (hello coding 책 답안과 다름)
def find_min_num(arr):
    if len(arr) == 0:
        pass
    elif len(arr) == 1:
        return arr[0]
    else:
        # min1 = arr[0] if arr[0] < arr[1] else arr[1]
        sub_min = find_min_num(arr[1:])
        # min1 = sub_min if min1 > sub_min else min1
        min1 = sub_min if arr[0] > sub_min else arr[0]
        return min1


# 0) while 문으로 풀기 (최초)
# def selection_sort(arr):
#
#     i = 0
#     while i < len(arr):
#         ret = find_min_num(arr[i:])
#         index_num = arr.index(ret)
#         print(f'min: {ret}, index: {index_num}')
#
#         # 숫자 교환하기
#
#         # 생각해보니 temp가 필요없었음.
#         # temp = arr[i]
#         # arr[i] = ret
#         # arr[index_num] = temp
#         if index_num != i:
#             arr[index_num] = arr[i]
#             arr[i] = ret
#             print(arr)
#             print()
#         else:
#             print(index_num, i)
#             print('건너뛴다')
#             print()
#
#         i += 1
#     return arr

def selection_sort(arr):

    #  * while + i 보다 보다 더 깔끔!
    #  * 선택정렬에서 정렬 대상의 마지막 원소는 검색할 필요가..? 없네..
    #    -> len(arr)-1
    # for i in range(len(arr)):
    for i in range(len(arr)-1):

        # 1) arr[i:]일 경우 -> min(ret)과 비교연산이 필요 없다.

        # ret = find_min_num(arr[i:])
        # index_num = arr.index(ret)
        # print(f'{i}번째, min: {ret}, index: {index_num}')
        # # 숫자 교환하기
        #
        # # 생각해보니 temp가 필요없었음.
        # # temp = arr[i]
        # # arr[i] = ret
        # # arr[index_num] = temp
        # if index_num != i:
        #     arr[index_num] = arr[i]
        #     arr[i] = ret
        #     print(arr)
        #     print()
        # else:
        #     print(arr)
        #     print(index_num, i)
        #     print('건너뛴다')
        #     print()

        # 2) arr[i+1:]일 경우 -> min(ret)과 비교연산이 필요 하다.

        print(i+1)
        ret = find_min_num(arr[i+1:])
        index_num = arr.index(ret)
        print(f'{i}번째, min: {ret}, index: {index_num}')

        if index_num != i and ret < arr[i]:
            arr[index_num] = arr[i]
            arr[i] = ret
            print(arr)
            print()
        else:
            print(arr)
            print(index_num, i)
            print('건너뛴다')
            print()

    return arr


if __name__ == '__main__':

    list_data = [5, 1, 3, 7, 2, 9]

    result = selection_sort(list_data)
    print(result)
