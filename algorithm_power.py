# Python3 program to calculate AlgorithmPower(x,n), The exponential of a number.

# T(n) = T(n/2)+Θ(1) ---> T(n)=Θ(logn)
#           / a^(n/2)*a^(n/2)           --> n is even
# a^n   = -
#           \ a^((n-1)/2)*a^((n-1)/2)*a --> n is odd
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Algorithmic Paradigm: Divide and conquer.

def AlgorithmPower(x, n):

    if (n == 0): return 1
    elif (int(n % 2) != 0):
        y = AlgorithmPower(x, (n-1)/2)
        return x*y*y
    else:
        y = AlgorithmPower(x, n/2)
        return y*y



x = 3
n = 2
print("Algorithm Power Calculate: {}".format(AlgorithmPower(x, n)))

# Result : Algorithm Power Calculate: 9