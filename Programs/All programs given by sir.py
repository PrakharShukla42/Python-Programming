'''1-print(20>30)

2-print(True>2)

3-print("ABC"=="abc")

4-print(10 or 20)

5-print(0 or False)

6-print("abc"or"xyz")

7-print(11 or 10)

8-print(True << 1)

9-print(~5)

10-print(bin(10))

11-print(oct(10))

12-print(hex(10))

a=10>5
print(a)


14-n1=0o17
n2=0b1110010
n3=0x1c2
n=int(n1)
print(n)
n=int(n2)
print(n)
n=int(n3)
print(n)

15-n=int(input("Enter The Binary Number="))
print(bin(n)[2:])

16-n=input("Enter The Binary Number=")
m=input("Enter The Another Binary Number=")
x=int(n,2)+int(m,2)
y=bin(x)
print(y)
print(y[2:])

17-n=int(input("Enter A String="))
if (n&(n-1))==0:
    print("Yes")
else:
    print("No")
    
18-x=int(input("Enter The Number="))
y=int(input("Enter The Number="))
x=x^y
y=x^y
x=x^y
print("Value After Swapping For X:",x)
print("Value After Swapping For Y:",y)

19-a=20
b=20
print(a is b)
print(id(a)==id(b))

20-print("Hello\n"*3)

21-print("Hello"*"Python")

22-print("abcd"[2:])

23-print("Hello"[-4:-2:-1])
'''
'''
24-a="Hello Python"
print("%s"%a[4:])

25-print(max("Hello Python"))

26-a="Hello Python"
print(a.count('o'))

27-a="Hello"
print(a.rfind("e"))

28-x,y=10,20
x,y=y,x
print(x,y)
'''