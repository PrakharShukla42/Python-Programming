n=int(input("Enter the Number of Elements You Want To Enter in Dictionries:"))
d={}
for i in range(n):
    k=int(input("Keys :"))
    v=input("Values :")
    d.update({k:v})
print(d)