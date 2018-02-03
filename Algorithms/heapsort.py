
def heap_sort(numlist,handler):

    def heap(i):
        l = 2 * i
        r = 2 * i + 1

        max_value = max(l, r, i, key = lambda x : find_max(x))

        if max_value != i:
            numlist.numbers[max_value], numlist.numbers[i] = numlist.numbers[i], numlist.numbers[max_value]
            handler.update([max_value], [i])
            heap(max_value)

    def find_max(x):
        if x<=heap_size:
            return numlist.numbers[x]
        return -1

    n = len(numlist.numbers)
    heap_size = n-1
    to_heap = list(range(n//2,-1,-1))
    while to_heap:
        i = to_heap.pop(0)
        heap(i)

    for i in range(n-1,0,-1):
        numlist.numbers[i], numlist.numbers[0] = numlist.numbers[0], numlist.numbers[i]
        handler.update([i],[0])
        heap_size -=1
        heap(0)


