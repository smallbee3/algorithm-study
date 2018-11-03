# fibonachi by recursion
from helper import my_timer


@my_timer
def fibo(num):
    # arr = [1, 1]
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(7))


# fibonacchi arr 출력(1)
@my_timer
def fibo_arr(num):

    fibo_list = []
    # fibo_list = [1, 1]
    #
    # if num == 1:
    #     return fibo_list[0]
    # elif num == 2:
    #     return fibo_list[1]
    # else:
    # for i in range(1, num+1):
    for i in range(num):
        fibo_list.append(fibo(i+1))
    return fibo_list


print(fibo_arr(5))


# fibonacchi arr 출력(2) - without recursion
@my_timer
def fibo_arr2(num):

    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fibo_list = [1, 1]
        for i in range(2, num):
            result = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.append(result)
        return fibo_list


print(fibo_arr2(10))


# fibonachi without recursion
def fibo2(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        a = 1
        b = 1
        # for i in range(2, num):
        # 여기서 i는 하는 역할이 없고, for ~ in range()는 결과적으로
        # num-1 만큼 하단의 코드를 실행하는 것밖에는 역할이 없다.
        # 특정 횟수만큼만 코드를 반복실행할 때 이 for ~ in range() 말고는 딱히 생각이 나지 않아서
        # 그냥 이대로 둠. (while + i += 1 을 쓰는 방법이 있긴하다..
        for i in range(num-2):
            c = a + b
            print(a, b, c)
            a = b
            b = c
        return c


print(fibo2(7))


# 181027
#  p.57

#  Without Recursion
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not None:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('I found the key!')


# With Recursion (*****)

def look_for_key_with_recursion(box):

    for item in box:
        if item.is_a_key():
            return print('I found the key!')
        elif item.is_a_box():
            return look_for_key_with_recursion(item)

    return 'There is no key.'

# look_for_key_with_recursion(main_box)
