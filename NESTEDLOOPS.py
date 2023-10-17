#NESTED LOOPS

rows =int(input("HOW MANY ROWS?: "))
column =int(input("HOW MANY COLUMNS?: "))
symbol =input("ENTER SYMBOL: ")

for i in range(rows):
    for j in range(column):
        print(symbol,end=" ")
    print()