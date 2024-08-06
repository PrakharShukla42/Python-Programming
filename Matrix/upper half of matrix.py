rows=int(input("Enter The NO Of Rows You Want To Enter:"))
column=int(input("Enter The No Of Coulmn You Want To Enter:"))
ls=[]
for i in range(rows):
    ls1=[]
    for j in range(column):
        x=int(input("Enter The Elements:"))
        ls1.append(x)
    ls.append(ls1)
for k in ls:
    print(k)
for i in range(len(ls)):
    for j in range(len(ls)):
        if i<=j:
            ls[i][j]=ls[i][j]
        else:
            ls[i][j]=0
print("Upper Half Of Matrix")
for i in ls:
    print(i)
        
