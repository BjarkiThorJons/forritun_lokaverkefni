from random import *
with open("spil2.txt","r") as spil:
    spilastokkur=spil.read().split("\n")
spil.close()
spilastokkur.remove(spilastokkur[0])
for x in spilastokkur:
    print(x)
print(len(spilastokkur))
spilari=[]
tolva=[]
for x in spilastokkur:
    spilari.append(x)
    spilastokkur.remove(x)
    if len(spilari)==26:
        break
tolva=spilastokkur
print(spilari)
print(len(spilari))
print(spilastokkur)
print(len(spilastokkur))
print(tolva)
print(len(tolva))

while len(spilari)!=0 and len(tolva)!=0:
    teljari=





print("Done.")