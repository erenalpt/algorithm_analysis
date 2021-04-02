def instertionsort(seq):

    for slice_end in range(len(seq)):
        pos = slice_end
        # inserting elements at correct position

        while pos > 0 and seq[pos] < seq[pos - 1]:
            (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
            pos = pos - 1
            print(seq)


# test input
l = [12, 11, 13, 5, 6]
instertionsort(l)
print()
print("insertion Sort Array: {}".format(l))