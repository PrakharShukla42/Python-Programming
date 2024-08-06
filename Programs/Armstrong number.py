num = int(input("Enter the number:"))
sum = 0
a= num
while(a > 0):
    digit=a%10
    print(digit)
    sum+=digit**4
    print(sum)
    a//=10
if num==sum:
     print(num, "is an Armstrong number.")                                                                          
else:
    print(num, "is not an Armstrong number.")
