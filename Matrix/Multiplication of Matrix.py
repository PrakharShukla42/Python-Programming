print("FOR FIRST MATRIX")
rows=int(input("Enter The NO Of Rows You Want To Enter:"))
column=int(input("Enter The No Of Coulmn You Want To Enter:"))
ls0=[]
for i in range(rows):
    ls1=[]
    for j in range(column):
        x=int(input("Enter The Elements:"))
        ls1.append(x)
    ls0.append(ls1)
for k in ls0:
    print(k)
print("FOR SECOND MATRIX")
rows=int(input("Enter The NO Of Rows You Want To Enter:"))
column=int(input("Enter The No Of Coulmn You Want To Enter:"))
ls2=[]
for i in range(rows):
    ls1=[]
    for j in range(column):
        x=int(input("Enter The Elements:"))
        ls1.append(x)
    ls2.append(ls1)
for k in ls2:
    print(k)
print("********FIRST MATRIX********")
for k in ls0:
    print(k)
print("********SECOND MATRIX********")
for k in ls2:
    print(k)
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(ls0)):
    for j in range(len(ls2)):
        result[i][j] = ls0[i][j] * ls2[i][j] 
print("Resultant Matrix is")
for r in result: 
   print(r) 

