
# def push(stack, item):
#     stack.append(item)
#
#
# def pop(stack):
#     return stack.pop()


# if __name__ == '__main__':
#     stack = []
#     push(1)
#     push(2)
#     push(3)
#     push(4)
#
#     print('current stack')
#     print(stack)
#
#     while stack:
#         print('POP > {}'.format(pop()))

def calculation(operand_1, operand_2, operator):
    if operator == '+':
        ret = operand_1 + operand_2
        return ret

    elif operator == '-':
        ret = operand_1 - operand_2
        return ret

    elif operator == '*':
        ret = operand_1 * operand_2
        return ret

    elif operator == '%':
        ret = operand_1 % operand_2
        return ret


def normal_calculator(exp):

    operand_stack = []
    operator_stack = []

    while exp:
        exp_list = exp.copy()
        for i in exp_list:
            try:
                if len(operand_stack) < 2 and\
                        type(int(i)) is int:
                    operand_stack.append(int(i))
                    exp.pop(0)
            except ValueError:
                if len(operator_stack) < 1:
                    operator_stack.append(i)
                    exp.pop(0)
            if len(operand_stack) == 2 and len(operator_stack) == 1:
                break

        print('stack push')
        print(operand_stack)
        print(operator_stack)
        print(exp)
        print()

        operand_2 = operand_stack.pop()
        operand_1 = operand_stack.pop()
        operator = operator_stack.pop()

        ret = calculation(operand_1, operand_2, operator)
        operand_stack.append(ret)

        print('stack pop & calculation')
        print(operand_stack)
        print(operator_stack)
        print(exp)
        print()
    return operand_stack[0]


if __name__ == '__main__':
    expression = '2*3+1'
    result = normal_calculator(list(expression))
    print(f'{expression} = {result}')
