h = input("height >")
w = h*2 - 1
spaces = h*2
leg = int((h*2-1)/2)
i = 1
while i <= h:
    print ' '*(spaces - i + 1), '*'*(2*i-1)
    i = i + 1
print ' '*(leg+(h+1)), "*"
