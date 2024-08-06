number = int(input("Enter Desired Number -"))
res = number % 10
while number > 9:
    number = number // 10
res += number
print('Addition of first and last digit of number is', res)