import sys
import re

class Matrix:
    def __init__(self, w, h):
        self.w = w
        self.h = h

def main(args):
    matrices = []
    # # test matrices 5x4 * 4x6 * 6x2 * 2x7
    matrices.append(Matrix(12,9))
    matrices.append(Matrix(9,5))
    matrices.append(Matrix(5,10))
    matrices.append(Matrix(10,4))
    matrices.append(Matrix(4,6))

    # regular expression
    # AxB (A and B are positive numbers)
    p = re.compile('([1-9][0-9]*)[x]([1-9][0-9]*)')
    for arg in args:
        m = p.search(arg)
        x = int(m.group(1))
        y = int(m.group(2))
        matrices.append(Matrix(x,y))

    optimize_matrix_multiplication(matrices)

def optimize_matrix_multiplication(matrices):
    n = len(matrices)

    d = [matrices[i].w for i in range(n)]
    d.append(matrices[-1].h)

    m = [[0]*n for i in range(n)]
    s = [[0]*n for i in range(n)]

    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l
            results = [ m[i][k] + m[k+1][j]+d[i]*d[k+1]*d[j+1] for k in range(i, j) ]
            m[i][j] = min(results)
            s[i][j] = results.index(m[i][j]) + i

    expression = ["[%dx%d]" % (matrices[i].w, matrices[i].h) for i in range(n)]
    get_expression(s, expression, 0, n-1)
    print('result : '+'\t'.join(expression))

def get_expression(s, expression, i, j):
    if i < j:
        div = s[i][j]
        get_expression(s, expression, i, div)
        get_expression(s, expression, div+1, j)

        if j - i + 1 != len(s):
            expression[i] = '%s%s' % ('(',expression[i])
            expression[j] = '%s%s' % (expression[j], ')')

if __name__ == "__main__":
    main(sys.argv[1:])
