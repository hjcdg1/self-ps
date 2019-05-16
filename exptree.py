### 수식 트리 : 컴파일러 이해
### [중위 표기법 -> 후위 표기법] 알고리즘

class Node :
    def __init__ (self, value) :
        self.value = value
        self.left = None
        self.right = None
    def set_value (self, value) :
        self.value = value
    def set_left (self, left) :
        self.left = left
    def set_right (self, right) :
        self.right = right
    def get_value (self) :
        return self.value
    def get_left (self) :
        return self.left
    def get_right (self) :
        return self.right

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

# postfix notation -> expression tree
def construct_tree (postfix) :
    tree_stack = []
    for c in postfix :
        if (is_operand(c)) :
            node = Node(c)
            tree_stack.append(node)
        else :
            node = Node(c)
            node.set_right(tree_stack.pop())
            node.set_left(tree_stack.pop())
            tree_stack.append(node)
    return tree_stack.pop()

def traversal (tree, opt) :
    if (tree == None) :
        return

    # preorder
    if (opt == 0) :
        print(tree.get_value(), end="")
        traversal(tree.get_left(), opt)
        traversal(tree.get_right(), opt)

    # inorder
    elif (opt == 1) :
        if (not is_operand(tree.get_value())) :
            print("(", end="")
        traversal(tree.get_left(), opt)
        print(tree.get_value(), end="")
        traversal(tree.get_right(), opt)
        if (not is_operand(tree.get_value())) :
            print(")", end="")

    # postorder
    else :
        traversal(tree.get_left(), opt)
        traversal(tree.get_right(), opt)
        print(tree.get_value(), end="")

infix = list(input("Enter an expression with the form of infix notation. (without any white spaces) \n: "))
exp_tree = construct_tree(infix_to_postfix(infix))
opt = int(input("Preorder = 0, Inorder = 1, Postorder = 2 \n: "))
traversal(exp_tree, opt)
print()

