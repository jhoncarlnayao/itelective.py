#TUPLE = collection which is ordered and unchangeable



student=("JHONCARL",21,"MALE")

print(student.count("JHONCARL"))


#here kay iprint niya asa or ika pila na index ang "male" na string
#which is ika 2 siya kay 0 man mag sugod permi sa index
print(student.index("MALE"))

for x in student:
    print(x)
    
if "JHONCARL" in student:
    print("JHON CARL IS HERE!")