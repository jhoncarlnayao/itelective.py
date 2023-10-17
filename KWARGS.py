# **kwargs



def hello(**kwargs):
   # print(" HELLO "+kwargs["first"]+" "+kwargs["last"])
    print("HELLO",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    
hello(first="jhoncarl",middle="sauyan",last="nayao")


