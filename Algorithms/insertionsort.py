def insertion_sort(numlist,handler):
    n = len(numlist.numbers)
    for i in range(n):
        j = i
        while numlist.numbers[j] < numlist.numbers[j-1] and j > 0:
            numlist.numbers[j],numlist.numbers[j-1]=numlist.numbers[j-1],numlist.numbers[j]
            j-=1
            handler.update([j])
    handler.update()