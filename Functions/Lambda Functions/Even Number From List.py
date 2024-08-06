def even(x):
    if x%2==0:
        return True
    else:
        return False
lst=[10,21,32,43,54]
lst1=list(filter(even,lst))
print(lst1)    
    