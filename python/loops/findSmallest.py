smallest = None
for num in [4 ,57, 38, 3784, 4789, 378, 543, 678, 7]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print('the smallest number:', smallest)