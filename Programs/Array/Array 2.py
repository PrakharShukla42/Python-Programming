from array import*
arr=array('d',[1.2,2.5,-3.5,4])
arr1=array(arr.typecode,(a*3 for a in arr))
print("The Array 1 Elements Are:")
for i in arr1:
    print(i)