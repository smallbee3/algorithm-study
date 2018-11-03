# # Prime number Special


# (1) Prime number check
def prime_check(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print(prime_check(7))


# (2) Return prime number list
def prime_list(num):
    count = 0
    start = 1
    list = []
    while count < num:
        if prime_check(start):
            list.append(start)
            count += 1
        start += 1
    return list


# print(prime_list(5))


# (3) Return nth prime number
# def prime_nth(num):
#     count = 0
#     start = 1
#     while count < num:
#         if prime_check(start):
#             count += 1
#         start += 1
#     return start-1
#
#
# print(prime_nth(52))


# p.125

HASHTABLE_SIZE = 10


def alphabet_to_prime(str):
    list52 = prime_list(52)

    # Alphabet - primenumber Hash table 만들기
    hash_table = {}
    for i, j in enumerate(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']):
        hash_table[j] = list52[i]
    sum = 0
    for i in str:
        sum += hash_table[i]
    return sum % HASHTABLE_SIZE


# 5-5
print('5-5')
print(alphabet_to_prime('Esther'))
print(alphabet_to_prime('Ben'))
print(alphabet_to_prime('Bob'))
print(alphabet_to_prime('Dan'))


# 5-6
print('5-6')
print(alphabet_to_prime('A'))
print(alphabet_to_prime('AA'))
print(alphabet_to_prime('AAA'))
print(alphabet_to_prime('AAAA'))


# 5-7
print('5-7')
print(alphabet_to_prime('MAUS'))
print(alphabet_to_prime('FunHome'))
print(alphabet_to_prime('Watchmen'))


# My Test
print('My Test')
print(alphabet_to_prime('MAUS'))
print(alphabet_to_prime('AUSM'))
print(alphabet_to_prime('SUAM'))
