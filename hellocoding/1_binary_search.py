import time


def my_timer(original_function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{}함수가 실행된 총 시간: {}초'.format(original_function.__name__, t2))
        return result
    return wrapper


@my_timer
def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 5))
print(binary_search(my_list, 6))
