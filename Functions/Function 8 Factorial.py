def fact(n):  
    if (n==0) :
        return 1       
    else:
        return n*fact(n - 1)
num = 5  
print('Factorial of'  , num ,  'is:' ,fact(num))
print('Fact of',num,'is:',fact(num))