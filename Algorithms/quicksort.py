def quick_sort(numlist,handler):
    n = len(numlist.numbers)
    numbers = numlist.numbers
    list_indicies = [(0,n-1)]
    while list_indicies:
        min_n,max_n= list_indicies.pop()
        if min_n<max_n:
            pivot = min_n
            for i in range(min_n+1,max_n+1):
                handler.update([i],[pivot])
                if numbers[i]<numbers[min_n]:
                    pivot+=1
                    numbers[pivot], numbers[i] = numbers[i], numbers[pivot]
            numbers[min_n],numbers[pivot] = numbers[pivot],numbers[min_n]
            handler.update([],[pivot])
            list_indicies.extend([(pivot+1,max_n),(min_n,pivot-1)])