with open("spil2.txt","r") as spil:
    listi=spil.read().split("\n")

listi2=[]
for x in listi:
    listi2.append(x)
    print(x)
print(listi2)