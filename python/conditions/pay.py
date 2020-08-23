hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h <= 40:
    pay = h * r
else:
    plus = h - 40
    payst = (h-plus) * r
    pay = ((1.5 * r) * plus) + payst
print(pay)