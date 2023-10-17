#logical operators ( and,or,not) check two or more conditional
temp= int(input("TEMPERATURE: "))



if  not(temp >=0 and temp <=30):
    print("TEMPERATURE IS GOOD TODAY")
    print("GO OUTSIDE")
elif not(temp<0 or temp>30):
    print("TEMPERATURE IS BAD")
    print("STAY INSIDE")
    
    
    #if you use NOT u just reverse the roll or the print that you put inside of ifelse
    #kumbaga kanang sa first na if giswap nimo ang unod sa baba na elif
    
 