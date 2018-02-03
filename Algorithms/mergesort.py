
def merge_sort(numlist,handler):

    def merge(handler,numlist,start,q,stop):
        for i in range(start,stop+1):
            handler.update([i])
        sorted_numbers = []
        low = numlist.numbers.copy()[start:q+1]
        high = numlist.numbers.copy()[q+1:stop+1]
        while (low != [] and high != []):
            if low[0]<high[0]:
                k = low.pop(0)
            else:
                k = high.pop(0)
            sorted_numbers.append(k)
        if low != []:
            sorted_numbers.extend(low)
        if high != []:
            sorted_numbers.extend(high)
        for i in range(start,stop+1):
            numlist.numbers[i]=sorted_numbers.pop(0)
            handler.update([i])
    def _merge_sort(handler,numlist,start,stop):
        if start<stop:
            q = (stop + start)//2
            _merge_sort(handler,numlist,start,q)
            _merge_sort(handler,numlist,q+1,stop)
            merge(handler,numlist,start,q,stop)

    _merge_sort(handler,numlist,0,len(numlist.numbers)-1)
