import copy, math
# show menu and return choice
def menu(menu_items):
    _ = [print(item) for item in menu_items]
    return int(input('Your choice: > ' ))

# convert the string to int or float depending on the string
def int_or_float(s):
    return float(s) if '.' in s or 'e' in s.lower() else int(s)

# matrix multiplication by a constant
def mult_const():
    print('Enter size of matrix: > ', end = '')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('Enter constant: > ', end='')
    c = int_or_float(input())

    print('The result is:')
    for i in range(n1):
        print(" ".join([str(c * A1[i][j]) for j in range(m1)]))
    print('')

# matrix addition
def add_matr():
    print('Enter size of first matrix: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter first matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('Enter size of second matrix: >')
    n2, m2 = [int(x) for x in input().split()]
    A2 = [0] * n2
    print('Enter second matrix: >')
    for i in range(n2):
        A2[i] = [int_or_float(x) for x in input().split()]

    if n1 == n2 and m1 == m2:
        print('The result is:')
        for i in range(n1):
            print(" ".join([str(A1[i][j] + A2[i][j]) for j in range(m1)]))
    else:
        print("The operation cannot be performed.")
    print('')

# matrix multiplication
def mult_matr():
    print('Enter size of first matrix: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter first matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('Enter size of second matrix: > ', end='')
    n2, m2 = [int(x) for x in input().split()]
    A2 = [0] * n2
    print('Enter second matrix: >')
    for i in range(n2):
        A2[i] = [int_or_float(x) for x in input().split()]

    if m1 == n2:
        print('The result is:')
        for i in range(n1):
            print(" ".join([str(sum([A1[i][j] * A2[j][k] for j in range(m1)])) for k in range(m2)]))
    else:
        print("The operation cannot be performed.")
    print('')

# matrix transposition
def transpose_matr():
    transpose_menu = ['1. Main diagonal', '2. Side diagonal',
                      '3. Vertical line', '4. Horizontal line']
    n = menu(transpose_menu)
    if n == 1:
        trans_main()
    elif n == 2:
        trans_side()
    elif n == 3:
        trans_vert()
    elif n == 4:
        trans_horiz()

# matrix transposition: main diagonal
def trans_main():
    print('Enter matrix size: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('The result is:')
    for i in range(m1):
        print(" ".join([str(A1[j][i]) for j in range(n1)]))

    print('')

# matrix transposition: side diagonal
def trans_side():
    print('Enter matrix size: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('The result is:')
    for i in range(m1):
        print(" ".join([str(A1[-j - 1][ -i - 1]) for j in range(n1)]))

    print('')

# matrix transposition: vertical line
def trans_vert():
    print('Enter matrix size: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('The result is:')
    for i in range(n1):
        print(" ".join([str(A1[i][-j - 1]) for j in range(m1)]))

    print('')

# matrix transposition: horizontal diagonal
def trans_horiz():
    print('Enter matrix size: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]

    print('The result is:')
    for i in range(n1):
        print(" ".join([str(A1[-i -1][j]) for j in range(m1)]))

    print('')

# matrix determinat
def det_matr():
    print('Enter matrix size: > ', end='')
    n1, m1 = [int(x) for x in input().split()]
    A1 = [0] * n1
    print('Enter matrix: >')
    for i in range(n1):
        A1[i] = [int_or_float(x) for x in input().split()]
    if n1 == m1:
        print('The result is:')
        print(det(A1))
    else:
        print("The operation cannot be performed.")

    print('')

# return a new matrix by removing row i and column j from nxn matrix A
# i and j runs from 0 to n-1
def red_matr(A, i, j):
    n = len(A)
    B = copy.deepcopy(A)
    B.pop(i)
    for p in range(n - 1):
        B[p].pop(j)

    return B

# recursive calculation of determinat
def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        #  expanding along the first column i = 0
        #  index of the element is i+1,j+1 <-->  A[i][j]
        return sum([((-1) ** (1 + j + 1)) * A[0][j] * det(red_matr(A, 0, j)) for j in range(n)])

# return transposed matrix of nxm matrix A
def trans(A):
    n = len(A)
    m = len(A[0])
    B = [[0] * n] * m
    for i in range(m):
        B[i] = [A[j][i] for j in range(n)]

    return B


# inverse of matrix
def inv_matr():
    print('Enter matrix size: > ', end='')
    n, m = [int(x) for x in input().split()]
    A = [0] * n
    print('Enter matrix: >')
    for i in range(n):
        A[i] = [int_or_float(x) for x in input().split()]
    if n != m:
        print('This matrix doesn\'t have an inverse.\n')
        return
    d = float(det(A))
    if d == 0:
        print('This matrix doesn\'t have an inverse.\n')
        return
    invA = [[0] * n for i in range(n)]  # inverse matrix
    for i in range(n):
        for j in range(n):
            invA[j][i] = ((-1) ** (i + j)) * det(red_matr(A, i, j)) / d
    print('The result is:')
    for i in range(n):
         print(" ".join([str(round(invA[i][j], 4)) for j in range(n)]))
    print('')

################################################

main_menu = ['1. Add matrices', '2. Multiply matrix by a constant',
                  '3. Multiply matrices', '4. Transpose matrix',
             '5. Calculate a determinant', '6. Inverse matrix', '0. Exit']
# Main loop
while True:
    n = menu(main_menu)
    if n == 0:
        break
    if n == 1:
        add_matr()
    elif n == 2:
        mult_const()
    elif n == 3:
        mult_matr()
    elif n == 4:
        transpose_matr()
    elif n == 5:
        det_matr()
    elif n == 6:
        inv_matr()

