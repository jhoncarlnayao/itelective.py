# str.format()



animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)


print("The {} jumped over the {}".format("cow","moon"))
# or this one
print("The {} jumped over the {}".format(animal,item))

print("The {1} jumped over the {0}".format(animal,item))#Positional argument

print("The {animal1} jumped over the {item1}".format(animal1="shark",item1="sea"))#Keyword argument

text =" The {} jumped over the {} "
print(text.format(animal,item))