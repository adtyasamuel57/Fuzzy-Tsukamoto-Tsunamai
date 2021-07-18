from fastapi import FastAPI
from antares_http import antares
import json
import requests

app = FastAPI()


@app.get('/tsukamoto/')
def show():

    antares.setDebug(False)
    antares.setAccessKey('935a0ba3ee50ed9c:c835eedd1ff34101')

    latestData = antares.get('NamiPostman', 'simulasiNami')
    print(latestData['content'])

    tg = latestData['content']["tg"]
    ka =latestData['content']["ka"]
    kg = latestData['content']["kg"]
    #Class Fuzzy
    tgg = float(tg)
    kaa = float(ka)
    kgg = float(kg)
    # input
    tinggiGelombang = tgg  # menggunakan satuan m
    kuatArus = kaa # Menggunakan satuan m/s
    kuatGempa= kgg # Menggunakan satuan ggal

    # define tinggiGelombang
    tinggiDangkal = 0
    tinggiSedang = 0
    tinggiTinggi = 0

    # define kuatArus
    arusLambat = 0
    arusSedang = 0 
    arusKuat = 0

    # define kuatGempa
    gempaPutih = 0
    gempaKuning = 0
    gempaHijau = 0
    gempaJingga = 0
    gempaMerah = 0

    # define Status
    status = 0
    statusAman = 0
    statusAwas = 0 
    statusBahaya = 0

        # define default role
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    z6 = 0
    z7 = 0
    z8 = 0
    z9 = 0
    z10 = 0
    z11 = 0
    z12 = 0
    z13 = 0
    z14 = 0
    z15 = 0
    z16 = 0
    z17 = 0
    z18 = 0
    z19 = 0
    z20 = 0
    z21 = 0
    z22 = 0
    z23 =0
    z24 = 0
    z25 = 0
    z26 = 0
    z27 = 0
    z28 = 0
    z29 = 0
    z30 = 0
    z31 = 0
    z32 = 0
    z33 = 0
    z34 = 0
    z35 = 0
    z36 = 0
    z37 = 0
    z38 = 0
    z39 = 0
    z40 = 0
    z41 = 0
    z42 = 0
    z43 = 0
    z44 = 0
    z45 = 0
    z46 = 0 
    z47 = 0
    z48 = 0
    z49 = 0
    z50 = 0
    z51 = 0
    z52 = 0
    z53 = 0
    z54 = 0
    z55 = 0
    z56 = 0 
    z57 = 0
    z58 = 0
    z59 = 0
    z60 = 0
    z61 = 0
    z62 = 0
    z63 = 0
    z64 = 0
    z65 = 0
    z66 = 0 
    z67 = 0
    z68 = 0
    z69 = 0
    z70 = 0
    z71 = 0
    z72 = 0
    z73 = 0
    z74 = 0
    z75 = 0
    z76 = 0 
    z77 = 0
    z78 = 0
    z79 = 0
    z80 = 0
    z81 = 0
    z82 = 0
    z83 = 0
    z84 = 0
    z85 = 0
    z86 = 0 
    z87 = 0
    z88 = 0
    z89 = 0
    z90 = 0
    z91 = 0
    z92 = 0
    z93 = 0
    z94 = 0
    z95 = 0
    z96 = 0 
    z97 = 0
    z98 = 0
    z99 = 0
    z100 = 0
    z101 = 0
    z102 = 0
    z103 = 0
    z104 = 0
    z105 = 0
    z106 = 0 
    z107 = 0
    z108 = 0
    z109 = 0
    z110 = 0
    z111 = 0
    z112 = 0
    z113 = 0
    z114 = 0
    z115 = 0
    z116 = 0 
    z117 = 0
    z118 = 0
    z119 = 0
    z120 = 0
    z121 = 0
    z122 = 0
    z123 = 0
    z124 = 0
    z125 = 0
    z126 = 0 
    z127 = 0
    z128 = 0
    z129 = 0
    z130 = 0
    z131 = 0
    z132 = 0
    z133 = 0
    z134 = 0
    z135 = 0
    
    
    # define real role
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0
    R7 = 0
    R8 = 0
    R9= 0
    R10 = 0
    R11 = 0
    R12 = 0
    R13 = 0
    R14 = 0
    R15 = 0
    R16 = 0
    R17 = 0
    R18 = 0
    R19 = 0
    R20 = 0
    R21 = 0
    R22 = 0
    R23 =0
    R24 = 0
    R25 = 0
    R26 = 0
    R27 = 0
    R28 = 0
    R29 = 0
    R30 = 0
    R31 = 0
    R32 = 0
    R33 = 0
    R34 = 0
    R35 = 0
    R36 = 0
    R37 = 0
    R38 = 0
    R39 = 0
    R40 = 0
    R41 = 0
    R42 = 0
    R43 = 0
    R44 = 0
    R45 = 0
    R46 = 0 
    R47 = 0
    R48 = 0
    R49 = 0
    R50 = 0
    R51 = 0
    R52 = 0
    R53 = 0
    R54 = 0
    R55 = 0
    R56 = 0 
    R57 = 0
    R58 = 0
    R59 = 0
    R60 = 0
    R61 = 0
    R62 = 0
    R63 = 0
    R64 = 0
    R65 = 0
    R66 = 0 
    R67 = 0
    R68 = 0
    R69 = 0
    R70 = 0
    R71 = 0
    R72 = 0
    R73 = 0
    R74 = 0
    R75 = 0
    R76 = 0 
    R77 = 0
    R78 = 0
    R79 = 0
    R80 = 0
    R81 = 0
    R82 = 0
    R83 = 0
    R84 = 0
    R85 = 0
    R86 = 0 
    R87 = 0
    R88 = 0
    R89 = 0
    R90 = 0
    R91 = 0
    R92 = 0
    R93 = 0
    R94 = 0
    R95 = 0
    R96 = 0 
    R97 = 0
    R98 = 0
    R99 = 0
    R100 = 0
    R101 = 0
    R102 = 0
    R103 = 0
    R104 = 0
    R105 = 0
    R106 = 0 
    R107 = 0
    R108 = 0
    R109 = 0
    R110 = 0
    R111 = 0
    R112 = 0
    R113 = 0
    R114 = 0
    R115 = 0
    R116 = 0 
    R117 = 0
    R118 = 0
    R119 = 0
    R120 = 0
    R121 = 0
    R122 = 0
    R123 = 0
    R124 = 0
    R125 = 0
    R126 = 0 
    R127 = 0
    R128 = 0
    R129 = 0
    R130 = 0
    R131 = 0
    R132 = 0
    R133 = 0
    R134 = 0
    R135 = 0


    # others
    total_RiZi = 0
    total_R = 0
    nilai_z = 0
    angka = 0


    # Jika Gelombang Dangkal
    if tinggiGelombang <= 1.5:
        tinggiDangkal = 1
    elif 1.5 < tinggiGelombang <= 2:
        tinggiDangkal = (1.5-tinggiGelombang) / (2 - 1.5)
    else:
        tinggiDangkal = 0

    # Jika Gelombang Sedang
    if 1.75 <= tinggiGelombang <= 2.25:
        tinggiSedang = (tinggiGelombang-1.75)/(2.25-1.75)
    elif 2.25 < tinggiGelombang <= 3.5:
        tinggiSedang = 1
    elif 3.5 < tinggiGelombang < 4:
        tinggiSedang = (4 - tinggiSedang) / (4 - 3.5)
    else:
        tinggiSedang = 0

    # Jika Gelombang Tinggi 
    if tinggiGelombang < 3.75:
        tinggiTinggi = 0
    elif 3.75 <= tinggiGelombang <= 4.25:
        tinggiTinggi = (tinggiGelombang-3.75)/(4.25-3.75)
    else:
        tinggiTinggi = 1


    # Jika Arus Lambat
    if kuatArus <= 3:
        arusLambat = 1
    elif 3 < kuatArus <= 5.5:
        arusLambat = (10 - kuatArus) / (10 - 6)
    else:
        arusLambat = 0

    # Jika Arus Sedang
    if 4<= kuatArus < 6:
        arusSedang = (kuatArus-4) / (6-4)
    elif 6 <=  kuatArus <= 10:
        arusSedang = 1
    elif 10 < kuatArus <= 13:
        arusSedang = (13-kuatArus)/(13-10)
    else:
        arusSedang = 0

    #Jika Arus Cepat
    if kuatArus < 11:
        arusKuat = 0
    elif 11 <= kuatArus <= 14:
        arusKuat = (kuatArus-11)/(14-11)
    else:
        arusKuat = 1

    #Jika Gempa Berwarna Putih 
    if kuatGempa <= 2.8:
        gempaPutih = 1
    elif 2.8< kuatGempa<= 2.9 :
        gempaPutih = (2.9-kuatGempa)/(2.9-2.8)
    else :
        gempaPutih = 0

    # Jika Gempa Berwarna Hijau 
    if 2.8 < kuatGempa <= 2.9 :
        gempaHijau = (kuatGempa-2.8)/(2.9-2.8)
    elif 2.9 <= kuatGempa <= 88:
        gempaHijau = 1
    elif 88 <= kuatGempa <= 89:
        gempaHijau = (89-kuatGempa)/(89-88)
    else:
        gempaHijau = 0

    #Jika Gempa Berwarna Kuning
    if 88 <= kuatGempa <= 89:
        gempaKuning = (kuatGempa-88)/(89-88)
    elif 89 <= kuatGempa <= 167:
        gempaKuning = 1
    elif 167 <= kuatGempa <= 168:
        gempaKuning = (168-kuatGempa)/(168-167)
    else:
        gempaKuning = 0

    #Jika Gempa Berwarna Jingga 
    if 167 <= kuatGempa <= 168:
        gempaJingga = (kuatGempa-167)/(168-167)
    elif 168 <= kuatGempa <= 564:
        gempaJingga = 1
    elif 564 <= kuatGempa <= 565 :
        gempaJingga = (565-kuatGempa)/(565-564)
    else:
        gempaJingga = 0

    #Jika Gempa Berwarna Merah 
    if kuatGempa < 564 :
        gempaMerah = 0
    elif 564 <= kuatGempa <= 565:
        gempaMerah = (kuatGempa-564)/(565-564)
    else:
        gempaMerah = 1  

    #Menghitung Rule
    R1 = min(tinggiDangkal,arusLambat,gempaPutih)
    z1 = 34 - R1

    R2 = min(tinggiDangkal,arusLambat,gempaPutih)
    z2 = R2 + 33

    R3 = min(tinggiDangkal,arusLambat,gempaPutih)
    z3 = 67 - R3

    R4 = min(tinggiDangkal,arusLambat,gempaHijau)
    z4 = 34 - R4

    R5 = min(tinggiDangkal,arusLambat,gempaHijau)
    z5 = 33 + R5

    R6 = min(tinggiDangkal,arusLambat,gempaHijau)
    z6 = 67 - R6

    R7 = min(tinggiDangkal,arusLambat,gempaKuning)
    z7 = 34 - R7

    R8 = min(tinggiDangkal,arusLambat,gempaKuning)
    z8 = R8 + 33

    R9 = min(tinggiDangkal,arusLambat,gempaKuning)
    z9 = 67 - R9

    R10 = min(tinggiDangkal,arusLambat,gempaJingga)
    z10 = 34 - R10

    R11 = min(tinggiDangkal,arusLambat,gempaJingga)
    z11 = R11 + 33

    R12 = min(tinggiDangkal,arusLambat,gempaJingga)
    z12 = 67 - R12

    R13 = min(tinggiDangkal,arusLambat,gempaMerah)
    z13 = 34 - R13

    R14 = min(tinggiDangkal,arusLambat,gempaMerah)
    z14 = R14 + 33

    R15 = min(tinggiDangkal,arusLambat,gempaMerah)
    z15 = 67 - R15

    R16 = min(tinggiDangkal,arusSedang,gempaPutih)
    z16 = 34 - R16

    R17 = min(tinggiDangkal,arusSedang,gempaPutih)
    z17 = R17 + 33

    R18 = min(tinggiDangkal,arusSedang,gempaPutih)
    z18 = 67 - R18

    R19 = min(tinggiDangkal,arusSedang,gempaHijau)
    z19 = 34 - R19

    R20 = min(tinggiDangkal,arusSedang,gempaHijau)
    z20 = R20 + 33

    R21 = min(tinggiDangkal,arusSedang,gempaHijau)
    z21 = 67 - R21

    R22 = min(tinggiDangkal,arusSedang,gempaKuning)
    z22 = 34 - R22

    R23 = min(tinggiDangkal,arusSedang,gempaKuning)
    z23 = R23 + 33

    R24 = min(tinggiDangkal,arusSedang,gempaKuning)
    z24 = 67 - R24

    R25 = min(tinggiDangkal,arusSedang,gempaJingga)
    z25 = 34 - R25

    R26 = min(tinggiDangkal,arusSedang,gempaJingga)
    z26 = R26 + 33

    R27 = min(tinggiDangkal,arusSedang,gempaJingga)
    z27 = 67 - R27

    R28 = min(tinggiDangkal,arusSedang,gempaMerah)
    z28 = 34 - R28

    R29 = min(tinggiDangkal,arusSedang,gempaMerah)
    z29 = R29 + 33

    R30 = min(tinggiDangkal,arusSedang,gempaMerah)
    z30 = 67 - R30

    R31 = min(tinggiDangkal,arusKuat,gempaPutih)
    z31 = 34 - R31

    R32 = min(tinggiDangkal,arusKuat,gempaPutih)
    z32 = R32 + 33

    R33 = min(tinggiDangkal,arusKuat,gempaPutih)
    z33 = 67 - R33

    R34 = min(tinggiDangkal,arusKuat,gempaHijau)
    z34 = 34 - R34

    R35 = min(tinggiDangkal,arusKuat,gempaHijau)
    z35 = R35 + 33

    R36 = min(tinggiDangkal,arusKuat,gempaHijau)
    z36 = 67 - R36

    R37 = min(tinggiDangkal,arusKuat,gempaKuning)
    z37 = 34 - R37

    R38 = min(tinggiDangkal,arusKuat,gempaKuning)
    z38 = R38 + 33

    R39 = min(tinggiDangkal,arusKuat,gempaKuning)
    z39 = 67 - R39

    R40 = min(tinggiDangkal,arusKuat,gempaJingga)
    z40 = 34 - R40

    R41 = min(tinggiDangkal,arusKuat,gempaJingga)
    z41 = R41 + 33

    R42 = min(tinggiDangkal,arusKuat,gempaJingga)
    z42 = 67 - R42

    R43 = min(tinggiDangkal,arusKuat,gempaMerah)
    z43 = 34 - R43

    R44 = min(tinggiDangkal,arusKuat,gempaMerah)
    z44 = R44 + 33

    R45 = min(tinggiDangkal,arusKuat,gempaMerah)
    z45 = 67 - R45

    R46 = min(tinggiSedang,arusLambat,gempaPutih)
    z46 = 34 - R46

    R47 = min(tinggiSedang,arusLambat,gempaPutih)
    z47 = R47 + 33

    R48 = min(tinggiSedang,arusLambat,gempaPutih)
    z48 = 67 - R48

    R49= min(tinggiSedang,arusLambat,gempaHijau)
    z49 = 34 - R49

    R50 = min(tinggiSedang,arusLambat,gempaHijau)
    z50 = R50 + 33

    R51 = min(tinggiSedang,arusLambat,gempaHijau)
    z51 = 67 - R51

    R52= min(tinggiSedang,arusLambat,gempaKuning)
    z52 = 34 - R52

    R53 = min(tinggiSedang,arusLambat,gempaKuning)
    z53 = R53 + 33

    R54 = min(tinggiSedang,arusLambat,gempaKuning)
    z54 = 67 - R54

    R55= min(tinggiSedang,arusLambat,gempaJingga)
    z55 = 34 - R55

    R56 = min(tinggiSedang,arusLambat,gempaJingga)
    z56 = R56 + 33

    R57 = min(tinggiSedang,arusLambat,gempaJingga)
    z57 = 67 - R57

    R58= min(tinggiSedang,arusLambat,gempaMerah)
    z58 = 34 - R58

    R59 = min(tinggiSedang,arusLambat,gempaMerah)
    z59 = R59 + 33

    R60 = min(tinggiSedang,arusLambat,gempaMerah)
    z60 = 67 - R60

    R61= min(tinggiSedang,arusSedang,gempaPutih)
    z61 = 34 - R61

    R62 = min(tinggiSedang,arusSedang,gempaPutih)
    z62 = R62 + 33

    R63 = min(tinggiSedang,arusSedang,gempaPutih)
    z63 = 67 - R63

    R64= min(tinggiSedang,arusSedang,gempaHijau)
    z64 = 34 - R64

    R65 = min(tinggiSedang,arusSedang,gempaHijau)
    z65 = R65 + 33

    R66 = min(tinggiSedang,arusSedang,gempaHijau)
    z66 = 67 - R66

    R67= min(tinggiSedang,arusSedang,gempaKuning)
    z67 = 34 - R67

    R68 = min(tinggiSedang,arusSedang,gempaKuning)
    z68 = R68 + 33

    R69 = min(tinggiSedang,arusSedang,gempaKuning)
    z69 = 67 - R69

    R70= min(tinggiSedang,arusSedang,gempaJingga)
    z70 = 34 - R70

    R71 = min(tinggiSedang,arusSedang,gempaJingga)
    z71 = R71 + 33

    R72 = min(tinggiSedang,arusSedang,gempaJingga)
    z72 = 67 - R72

    R73= min(tinggiSedang,arusSedang,gempaMerah)
    z73 = 34 - R73

    R74 = min(tinggiSedang,arusSedang,gempaMerah)
    z74 = R74 + 33

    R75 = min(tinggiSedang,arusSedang,gempaMerah)
    z75 = 67 - R75

    R76= min(tinggiSedang,arusKuat,gempaPutih)
    z76 = 34 - R76

    R77 = min(tinggiSedang,arusKuat,gempaPutih)
    z77 = R77 + 33

    R78 = min(tinggiSedang,arusKuat,gempaPutih)
    z78 = 67 - R78

    R79= min(tinggiSedang,arusKuat,gempaHijau)
    z79 = 34 - R79

    R80 = min(tinggiSedang,arusKuat,gempaHijau)
    z80 = R80 + 33

    R81 = min(tinggiSedang,arusKuat,gempaHijau)
    z81 = 67 - R81

    R82= min(tinggiSedang,arusKuat,gempaKuning)
    z82 = 34 - R82

    R83 = min(tinggiSedang,arusKuat,gempaKuning)
    z83 = R83 + 33

    R84 = min(tinggiSedang,arusKuat,gempaKuning)
    z84 = 67 - R84

    R85= min(tinggiSedang,arusKuat,gempaJingga)
    z85 = 34 - R85

    R86 = min(tinggiSedang,arusKuat,gempaJingga)
    z86 = R86 + 33

    R87 = min(tinggiSedang,arusKuat,gempaJingga)
    z87 = 67 - R87

    R88= min(tinggiSedang,arusKuat,gempaMerah)
    z88 = 34 - R88

    R89 = min(tinggiSedang,arusKuat,gempaMerah)
    z89 = R89 + 33

    R90 = min(tinggiSedang,arusKuat,gempaMerah)
    z90 = 67 - R90

    R91= min(tinggiTinggi,arusLambat,gempaPutih)
    z91 = 34 - R91

    R92 = min(tinggiTinggi,arusLambat,gempaPutih)
    z92 = R92 + 33

    R93 = min(tinggiTinggi,arusLambat,gempaPutih)
    z93 = 67 - R93

    R94= min(tinggiTinggi,arusLambat,gempaHijau)
    z94 = 34 - R94

    R95 = min(tinggiTinggi,arusLambat,gempaHijau)
    z95 = R95 + 33

    R96 = min(tinggiTinggi,arusLambat,gempaHijau)
    z96 = 67 - R96

    R97= min(tinggiTinggi,arusLambat,gempaKuning)
    z97 = 34 - R97

    R98 = min(tinggiTinggi,arusLambat,gempaKuning)
    z98 = R98 + 33

    R99 = min(tinggiTinggi,arusLambat,gempaKuning)
    z99 = 67 - R99

    R100= min(tinggiTinggi,arusLambat,gempaJingga)
    z100 = 34 - R100

    R101 = min(tinggiTinggi,arusLambat,gempaJingga)
    z101 = R101 + 33

    R102 = min(tinggiTinggi,arusLambat,gempaJingga)
    z102 = 67 - R102

    R103= min(tinggiTinggi,arusLambat,gempaMerah)
    z103 = 34 - R103

    R104 = min(tinggiTinggi,arusLambat,gempaMerah)
    z104 = R104 + 33

    R105 = min(tinggiTinggi,arusLambat,gempaMerah)
    z105 = 67 - R105

    R106= min(tinggiTinggi,arusSedang,gempaPutih)
    z106 = 34 - R106

    R107 = min(tinggiTinggi,arusSedang,gempaPutih)
    z107 = R107 + 33

    R108 = min(tinggiTinggi,arusSedang,gempaPutih)
    z108 = 67 - R108

    R109= min(tinggiTinggi,arusSedang,gempaHijau)
    z109 = 34 - R109

    R110 = min(tinggiTinggi,arusSedang,gempaHijau)
    z110 = R110 + 33

    R111 = min(tinggiTinggi,arusSedang,gempaHijau)
    z111 = 67 - R111

    R112= min(tinggiTinggi,arusSedang,gempaKuning)
    z112 = 34 - R112

    R113 = min(tinggiTinggi,arusSedang,gempaKuning)
    z113 = R113 + 33

    R114 = min(tinggiTinggi,arusSedang,gempaKuning)
    z114 = 67 - R114

    R115= min(tinggiTinggi,arusSedang,gempaJingga)
    z115 = 34 - R115

    R116 = min(tinggiTinggi,arusSedang,gempaJingga)
    z116 = R116 + 33

    R117 = min(tinggiTinggi,arusSedang,gempaJingga)
    z117 = 67 - R117

    R118= min(tinggiTinggi,arusSedang,gempaMerah)
    z118 = 34 - R118

    R119 = min(tinggiTinggi,arusSedang,gempaMerah)
    z119 = R119 + 33

    R120 = min(tinggiTinggi,arusSedang,gempaMerah)
    z120 = 67 - R120

    R121= min(tinggiTinggi,arusKuat,gempaPutih)
    z121 = 34 - R121

    R122 = min(tinggiTinggi,arusKuat,gempaPutih)
    z122 = R122 + 33

    R123 = min(tinggiTinggi,arusKuat,gempaPutih)
    z123 = 67 - R123

    R124= min(tinggiTinggi,arusKuat,gempaHijau)
    z124 = 34 - R124

    R125 = min(tinggiTinggi,arusKuat,gempaHijau)
    z125 = R125 + 33

    R126 = min(tinggiTinggi,arusKuat,gempaHijau)
    z126 = 67 - R126

    R127= min(tinggiTinggi,arusKuat,gempaKuning)
    z127 = 34 - R127

    R128 = min(tinggiTinggi,arusKuat,gempaKuning)
    z128 = R128 + 33

    R129 = min(tinggiTinggi,arusKuat,gempaKuning)
    z129 = 67 - R129

    R130= min(tinggiTinggi,arusKuat,gempaJingga)
    z130 = 34 - R130

    R131 = min(tinggiTinggi,arusKuat,gempaJingga)
    z131 = R131 + 33

    R132 = min(tinggiTinggi,arusKuat,gempaJingga)
    z132 = 67 - R132

    R133= min(tinggiTinggi,arusKuat,gempaMerah)
    z133 = 34 - R133

    R134 = min(tinggiTinggi,arusKuat,gempaMerah)
    z134 = R134 + 33

    R135 = min(tinggiTinggi,arusKuat,gempaMerah)
    z135 = 67 - R135



    # Menghitung nilai STATUS
    # Menjumlahkan (Ri) dan (Zi)
    total_RiZi = (R1 * z1) + (R2 * z2) + (R3 * z3) + (R4 * z4) + (R5 * z5) + (R6 * z6) + (R7*z7) + (R8*z8) + (R9*z9) + (R10*z10)+(R1 * z11) + (R12 * z12) + (R13 * z13) + (R14 * z14) + (R15 * z15) + (R16 * z16) + (R17*z17) + (R18*z18) + (R19*z19) + (R20*z20) + (R21 * z21) + (R22 * z22) + (R23 * z23) + (R24 * z24) + (R25 * z25) + (R26 * z26) + (R27*z27) + (R28*z28) + (R29*z29) + (R30*z30) + (R31 * z31) + (R32 * z32) + (R33 * z33) + (R34 * z34) + (R35 * z35) + (R36 * z36) + (R37*z37) + (R38*z38) + (R39*z39) + (R40*z40)+ (R41 * z41) + (R42 * z42) + (R43 * z43) + (R44 * z44) + (R45 * z45) + (R46 * z46) + (R47 * z47) + (R48 * z48) + (R49 * z49) + (R50 * z50) +(R51 * z51) + (R52 * z52) + (R53 * z53) + (R54 * z54) + (R55 * z55) + (R56 * z56) + (R57 * z57) + (R58 * z58) + (R59 * z59) + (R60 * z60) + (R61 * z61) + (R62 * z62) + (R63 * z63) + (R64 * z64) + (R65 * z65) + (R66 * z66) + (R67 * z67) + (R68 * z68) + (R69 * z69) + (R70 * z70) + (R71 * z71) + (R72 * z72) + (R73 * z73) + (R74 * z74) + (R75 * z75) + (R76 * z76) + (R77 * z77) + (R78 * z78) + (R79 * z79) + (R80 * z80) + (R81 * z81) + (R82 * z82) + (R83 * z83) + (R84 * z84) + (R85 * z85) + (R86 * z86) + (R87 * z87) + (R88 * z88) + (R89 * z89) + (R90 * z90) + (R91 * z91) + (R92 * z92) + (R93 * z93) + (R94 * z94) + (R95 * z95) + (R96 * z96) + (R97 * z97) + (R98 * z98) + (R99 * z99) + (R100 * z100) + (R101 * z101) + (R102 * z102) + (R103 * z103) + (R104 * z104) + (R105 * z105) + (R106 * z106) + (R107 * z107) + (R108 * z108) + (R109 * z109) + (R110 * z110) + (R111 * z111) + (R112 * z112) + (R113 * z113) + (R114 * z114) + (R115 * z115) + (R116 * z116) + (R117 * z117) + (R118 * z118) + (R119 * z119) + (R120 * z120) + (R121 * z121) + (R122 * z122) + (R123 * z123) + (R124 * z124) + (R125 * z125) + (R126 * z126) + (R127 * z127) + (R128 * z128) + (R129 * z129) + (R130 * z130) + (R131 * z131) + (R132 * z132) + (R133 * z133) + (R134 * z134) + (R135 * z135)  

    # Menjumlahkan seluruh (Ri)
    total_R = R1 + R2 + R3 + R4 + R5 + R6 + R7 +R8 + R9+ R10 +R11+R12+R13+R14+R15+R16+R17+R18+R19+R20+R21+R22+R23+R24+R25+R26+R27+R28+R29+R30+R31+R32+R33+R34+R35+R36+R37+R38+R39+R40+R41+R42+R43+R44+R45+R46+R47+R48+R49+R50+R51+R52+R53+R54+R55+R56+R57+R58+R59+R60+R61+R62+R63+R64+R65+R66+R67+R68+R69+R70+R71+R72+R73+R74+R75+R76+R77+R78+R79+R80+R81+R82+R83+R84+R85+R86+R87+R88+R89+R90+R91+R92+R93+R94+R95+R96+R97+R98+R99+R100+R101+R102+R103+R104+R105+R106+R107+R108+R109+R110+R111+R112+R113+R114+R115+R116+R117+R118+R119+R120+R121+R122+R123+R124+R125+R126+R127+R128+R129+R130+R131+R132+R133+R134+R135

    # Mendapatkan nilai_z / total bonus
    nilai_z = total_RiZi / total_R
   
    status = nilai_z
    #Jika Status Aman
    if status <= 33:
        statusAman = 1
    elif 33<= status < 34:
        statusAman = (34-status) / (34-33)
    else:
        statusAman = 0 

    #Jika Status Awas
    if 33< status <= 34:
        statusAwas = (status-33)/(34-33)
    elif 34 <= status <= 66:
        statusAwas = 1
    elif 66 <= status <67 :
        statusAwas = (67- status)/(67-66)
    else:
        statusAwas = 0

    #Jika Status Bahaya
    if status < 66 :
        statusBahaya = 0
    elif 66 < status <= 67:
        statusBahaya = (status-66)/(67-66)
    else:
        statusBahaya = 1




    #Display Tinggi Gelombang
    if tinggiDangkal != 0:
        msg = "Dangkal ({})".format("%.2f" % tinggiDangkal)
        print('Tinggi Gelombang = ', msg)
    elif tinggiSedang != 0:
        msg = "Sedang ({})".format("%.2f" % tinggiSedang)
        print('Tinggi Gelombang = ', msg)
    elif tinggiTinggi != 0:
        msg = "Tinggi ({})".format("%.2f" % tinggiTinggi)
        print('Tinggi Gelombang = ', msg)

    #Display Kuat Arus
    if arusLambat != 0:
        msg = "Lambat ({})".format("%.2f" % arusLambat)
        print('Kecepatan Arus = ', msg)
    elif arusSedang != 0:
        msg = "Sedang ({})".format("%.2f" % arusSedang)
        print('Kecepatan Arus = ', msg)
    elif arusKuat != 0:
        msg = "Kuat ({})".format("%.2f" % arusKuat)
        print('Kecepatan Arus = ', msg)

    #Display Gempa

    if gempaPutih != 0:
        msg = "Putih ({})".format("%.2f" % gempaPutih)
        print('Kekuatan Gempa = ', msg)
    elif gempaHijau != 0:
        msg = "Hijau ({})".format("%.2f" % gempaHijau)
        print('Kekuatan Gempa = ', msg)
    elif gempaKuning != 0:
        msg = "Kuning ({})".format("%.2f" % gempaKuning)
        print('Kekuatan Gempa = ', msg)
    elif gempaJingga != 0:
        msg = "Jingga ({})".format("%.2f" % gempaJingga)
        print('Kekuatan Gempa = ', msg)
    elif gempaMerah != 0:
        msg = "merah ({})".format("%.2f" % gempaMerah)
        print('Kekuatan Gempa = ', msg)

    # Display Status
    if statusAman != 0:
        msg = "Aman ({})".format("%.2f" % statusAman)
        print('Status = ', msg)
        respon = "aman"
    elif statusAwas != 0:
        msg = "Awas ({})".format("%.2f" % statusAwas)
        print('Status = ', msg)
        respon = "awas"
    elif statusBahaya != 0:
        msg = "Bahaya ({})".format("%.2f" % statusBahaya)
        print('Status = ', msg)
        respon = "bahaya"
    
    return respon