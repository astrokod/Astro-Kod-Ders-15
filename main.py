def toplam(sayilar):
    """Verilen bir listenin içindeki değerlerin toplamını return eden fonksiyon"""
    # sonuc değişkenini 0 değeriyle tanımla
    sonuc = 0
    # Tüm sayıları sırasıyla sayi değişkenine atan bir döngü
    for sayi in sayilar:
        # sayi değerini sonuc değeriyle toplayıp, sonuc değişlenine ata
        sonuc += sayi

    # sonuc'u return et
    return sonuc


def toplam_r(sayilar):
    """Verilen bir listenin içindeki değerlerin toplamını return eden fonksiyon"""
    # Gelen sayilar dizisinin eleman sayısı sıfır ise, 0 değerini return et
    # Çıkış koşulu
    if len(sayilar) == 0:
        return 0

    # kendini tekrar çağır ve argüman olarak daha önce verilen sayı listesinin
    # ilk elemanı dışındaki bütün listeyi ver,
    # Yukarıdaki işlemi sayı listesinin ilk elemanıyla topla
    return sayilar[0] + toplam_r(sayilar[1:])


def faktor(sayi):
    """Verilen sayının faktöriyelini hesaplayan fonksiyon"""
    # sonuc değişkenine 1 değerini ata
    sonuc = 1
    # 1'den sayi+1'e kadar bir döngü oluştur
    # 5 için i değeri sırasıyla:
    # 1, 2, 3, 4, 5
    # olur
    for i in range(1, sayi + 1):
        # i değerlini sonuc değeriyle çarpıp, sonuc değişkenine ata
        sonuc *= i

    # sonuc'u return et
    return sonuc


def faktor_r(sayi):
    """Verilen sayının faktöriyelini hesaplayan fonksiyon"""
    # Eğer sayı 0'a eşit ise 1 return et
    # Çıkış koşulu
    if sayi == 0:
        return 1

    # kendini çağırıp daha önce verilen
    # sayının bir eksiğini parametre olarak ver
    # yukarıdaki değeri, sayi ile çarp
    return sayi * faktor_r(sayi - 1)


if __name__ == "__main__":
    s = [1, 3, 6, 8, 12, 99, 255, -29]
    print("Toplam sonucu: ", toplam(s))
    print("Toplam (Recursive) sonucu: ", toplam_r(s))
    print("Faktöriyel sonucu: ", faktor(11))
    print("Faktöriyel (Recursive) sonucu: ", faktor_r(11))
