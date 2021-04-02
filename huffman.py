def huffman(freqtable):
    # Ref.: https://bit.ly/3cWJD22
    from collections import defaultdict 
    from heapq import heappush, heappop, heapify

    # mapping of letters to codes
    code = defaultdict(list)

    # Using a heap makes it easy to pull items with lowest frequency.
    # Items in the heap are tuples containing a list of letters and the
    # combined frequencies of the letters in the list.
    heap = [ ( freq, [ ltr ] ) for ltr,freq in freqtable.items() ]
    heapify(heap)

    # Reduce the heap to a single item by combining the two items
    # with the lowest frequencies.
    while len(heap) > 1:
        freq0,letters0 = heappop(heap)
        for ltr in letters0:
            code[ltr].insert(0,'0')

        freq1,letters1 = heappop(heap)
        for ltr in letters1:
            code[ltr].insert(0,'1')

        heappush(heap, ( freq0+freq1, letters0+letters1))

    for k,v in code.items():
        code[k] = ''.join(v)

    return code

for i in range(1,5000):
    
    freqtable = dict(a=8, b=3, c=4, d=12, e=i, f=50, g=25, h=15)
    print(str(i) + " --> " + str(sorted(huffman(freqtable).items())))
   
    
