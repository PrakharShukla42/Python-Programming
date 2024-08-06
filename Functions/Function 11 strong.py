import math  
num = int(input(" Enter the Number:"))  
sum = 0  
temp = num  
  
while(temp > 0):  
    rem = temp % 10  
    fact = math.factorial(rem)
  
    print("Factorial of %d = %d" %(rem, fact))  
    sum = sum + fact  
    temp = temp // 10  
  
print("\n Sum of Factorials of a Given Number %d = %d" %(num, sum))  
      
if (sum == num):  
    print(" The given number is a Strong Number")  
else:  
    print("The given number is not a Strong Number")