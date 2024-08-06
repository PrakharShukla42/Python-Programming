def fact(n):
    prod=1
    while n>=1:
        prod*=n
        n=n-1
    return prod
for i in range(1,11):
    print("Factorial Of {} is {}".format(i,fact(i)))
    