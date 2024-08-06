student=(1,"Prakhar Shukla",28,29,30,25,23)
rno,name=student[0:2]
print("Roll Number Of Student =",rno)
print("Name Of Student Is =",name)
s=english,electrical,iiot,physics,maths=student[2:8]
print("Marks In English Are =",english)
print("Marks In Electrical Are =",electrical)
print("Marks In IIOT Are =",iiot)
print("Marks In Physics Are =",physics)
print("Marks In Maths Are =",maths)
k=sum(s)
print("Total Marks=",k)
percentage=k*100/150
print("Percentage Of Marks =",percentage)
print("Total Elements In Tuple Are=",len(student))
print("Minimun Marks  In Exams Are =",min(s))
print("Maximun Marks  In Exams Are =",max(s))
print(s.count(23))
print(s.index(30))
print(sorted(s))
avg=k/5
print("Average Of Marks Is =",avg)

