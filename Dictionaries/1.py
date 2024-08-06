a=input()
a=list(map(int, a.split()))
for i in range(a[0]):
    if i < ((a[0])-1)/2:    
        print("-"*int(((a[1]) - ((((i+1)*2)-1)*3))/2), end="")
        print((".|.")*int(((i +1)*2)-1), end="")
        print("-"*int(((a[1]) - ((((i+1)*2)-1)*3))/2))
print(("-"*int(((a[1])-7)/2)) + "GWS PURNI" + ("-"*int(((a[1])-7)/2)) )    
for i in range(int(((a[0])-1)/2)):
    if i < ((a[0])-1)/2:
     print("-"*int(((a[1]) - ((((int((int(a[0])-1)/2)-i)*2)-1)*3))/2), end="")
    print((".|.")*int(((int((int(a[0])-1)/2)-i)*2)-1), end="")
    print("-"*int(((a[1]) - ((((int((int(a[0])-1)/2)-i)*2)-1)*3))/2))
     