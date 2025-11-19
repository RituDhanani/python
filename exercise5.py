def pair(numbers, n):
    show = set()
    pairs=set()
    for num in numbers:
        complement = n - num
        if complement in show:
            pair = tuple(sorted([num, complement]))
            pairs.add(pair)
        show.add(num)
    
    return [list(pair) for pair in pairs]
numbers = [9,4,8,10,2,4,8,3,14,4,8]
n=12
output = pair(numbers, n)
print(output)


 