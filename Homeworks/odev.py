liste_tek = [1,3,5,7,9,11,15]
liste_cift = [0,2,4,6,8,10,12,14]

liste = liste_tek + liste_cift

liste2=[i*2 for i in liste]

for i in liste2:
    print("{} veri tipi: {}".format(i, type(i)))