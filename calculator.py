### 스택을 활용한 계산기 구현
### [중위 표기법 -> 후위 표기법] 알고리즘

def is_operand (c) :
    return c.isdigit()

def is_op (c) :
    return (c == '+' or c == '-' or c == '*' or c == '/' or c == '(' or c == ')')

def prec (c) :
    if (c == '*' or c == '/') :
        return 5
    elif (c == '+' or c == '-') :
        return 3
    else :
        return 1

# infix notation -> postfix notation
def infix_to_postfix (infix) :
    op_stack = []
    postfix = []

    for c in infix :
        if (is_operand(c)) :
            postfix.append(c)
        else :
            if (len(op_stack) == 0) :
                op_stack.append(c)
            else :
                if (c == '(') :
                    op_stack.append('(')
                elif (c == ')') :
                    while(op_stack[len(op_stack)-1] != '(') :
                        postfix.append(op_stack.pop())
                    op_stack.pop()
                else :
                    while (len(op_stack) != 0 and prec(op_stack[len(op_stack)-1]) >= prec(c)) :
                        postfix.append(op_stack.pop())
                    op_stack.append(c)

    while (len(op_stack) != 0) :
        postfix.append(op_stack.pop())

    return postfix

# evaluate postfix notation
def eval (postfix) :
    stack = []
    for c in postfix :
        if (is_operand(c)) :
            stack.append(int(c))
        else :
            v1 = stack.pop()
            v2 = stack.pop()
            if (c == '+') :
                stack.append(v1 + v2)
            elif (c == '-') :
                stack.append(v1 - v2)
            elif (c == '*') :
                stack.append(v1 * v2)
            elif (c == '/') :
                stack.append(v1 / v2)
    return stack.pop()

# calcuate infix notation
def calculate (infix) :
    postfix = infix_to_postfix (infix)
    return eval (postfix)

input_str = input("Enter an expression with the form of infix notation to calculate. (without any white spaces) \n: ")
input_list = list(input_str)
print("The result:", calculate(input_list))

