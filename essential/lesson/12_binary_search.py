
# def binary_search(arr, num):
#
#     low = arr[0]
#     # 헤매기 1
#     high = arr[len(arr)-1]
#
#     while low <= high:
#         # 헤매기 2
#         mid = (low + high) // 2
#
#         if mid == num:
#             return mid
#
#         elif mid < num:
#             low = mid + 1
#         else:
#             high = mid - 1


# 헤매기 3 - index로 low/high 설정한 개념자체를 모르고 있었음.
def binary_search(arr, item):
    low = 0
    # 헤매기 1
    high = len(arr)-1

    while low <= high:
        # 헤매기 2
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':

    # list_data = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
    list_data = ['a', 'c', 'e', 'f', 'g', 'i']

    print('binary_search : ', end='')
    print(binary_search(list_data, 'g'))
