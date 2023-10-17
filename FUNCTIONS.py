#FUNCTIONS = a block of code which is executed only when it called

#kung gusto nimo maka add og name or such dapat isulod nimo ang variable sulod anang hello()
def hello(name,lastname,age):
    print("FIRST NAME "+name)
    print("LAST NAME: "+lastname)
    print("YOU ARE "+str(age)+" YEARS OLD")




#mo run lang ni siya og naa ni nga function
hello(name=input("FRISTNAME HERE: "),
      lastname=input("LASTNAME HERE: "),
      age=int(input("AGE HERE: ")))


#name="nayao"
#hello(name)