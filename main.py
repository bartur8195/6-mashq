# 2
def tasodifiy_iqtibos():
    import random

    iqtiboslar = [
        "Hech qachon taslim bo‘lma!",
        "Bugungi mehnat — ertangi muvaffaqiyat.",
        "Orzularing sari dadil qadam tashla.",
        "Harakat — rivojlanish kaliti.",
        "Muvaffaqiyat sabrni sevadi."
    ]

    print(random.choice(iqtiboslar))

# 3
def fayl_yaratish():
    with open("salom.txt", "a", encoding="utf-8") as fayl:
        fayl.write("Dastur ishga tushdi!\n")
    print("Xabar faylga yozildi.")
