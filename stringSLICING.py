#slicing 

name ="jhon carl"

firstname=name[0:4] #by index
#firstname=name[:3] more simple
lastname=name[5:9]

funkyname=name[:9:1]
#funkyname=name[::1] more simple way

reversename=name[::-1]#make the name reverse
print(reversename)


print(firstname)
print(lastname)
print(funkyname)



web="http://google.com"
web2="http://wikipedia.com"

#separate each value 
slice=slice(7,-4)
print(web[slice])

print(web2[slice])