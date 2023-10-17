#SET = collection which is unordered,unindexed no duplicate values
# so ang set kay naka random siya kung unsa imong i print


utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#add
utensils.add("napkin")

#remove
utensils.remove("fork")

#empty list
utensils.clear()

#also here same ra siya sababa
dishes.update(utensils)

#so here kay mura gi combine nimo tanan kung i print nimo ang dinner
#kay ma print unsa ang sulod nga naa sa utensils and dishes
dinner=utensils.union(dishes)

#icompare niya kung unsa ang difference saila duha 
print(utensils.difference(dishes))    

#i print niya unsa common saila or like naa ba sila kapareha 
print(utensils.intersection(dishes))


for x in dinner:
    print(x)
    

