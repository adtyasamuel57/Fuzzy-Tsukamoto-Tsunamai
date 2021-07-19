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

    R2 = min(tinggiDangkal,arusLambat,gempaHijau)
    z2 = 34 - R2

    R3 = min(tinggiDangkal,arusLambat,gempaKuning)
    z3 = R3 + 33

    R4 = min(tinggiDangkal,arusLambat,gempaJingga)
    z4 = R4 + 33

    R5 = min(tinggiDangkal,arusLambat,gempaMerah)
    z5 = R5 + 66

    R6 = min(tinggiDangkal,arusSedang,gempaPutih)
    z6 = 34 - R6

    R7 = min(tinggiDangkal,arusSedang,gempaHijau)
    z7 = R7 + 33

    R8 = min(tinggiDangkal,arusSedang,gempaKuning)
    z8 = R8 + 33

    R9 = min(tinggiDangkal,arusSedang,gempaJingga)
    z9 = R9 + 66

    R10 = min(tinggiDangkal,arusSedang,gempaMerah)
    z10 = R10 + 66

    R11 = min(tinggiDangkal,arusKuat,gempaPutih)
    z11 = 34 - R11

    R12 = min(tinggiDangkal,arusKuat,gempaHijau)
    z12 = R12 + 33

    R13 = min(tinggiDangkal,arusKuat,gempaKuning)
    z13 = R13 + 66

    R14 = min(tinggiDangkal,arusKuat,gempaJingga)
    z14 = R14 + 66 

    R15 = min(tinggiDangkal,arusKuat,gempaMerah)
    z15 = R15 + 66

    R16 = min(tinggiSedang,arusLambat,gempaPutih)
    z16 = 34 - R16

    R17 = min(tinggiSedang,arusLambat,gempaHijau)
    z17 = 34 - R17 

    R18 = min(tinggiSedang,arusLambat,gempaKuning)
    z18 = R18 + 33

    R19 = min(tinggiSedang,arusLambat,gempaJingga)
    z19 = R19 + 33

    R20 = min(tinggiSedang,arusLambat,gempaMerah)
    z20 = R20 + 66

    R21 = min(tinggiSedang,arusSedang,gempaPutih)
    z21 = 34 - R21

    R22 = min(tinggiSedang,arusSedang,gempaHijau)
    z22 = R22 + 33

    R23 = min(tinggiSedang,arusSedang,gempaKuning)
    z23 = R23 + 33

    R24 = min(tinggiSedang,arusSedang,gempaJingga)
    z24 = R24 + 33

    R25 = min(tinggiSedang,arusSedang,gempaMerah)
    z25 = R25 + 33

    R26 = min(tinggiSedang,arusKuat,gempaPutih)
    z26 = 34 - R26 

    R27 = min(tinggiSedang,arusKuat,gempaHijau)
    z27 = 34 - R27

    R28 = min(tinggiSedang,arusKuat,gempaKuning)
    z28 = 34 - R28

    R29 = min(tinggiSedang,arusKuat,gempaJingga)
    z29 = R29 + 33

    R30 = min(tinggiSedang,arusKuat,gempaMerah)
    z30 = R30 + 33

    R31 = min(tinggiTinggi,arusLambat,gempaPutih)
    z31 = 34 - R31

    R32 = min(tinggiTinggi,arusLambat,gempaHijau)
    z32 = 34 - R32 

    R33 = min(tinggiTinggi,arusLambat,gempaKuning)
    z33 = 34 - R33

    R34 = min(tinggiTinggi,arusLambat,gempaJingga)
    z34 = 34 - R34

    R35 = min(tinggiTinggi,arusLambat,gempaMerah)
    z35 = R35 + 33

    R36 = min(tinggiTinggi,arusSedang,gempaPutih)
    z36 = 34 - R36

    R37 = min(tinggiTinggi,arusSedang,gempaHijau)
    z37 = 34 - R37

    R38 = min(tinggiTinggi,arusSedang,gempaKuning)
    z38 = 34 - R38

    R39 = min(tinggiTinggi,arusSedang,gempaJingga)
    z39 = 34 - R39

    R40 = min(tinggiTinggi,arusSedang,gempaMerah)
    z40 = R40 + 33

    R41 = min(tinggiTinggi,arusKuat,gempaPutih)
    z41 = 34 - R41

    R42 = min(tinggiTinggi,arusKuat,gempaHijau)
    z42 = 34 - R42

    R43 = min(tinggiTinggi,arusKuat,gempaKuning)
    z43 = R43 + 33

    R44 = min(tinggiTinggi,arusKuat,gempaJingga)
    z44 = R44 + 33

    R45 = min(tinggiTinggi,arusKuat,gempaMerah)
    z45 = R45 + 33


    # Menghitung nilai STATUS
    # Menjumlahkan (Ri) dan (Zi)
    total_RiZi = (R1 * z1) + (R2 * z2) + (R3 * z3) + (R4 * z4) + (R5 * z5) + (R6 * z6) + (R7*z7) + (R8*z8) + (R9*z9) + (R10*z10)+(R1 * z11) + (R12 * z12) + (R13 * z13) + (R14 * z14) + (R15 * z15) + (R16 * z16) + (R17*z17) + (R18*z18) + (R19*z19) + (R20*z20) + (R21 * z21) + (R22 * z22) + (R23 * z23) + (R24 * z24) + (R25 * z25) + (R26 * z26) + (R27*z27) + (R28*z28) + (R29*z29) + (R30*z30) + (R31 * z31) + (R32 * z32) + (R33 * z33) + (R34 * z34) + (R35 * z35) + (R36 * z36) + (R37*z37) + (R38*z38) + (R39*z39) + (R40*z40)+ (R41 * z41) + (R42 * z42) + (R43 * z43) + (R44 * z44) + (R45 * z45) 

    # Menjumlahkan seluruh (Ri)
    total_R = R1 + R2 + R3 + R4 + R5 + R6 + R7 +R8 + R9+ R10 +R11+R12+R13+R14+R15+R16+R17+R18+R19+R20+R21+R22+R23+R24+R25+R26+R27+R28+R29+R30+R31+R32+R33+R34+R35+R36+R37+R38+R39+R40+R41+R42+R43+R44+R45

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