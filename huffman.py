# 비결정적 알고리즘 구현 연습

T = int(input("Number of test cases : "))

def prefix (l1, l2) :
    if (len(l1) >= len(l2)) :
        l1 = l1[0:len(l2)]
    else :
        l2 = l2[0:len(l1)]
    for (i, j) in zip(l1, l2) :
        if (i != j) :
            return False
    return True

def check_prefix (tree, Z, ends, prev, pos) :
    start = 0
    for i in range(0, Z) :
        current = tree[start:ends[i]+1]
        for c in prev :
            if (prefix(c, current)) :
                if (len(current) >= len(c)) :
                    pos.append(i)
                return False
        prev.append(current)
        start = ends[i] + 1
    return True

def check_full (tree, Z, ends, prev) :
    for c in prev :
        pre = c[0:len(c)-1]
        pre.append('1' if (c[len(c)-1] == '0') else '0')
    
        isFound = False
        for p in prev :
            if (prefix(p, pre)) :
                isFound = True
                break
        if (not isFound) :
            return False
    return True

def print_case (tree, Z, ends) :
    start = 0
    for i in range(0, Z) :
        print(i, end="")
        print("->", end="")
        print("".join(tree[start:ends[i]+1]))
        start = ends[i] + 1

for t in range(0, T) :
    Z = int(input("Number of characters : "))
    N = int(input("Arity of the tree : "))
    tree = list(input("Tree : "))
    n = len(tree)

    ends = []
    for i in range(0, Z-1) :
        ends.append(i)
    ends.append(n-1)

    while (True) :
        #print_case(tree, Z, ends)
        prev = []
        pos = []
        isOK = check_prefix(tree, Z, ends, prev, pos) and check_full(tree, Z, ends, prev)
        if (isOK) :
            print_case(tree, Z, ends)
            break

        if (len(pos) == 1) :
            X = pos[0] - 1
        else :
            X = Z -2

        while (X >= 0) :
            if (ends[X] < n+X-Z) :
                ends[X] = ends[X] + 1
                for k in range(X+1, Z-1) :
                    ends[k] = ends[k-1] + 1
                break
            else :
                X = X - 1

        if (X < 0) :
            break


