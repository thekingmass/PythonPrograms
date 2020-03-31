name=input("Please input your name\n")
i=0
print ("your name is", len(name), "characters long")
for i in range(len(name)):
    print(name[i],".", end=" ")
