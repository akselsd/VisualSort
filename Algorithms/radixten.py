def radix_sort_base_ten(numlist,handler):
    n = len(numlist.numbers)
    max_digit = len(str(n))

    for base in range(max_digit):
        buckets = [[] for x in range(10)]
        for index, value in enumerate(numlist.numbers):
            handler.update([index])
            base_value = (value // (10**base)) % 10
            buckets[base_value].append(value)
        new_numbers = []
        numlist.numbers = []

        for bucket in buckets:
            new_numbers.extend(bucket)
        for new_index in range(n):
            numlist.numbers.append(new_numbers[new_index])
            handler.update([new_index])

    handler.update()