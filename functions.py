tom_list = [45,34,689]
joy_list = [65,87,32]

total = 0
item: int
for i in tom_list:
    total = total+i
print("Tom's expense:",total)

total = 0
for item in joy_list:
    total = total + item
print("Joy's expense:", total)

example1

def calculate_total(exp):
    total=0
    for i in exp:
        total=total +i
    return total

tom_list = [45,34,689]
joy_list = [65,87,32]

tom_total=calculate_total(tom_list)
joy_total=calculate_total(joy_list)

print("Tom's total expense",tom_total)
print("Joy's total expense",joy_total)

example2

def sum(a,b):
    SUM=int(a)+int(b)
    return SUM

a=input("Enter first number")
b=input("Enter second number")

Sum=sum(a,b)

print("The sum of two numbers is:",Sum)