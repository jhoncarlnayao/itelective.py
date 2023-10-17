#DICTIONARY 


capitals = {"USA":"WASHINGTON DC",
            "INDIA":"NEW DEHLI",
            "CHINA":"BEIJING",
            "RUSSIA":"MOSCOW"}

#here kay mag add siya og new country and capital
capitals.update({"GERMANY":"BERLIN"})


#ilisan niya ang capital sa USA
capitals.update({"USA":"LAS VEGAS"})

#iremove niya ang china
capitals.pop("CHINA")

#clear list/dictionary
capitals.clear()




print(capitals["RUSSIA"])

#so here pag wala sa list imong gina pangita mo print siya og "NONE"
#much safer way aron dimag print og error
print(capitals.get("GERMANY"))

#diri kay ipang print nilang niya ang country so ang country man sa atoa list kay
#usa , india, china and russia
print(capitals.keys())

#diri nga part kay i print niya ang capital ana nga country which is 
# washington dc, new dehli, beijing and moscow
print(capitals.values())

#so here kay i print naniya tanan ang naa saimo list or dictionary 
# COUNTRY : CAPITAL
print(capitals.items())


for key,value in capitals.items():
    print(key,value)