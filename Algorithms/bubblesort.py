def bubble_sort(numlist,handler):
    numbers = numlist.numbers
    n = len(numlist.numbers)
    for i in range(n):
        for k in range(n-i-1):
            handler.update([k])
            if numbers[k]>numbers[k+1]:
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
    handler.update([])