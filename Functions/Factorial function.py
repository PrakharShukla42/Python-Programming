def fact(n):  
    if (n==0):
        return 1
    else:
        return n*fact(n - 1)
num = int(input("Enter The Number You Want To Do Factorial :"))
print('Fact of',num,'is:',fact(num))