#LIST

#        0        1        2
food=["hotdogs","ham","chicken"]

#ichange niya ang naa sa 0 na index
food[0]="pizza"

#print(food[0])

#mag add siyag item sa pinaka last 
food.append("ice cream")

#remove
food.remove("pizza")

#remove last
food.pop()

#insert kung unsa imo iinsert
food.insert(0,"cake")

#isort niya by letter
food.sort()

#also clear i empty niya naa sa list 
food.clear()



for x in food:
    print(x)


