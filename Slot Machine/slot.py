import random

MAX_YATIRMA = 10000
MİN_YATIRMA = 100

SATIR = 5
SÜTUN = 3

sembol_sayısı = {
    "+": 6, 
    "*": 5,
    "!": 4,
    "%": 3
}

sembol_değerleri = {
    "+": 2,
    "*": 3,
    "!": 4,
    "%": 10
}

def kazanma_şartları(sütunlar, satırlar, iddaa, değerler):
    kazanmalar = 0
    kazanan_satırlar = []
    for satır in range(satırlar):
        sembol = sütunlar[0][satır]
        for sütun in sütunlar:
            kontrol_sembol = sütun[satır]
            if sembol != kontrol_sembol:
                break
        else:
            kazanmalar += değerler[sembol] * iddaa
            kazanan_satırlar.append(satır + 1)

    return kazanmalar, kazanan_satırlar



def slot_makinesi_çevir(sat, süt, semboller):
    bütün_semboller = []
    for sembol, sembol_sayısı in semboller.items():
        for _ in range(sembol_sayısı):
            bütün_semboller.append(sembol)
        
    sütunlar = []
    for _ in range(süt):
        sütun = []
        anlık_semboller = bütün_semboller[:]
        for _ in range(sat):
            değer = random.choice(anlık_semboller)
            anlık_semboller.remove(değer)
            sütun.append(değer)

        sütunlar.append(sütun)

    return sütunlar      


def slot_makinesi(sütunlar):
    for satır in range(len(sütunlar[0])):
        for i, sütun in enumerate(sütunlar):
            if i != len(sütunlar) - 1:
                print(sütun[satır], end=" | ")
            else:
                print(sütun[satır], end="")

        print()


def yatırma():
    global basla
    while True:
        basla = int(input("Kaç TL yatırmak istersiniz?(100-1000): "))
        if basla < MİN_YATIRMA or basla > MAX_YATIRMA:
            print("Lütfen belirtilen aralıkta bir miktar giriniz!")
        else:
            break

    return basla



def satırlar():
    global satır_sayısı
    while True:
        satır_sayısı = int(input("Kaç satır oynamak istersiniz?(1-5): "))
        
        if satır_sayısı > 5 or satır_sayısı < 1:
            print("Lütfen belirtilen aralıkta satır sayısı giriniz!")
        else:
            break

    return satır_sayısı


def bahis1():
    while True:
        bahis_miktarı = int(input("Var olan miktarın kaçıyla bahis oynamak istersin?: "))
        if bahis_miktarı > miktar:
            print(f"Lütfen geçerli bir miktar giriniz! Şuan geçerli bakiyeniz {miktar}")
        elif miktar < bahis_miktarı:
            print(f"Kasadaki paradan daha fazla bir miktarla oynayamazsınız. Kasada toplam {miktar}TL var.")
        else:
            break
    
    return bahis_miktarı

def döndür(miktar):
    satır = satırlar()
    bahis = bahis1()
    geriye_kalan = miktar - bahis
    print(f"Şu anda {bahis} kadar parayla {satır} satıra oynuyorsun. Kasada geriye {geriye_kalan} kadar paran kaldı.")
    slotlar = slot_makinesi_çevir(SATIR, SÜTUN, sembol_sayısı)
    slot_makinesi(slotlar)
    kazanmalar, kazanan_satırlar = kazanma_şartları(slotlar, satır, bahis, sembol_değerleri)
    print(f"Sen {kazanmalar} TL kazandın.")
    print(f"Şu satırlarda kazandın:", *kazanan_satırlar)
    return kazanmalar - bahis



def main():
    global miktar
    miktar = yatırma()
    while True:
        print(f"Şuanki paran {miktar}TL")
        if miktar <= 0:
            print("Paranız bitti.")
            tekrar = str(input("Tekrar para yatırmak ister misiniz?(E/H): "))
            if tekrar == "E":
                return main()
            else:
                break
        oyna = input("Oynamak için Enter'a bas.(çıkmak için q ya basınız)")
        if oyna == "q":
            break
        miktar += döndür(miktar)

    print(f"Bu kadar parayla ayrıldın: {miktar}TL")


main()







