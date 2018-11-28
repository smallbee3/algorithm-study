
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


# # 헤매기 3 - index로 low/high 설정한 개념자체를 모르고 있었음.
# def binary_search(arr, item):
#     low = 0
#     # 헤매기 1
#     high = len(arr)-1
#
#     while low <= high:
#         # 헤매기 2
#         mid = (low + high) // 2
#         guess = arr[mid]
#
#         if guess == item:
#             return mid
#         elif guess < item:
#             low = mid + 1
#         else:
#             high = mid - 1

# 2018.11.28
# Solved third time, but still it takes a bit of time.
def binary_search(arr, item):

    low = 0
    high = len(arr)-1

    while low <= high:

        # mistake
        # mid = low + high // 2
        mid = (low + high) // 2

        if arr[mid] == item:
            return print(f'index: {mid}, value: {arr[mid]}')
        if arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    print('The input number does not exist in the list')


if __name__ == '__main__':

    print('binary_search : ', end='')

    # list_data = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
    # binary_search(list_data, 10)

    list_data = ['a', 'c', 'e', 'f', 'g', 'i']
    binary_search(list_data, 'e')
