
import sys 

# Matrix A[i] has dimension p[i-1] x p[i] 
# for i = 1..n 


def MatrixChainOrder(p, i, j): 

	if i == j: 
		return 0

	_min = sys.maxsize 

	# place parenthesis at different places 
	# between first and last matrix, 
	# recursively calculate count of 
	# multiplications for each parenthesis 
	# placement and return the minimum count 
	for k in range(i, j): 

		count = (MatrixChainOrder(p, i, k) 
				+ MatrixChainOrder(p, k + 1, j) 
				+ p[i-1] * p[k] * p[j]) 

		if count < _min: 
			_min = count 

	# Return minimum count 
	return _min 


# Driver code 
arr = [30,1,40,10,25] 
n = len(arr) 

print("Minimum number of multiplications is ", 
	MatrixChainOrder(arr, 1, n-1)) 

# This code is contributed by Aryan Garg 

def MatChainMul(arr, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        dp[i][i] = 0
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            dp[i][j] = 10**10
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if q < dp[i][j]:
                    dp[i][j] = q
    
    return dp[1][n-1]

arr = [30,1,40,25]
size = len(arr)

print("Minimum number of multiplications are" +str(MatChainMul(arr, size)))

def MatrixChainMultiplication(dims, i, j):
 
    # base case: one matrix
    if j <= i + 1:
        return 0
 
    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')
 
    # take the minimum over each possible position at which the
    # sequence of matrices can be split
 
    """
        (M[i+1]) x (M[i+2]..................M[j])
        (M[i+1]M[i+2]) x (M[i+3.............M[j])
        ...
        ...
        (M[i+1]M[i+2]............M[j-1]) x (M[j])
    """
 
    for k in range(i + 1, j):
 
        # recur for M[i+1]..M[k] to get an i x k matrix
        cost = MatrixChainMultiplication(dims, i, k)
 
        # recur for M[k+1]..M[j] to get a k x j matrix
        cost += MatrixChainMultiplication(dims, k, j)
 
        # cost to multiply two (i x k) and (k x j) matrix
        cost += dims[i] * dims[k] * dims[j]
 
        if cost < min:
            min = cost
 
    # return min cost to multiply M[j+1]..M[j]
    return min
 
 
if __name__ == '__main__':
 
    # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
    # input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
    dims = [30,1,40,25]
 
    print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1))


def MatrixChainMultiplication(dims, i, j, T):
 
    # base case: one matrix
    if j <= i + 1:
        return 0
 
    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a lookup table
    if T[i][j] == 0:
 
        # take the minimum over each possible position at which the
        # sequence of matrices can be split
 
        """
            (M[i+1]) x (M[i+2]..................M[j])
            (M[i+1]M[i+2]) x (M[i+3.............M[j])
            ...
            ...
            (M[i+1]M[i+2]............M[j-1]) x (M[j])
        """
 
        for k in range(i + 1, j):
 
            # recur for M[i+1]..M[k] to get an i x k matrix
            cost = MatrixChainMultiplication(dims, i, k, T)
 
            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += MatrixChainMultiplication(dims, k, j, T)
 
            # cost to multiply two (i x k) and (k x j) matrix
            cost += dims[i] * dims[k] * dims[j]
 
            if cost < min:
                min = cost
 
        T[i][j] = min
 
    # return min cost to multiply M[j+1]..M[j]
    return T[i][j]
 
 
if __name__ == '__main__':
 
    # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
    # input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
    dims = [30,1,40,25]
 
    # lookup table to store the solution to already computed sub-problems
    T = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1, T))


def matrix_product(p):
    """
    Return m and s.

    m[i][j] is the minimum number of scalar multiplications needed to compute the
    product of matrices A(i), A(i + 1), ..., A(j).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.

    p[0... n] is a list such that matrix A(i) has dimensions p[i - 1] x p[i].
    """
    length = len(p) # len(p) = number of matrices + 1

    # m[i][j] is the minimum number of multiplications needed to compute the
    # product of matrices A(i), A(i+1), ..., A(j)
    # s[i][j] is the matrix after which the product is split in the minimum
    # number of multiplications needed

    m = [[-1]*length for _ in range(length)]
    s = [[-1]*length for _ in range(length)]

    matrix_product_helper(p, 1, length - 1, m, s)

    return m, s


def matrix_product_helper(p, start, end, m, s):

    """
    Return the minimum number of scalar multiplications needed to compute the
    product of matrices A(start), A(start + 1), ..., A(end).

    The minimum number of scalar multiplications needed to compute the
    product of matrices A(i), A(i + 1), ..., A(j) is stored in m[i][j].

    The index of the matrix after which the above product is split in an optimal
    parenthesization is stored in s[i][j].

    p[0... n] is a list such that matrix A(i) has dimensions p[i - 1] x p[i].
    """
    if m[start][end] >= 0:
        return m[start][end]

    if start == end:
        q = 0
    else:
        q = float('inf')
        for k in range(start, end):
            temp = matrix_product_helper(p, start, k, m, s) \
                   + matrix_product_helper(p, k + 1, end, m, s) \
                   + p[start - 1]*p[k]*p[end]
            if q > temp:
                q = temp
                s[start][end] = k

    m[start][end] = q
    return q


def print_parenthesization(s, start, end):
    """
    Print the optimal parenthesization of the matrix product A(start) x
    A(start + 1) x ... x A(end).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.
    """
    if start == end:
        print('A[{}]'.format(start), end='')
        return

    k = s[start][end]

    print('(', end='')
    print_parenthesization(s, start, k)
    print_parenthesization(s, k + 1, end)
    print(')', end='')


n = int(input('Enter number of matrices: '))
p = []
for i in range(n):
    temp = int(input('Enter number of rows in matrix {}: '.format(i + 1)))
    p.append(temp)
temp = int(input('Enter number of columns in matrix {}: '.format(n)))
p.append(temp)

m, s = matrix_product(p)
print('The number of scalar multiplications needed:', m[1][n])
print('Optimal parenthesization: ', end='')
print_parenthesization(s, 1, n)
