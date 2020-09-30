# score = float(input("Enter Score: "))

# if score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print("B")
# elif score >= 0.7:
#     print("C")
# elif score >= 0.6:
#     print("D")
# elif score < 0.6:
#     print("F")
# else:
#     print("Error")

# import math

# a = float(input("enter a: "))
# b = float(input("enter b: "))
# c = float(input("enter c: "))
# p = (a+b+c)/2
# s= math.sqrt(p*(p-a)*(p-b)*(p-c))
# print("result:", s)

# Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

# num = int(input())
# if num > -15 and num <= 12 or num > 14 and num < 17 or num >= 19:
#     print("True")
# else:
#     print("False")

# num = input()
# if num.endswith("5") or num.endswith("0") or num.endswith("6") or num.endswith("7") or num.endswith("8") or num.endswith("9"):
#     print(num, "программистов")
# elif num.endswith("1"):
#     print(num, "программист")
# elif num.endswith("2") or num.endswith("3") or num.endswith("4"):
#     print(num, "программиста")

stuff = ["hjj", "hjk", "hjhj"]
print(len(stuff))