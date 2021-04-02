def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    print(array)

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def quick_sort(lst):

    if lst == []:
        return []
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x > pivot]
    print(lst, pivot, "is pivot", left, "and", right, "should be sorted")
    new_list = quick_sort(left) + [pivot] + quick_sort(right)
    print("NEW", new_list)
    return new_list


data = [38, 27, 43, 3, 9, 82, 10]
new_data = data

print('Other Quick Sorting')
quick_sort(new_data)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')

print('Sorted Array in Ascending Order:')

size = len(data)
quickSort(data, 0, size - 1)

print(data)






