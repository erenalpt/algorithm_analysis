def radixsort(aList):
    BASEMOD = 10
    terminateLoop = False
    temp = 0
    power = 0
    newList = []
    while not terminateLoop:
        terminateLoop = True
        tempnums = [[] for x in range(BASEMOD)]

        for x in aList:
            temp = int(x / (BASEMOD ** power))
            tempnums[temp % BASEMOD].append(x)
            print(aList)

            if terminateLoop:
                terminateLoop = False

        for y in tempnums:
            for x in range(len(y)):
                if int(y[x] / (BASEMOD ** (power+1))) == 0:
                    newList.append(y[x])
                    aList.remove(y[x])

        power += 1

    return newList


lst = [1, 4, 1, 5, 5, 6, 12, 52, 1, 5, 51, 2, 21, 415, 12, 51, 2, 51, 2]

print(radixsort(lst))
