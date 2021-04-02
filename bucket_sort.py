def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
        print(bucket)
    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
      
    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
           
            array[k] = bucket[i][j]
            
            k += 1
    return array

# EX:[49, 50, 76, 98] = [.49, .50, .76, .98]
array = [.29, .25 , .03, .49, .09, .37, .21, .43]
print("Sorted Array in descending order is")
print(bucketSort(array))