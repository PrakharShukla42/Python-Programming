def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
        avg=sum//n
        return sum,avg
print('Enter Numbers separated by space:')
lst=[int(x) for x in input().split()]
x,y=calculate(lst)
print('Total :',x)
print('Average :',y)
