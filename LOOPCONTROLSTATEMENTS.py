#loop control statments

#break , continue, pass

#BREAK:
#dili mag stop ang while looop og dili nimo iinput imong name
while True:
    name=input("NAME HERE: ")
    if name !="":
        break # terminate
        
        
#CONTINUE"
#here kay gihawa niya ang "-" symbol na ing ana         
phonenum="123-456*789"
for i in phonenum:
    if i =="-":
        if i =="*":
            continue
       
    print(i,end="")
        
        
#PASS
#dinhia na part kay gi skip ra niya ang number 13
for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)        