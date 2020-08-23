sum = 0.0
count = 0
while True:
    num = input('Enter your number ')
    if num == 'done' :
        break
    try:
        numFinal = float(num)
    except:
        print('Invalid input')
        continue
    sum = sum + numFinal 
    count = count + 1
print(sum, count, sum / count)


    