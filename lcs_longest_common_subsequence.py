def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


S1 = "ABCBDAB"
S2 = "BDCABA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = "ok"
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = "left"
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = "up"
    return c, flag


def printlcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == "ok":
        printlcs(flag, a, i-1, j-1)
        print(a[i-1], end="")
    elif flag[i][j] == "left":
        printlcs(flag, a, i, j-1)
    else:
        printlcs(flag, a, i-1, j)


a="ABCB"
b="BDCAB"
c, flag=lcs (a, b)
for i in c:
    print (i)
print ("")
for j in flag:
    print (j)
print ("")
printlcs (flag, a, len (a), len (b))
print ("")
