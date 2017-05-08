# Höfundar Bjarki Þór Jónsson og Atli Óskarsson
# importar random og time
from random import *
import time
# Tekur Spil úr texta skjali og setur að handahófi í lista.
with open("spil2.txt","r") as spil:
    spilastokkur=spil.read().split("\n")
spil.close()
spilari=[]
tolva=[]
# Skiptir lista í tvent og setur í 2 lista
for x in spilastokkur:
    randomtala=randint(0,len(spilastokkur)-1)
    spilari.append(spilastokkur[randomtala])
    spilastokkur.remove(spilastokkur[randomtala])
    if len(spilari)==26:
        break
tolva=spilastokkur
strid=[]
teljari=0
# Spilið
while len(spilari)!=0 and len(tolva)!=0:
    # Tekur úr lista og setur það í lista
    spil=str(spilari[0])
    spil=spil.split(",")
    spil2=str(tolva[0])
    spil2=spil2.split(",")
    # Spilari gerir þegar 2 fer upp í teljara
    if teljari%2==0:
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
        # Spilari velur frá 1-8
        veldu=int(input("Veldu flokk "))
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])
        time.sleep(1)
    # Talvan gerir þegar 2 fer ekki upp í teljara
    if teljari%2!=0:
        print("tölvann dróg spilið",spil2[0],"1. Þyngd",spil2[1],"2. Mjólkurlagni dætra",spil2[2],"3. Einkunn ullar",spil2[3],"4. Fjöldi afkvæma",spil2[4],"5. Einkunn læris",spil2[5],"6. Frjósemi",spil2[6],"7. Gerð/þykkt bakvöðva",spil2[7],"8. Einkunn fyrir malir",spil2[8])
        randomtala=randint(1,8)
        time.sleep(1)
        # Talvan velur tölu frá 1-8 að handhófi
        print("Tölvann valdi ",randomtala)
        print("Þú drókst spilið",spil[0],"1. Þyngd",spil[1],"2. Mjólkurlagni dætra",spil[2],"3. Einkunn ullar",spil[3],"4. Fjöldi afkvæma",spil[4],"5. Einkunn læris",spil[5],"6. Frjósemi",spil[6],"7. Gerð/þykkt bakvöðva",spil[7],"8. Einkunn fyrir malir",spil[8])
        time.sleep(1)
    # Reiknar muninn á milli það sem talvan hefur og notandinn
    utkoma=float(spil[veldu])-float(spil2[veldu])
    # Ef útkoman er meiri en 0
    if utkoma>0:
        # setur spilin aftast í bunkan hjá notendanum
        print("Spilari vann")
        spilari.append(tolva[0])
        tolva.remove(tolva[0])
        spilari.append(spilari[0])
        spilari.remove(spilari[0])
        # Ef það eru spil í strid þá setur það í spilara listan.
        if len(strid)>0:
            for x in strid:
                spilari.append(x)
            # Tæmir lista
            strid=[]
    elif utkoma<0:
        print("Tolva vann")
        tolva.append(spilari[0])
        spilari.remove(spilari[0])
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        # Ef það eru spil í strid þá setur það í tölvu listan.
        if len(strid)>0:
            for x in strid:
                tolva.append(x)
            # Tæmir lista
            strid=[]
    # ef utkoman er 0 þá var jafntefli og er sett spilin í listan
    elif utkoma==0:
        print("Jafntefli")
        strid.append(tolva[0])
        tolva.remove(tolva[0])
        strid.append(spilari[0])
        spilari.remove(spilari[0])
    teljari+=1
    # Segir hve mikið hver er með
    print("Spilari er með", len(spilari), "talvan er með", len(tolva))
# Ef talvan er með 0 spil
if len(tolva)==0:
    print("Spilari vann spilið")
# Ef spilarinn er með 0 spil
if len(spilari)==0:
    print("Tolvan vann spilið")
