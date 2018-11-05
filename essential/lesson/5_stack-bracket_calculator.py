
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


def bracket_calculator(exp):

    operand_stack = []
    operator_stack = []

    # 'Use while True + condition: break' instead of 'do ~ while'
    while True:

        for i in exp:
            try:
                if type(int(i)) is int:
                    operand_stack.append(int(i))
            except ValueError:

                if operator_stack and i in ['-', '+']:
                    existing_operator = operator_stack.pop()
                    if existing_operator in ['*', '%']:
                        operand_2 = operand_stack.pop()
                        operand_1 = operand_stack.pop()
                        ret = calculation(operand_1, operand_2, existing_operator)
                        operand_stack.append(ret)

                    operator_stack.append(i)

                # when operator is '+' or '-'
                else:
                    operator_stack.append(i)
                # exp.pop(0)

        print('stack push')
        print(operand_stack)
        print(operator_stack)
        print()

        while True:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            operator = operator_stack.pop()

            ret = calculation(operand_1, operand_2, operator)
            operand_stack.append(ret)

            if not operator_stack:
                break
        if not operator_stack:
            break

    return operand_stack[0]


if __name__ == '__main__':
    # expression = '1*2+3'
    expression = '2+3*4+1%5+6*2%6'
    result = bracket_calculator(list(expression))
    print(f'{expression} = {result}')
