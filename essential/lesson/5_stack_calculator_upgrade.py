
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


# 181127
# Solved again with much simpler code
# and fixed the flaw of "6 * 2 % 6 = 12"

def bracket_calculator(exp):

    operand = []
    operator = []

    for i in exp:
        if i not in ['+', '-', '*', '%']:
            operand.append(int(i))
            continue

        if len(operator) == 0:
            operator.append(i)
            continue

        # if i in ['+', '-'] and operator[len(operator)-1] in ['*', '%']:

        # Above code made a false result when 6 * 2 % 6 -> 12
        if operator[len(operator)-1] in ['*', '%']:
            # 6 * 2 % 6 -> 0
            num1 = operand.pop()
            num2 = operand.pop()
            oper = operator.pop()

            # mistake
            # result = calculation(num1, num2, oper)
            result = calculation(num2, num1, oper)

            operand.append(result)
            operator.append(i)
        else:
            operator.append(i)

    while True:
        if len(operand) == 1:
            return operand.pop()
        num1 = operand.pop()
        num2 = operand.pop()
        oper = operator.pop()
        # result = calculation(num1, num2, oper)
        result = calculation(num2, num1, oper)
        operand.append(result)


if __name__ == '__main__':
    # expression = '1*2+3'
    # expression = '2+3*4'
    # expression = '1%5'
    expression = '2+3*4+1%5+6*2%6'
    ret = bracket_calculator(list(expression))

    print(f'{expression} = {ret}')


# def bracket_calculator(exp):
#
#     operand_stack = []
#     operator_stack = []
#
#     # 'Use while True + condition: break' instead of 'do ~ while'
#     while True:
#
#         for i in exp:
#             try:
#                 if type(int(i)) is int:
#                     operand_stack.append(int(i))
#             except ValueError:
#
#                 if operator_stack and i in ['-', '+']:
#                     existing_operator = operator_stack.pop()
#                     if existing_operator in ['*', '%']:
#                         operand_2 = operand_stack.pop()
#                         operand_1 = operand_stack.pop()
#                         ret = calculation(operand_1, operand_2, existing_operator)
#                         operand_stack.append(ret)
#
#                     operator_stack.append(i)
#
#                 # when operator is '+' or '-'
#                 else:
#                     operator_stack.append(i)
#                 # exp.pop(0)
#
#         print('stack push')
#         print(operand_stack)
#         print(operator_stack)
#         print()
#
#         while True:
#             operand_2 = operand_stack.pop()
#             operand_1 = operand_stack.pop()
#             operator = operator_stack.pop()
#
#             ret = calculation(operand_1, operand_2, operator)
#             operand_stack.append(ret)
#
#             if not operator_stack:
#                 break
#         if not operator_stack:
#             break
#
#     return operand_stack[0]
#
#
# if __name__ == '__main__':
#     # expression = '1*2+3'
#     expression = '2+3*4+1%5+6*2%6'
#     result = bracket_calculator(list(expression))
#     print(f'{expression} = {result}')
