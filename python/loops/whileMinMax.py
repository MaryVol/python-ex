max = 0 
min = None
while True:
    num = input("Enter your number ")
    if num == 'done':
        break
    try:
        numFinal = float(num)
    except: 
        print('invalid input')
        continue
    if numFinal > max:
        max = numFinal 
    if min is None:
        min = numFinal
    elif min > numFinal:
        min = numFinal
print("Min value", min, "max value", max) 