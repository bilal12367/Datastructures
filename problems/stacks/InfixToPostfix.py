
def infix_to_postfix(infix_expr):
    def get_precedence(operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def is_operator(char):
        return char in {'+', '-', '*', '/', '^'}

    stack = []
    postfix = []

    for char in infix_expr:
        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        elif is_operator(char):  # Operator
            while stack and is_operator(stack[-1]) and get_precedence(stack[-1]) >= get_precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def infixToPostFix(s):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(char):
        print(char)
        return char in ['+', '-', '*', '/', '^']
    postfix = []
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c.isalnum():
            postfix.append(c)
        elif c == ')':
            stack.append(c)
        elif c == '(':
            while stack and stack[-1] != ')':
                postfix.append(stack.pop())
            stack.pop()
        elif c in '+-*/^':
            while stack and stack[-1] in '+-*/^' and prec[c] < prec[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)[::-1]


exp = '(a+b)*(c-d)+e/f*(g-h)+i*(j+k)/(l*m-n)*(o+p)/q-r*s/(t+u)*v-w/(x*y+z)'

print(infixToPostFix(exp[::-1]))
# print(infix_to_postfix(exp))
