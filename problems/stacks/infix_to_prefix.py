def infix_to_prefix(infix_expr):
    def get_precedence(operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def is_operator(char):
        return char in {'+', '-', '*', '/', '^'}

    def reverse_string(string):
        return string[::-1]

    stack = []
    prefix = []
    for char in reverse_string(infix_expr):
        if char.isalnum():  # Operand
            prefix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()  # Discard ')'
        elif is_operator(char):  # Operator
            while stack and is_operator(stack[-1]) and get_precedence(stack[-1]) > get_precedence(char):
                prefix.append(stack.pop())
            stack.append(char)

    while stack:
        prefix.append(stack.pop())

    return ''.join(reverse_string(prefix))


# Example usage:
infix_expr = "(a+b)*(c-d)+e/f*(g-h)+i*(j+k)/(l*m-n)*(o+p)/q-r*s/(t+u)*v-w/(x*y+z)"
prefix_expr = infix_to_prefix(infix_expr)
print(f"Infix Expression: {infix_expr}")
print(f"Prefix Expression: {prefix_expr}")
