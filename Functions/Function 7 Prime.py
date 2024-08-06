def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input("Enter The Number"))
result=prime(num)
if result==1:
    print(num,"Is Prime")
else:
    print(num,"Is Not Prime")
    