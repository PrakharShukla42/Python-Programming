rows=int(input("Enter The NO Of Rows You Want To Enter:"))
column=int(input("Enter The No Of Coulmn You Want To Enter:"))
ls=[]
for i in range(rows):
    ls1=[]
    for j in range(column):
        x=int(input("Enter The Elements:"))
        ls1.append(x)
    ls.append(ls1)
    #print(ls)
print(ls)
print("List In Matrix Form")
for k in ls:
    print(k)
add=0
for i in range(len(ls)):
    for j in range(len(ls)):
        if i==j:
            add+=ls[i][j]
print("Sum Of Diogonal ELements:",add)    

