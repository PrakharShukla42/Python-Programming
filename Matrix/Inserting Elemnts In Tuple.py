stud=("Prakhar","Aditya","Faiz","Sumit","Nitin")
print(stud)
elem=[input("Enter The Name You Want To Insert =")]
elem_new=tuple(elem)
pos=int(input("Enter The Postion You Want To Enter ="))
new_stud=stud[0:pos-1]
new_stud=new_stud+elem_new
stud=new_stud+elem_new[pos-1:]
print(stud)
print(len(stud))


