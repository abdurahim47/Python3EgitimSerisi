# -*- coding: utf-8 -*-

def get_address(metin="Adresi Giriniz: "):
    """Kullanıcıdan alınan adres verisinin \n gibi şeylere maruz kalmaması için yazıldı"""
    adres = input(metin)
    return r"".join(adres)

def get_char(metin="Lütfen Bir Karakter Giriniz: "):
    """Kullanıcıdan tek bir karakter almak için tasarlandı."""
    kabul = "abcçdefgğhıijklmnoöprsştuüvyzqwxABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX"
    girdi_char = str(input(metin))
    while len(girdi_char) != 1:
            girdi_char = get_char(metin)
    else:
        if girdi_char not in kabul:
            girdi_char = get_char(metin)
    return girdi_char

def get_string(metin="Lütfen Bir String Giriniz: "):
    """Kullanıcıdan bir karakter katarı almak için tasarlandı."""
    while True:
        try:
            girdi_string = str(input(metin))
        except ValueError as e:
            print("Yanlış Değer! Lütfen Bir String Giriniz: ")
            continue
        else:
            return girdi_string

def get_int(metin="Lütfen Bir Tamsayı Giriniz: "):
    """Kullanıcıdan tamsayı alımı için tasarlandı."""
    while True:
        try:
            girdi_int = int(input(metin))
        except ValueError as e:
            print("Yanlış Değer! Lütfen Bir Tamsayı Giriniz: ")
            continue
        else:
            return girdi_int

def get_pos_int(metin="Lütfen Pozitif Bir Tamsayı Giriniz: "):
    """Kullanıcıdan pozitif tamsayı alımı için tasarlandı."""
    sayı = get_int(metin)
    while sayı <= 0:
        sayı = get_pos_int(metin)
    else:
        return sayı

def get_neg_int(metin="Lütfen Negatif Bir Tamsayı Giriniz: "):
    """Kullanıcıdan negatif tamsayı alımı için tasarlandı."""
    sayı = get_int(metin)
    while sayı >= 0:
        sayı = get_neg_int(metin)
    else:
        return sayı

def get_float(metin="Lütfen Bir Ondalıklı Sayı Giriniz: "):
    """Kullanıcıdan ondalıklı sayı alımı için tasarlandı."""
    while True:
        try:
            metin = str(metin)
            girdi_float = float(input(metin))
        except ValueError as e:
            print("Yanlış Değer! Lütfen bir ondalıklı sayı giriniz")
            continue
        else:
            return girdi_float

def get_pos_float(metin="Lütfen Pozitif Bir Ondalıklı Sayı Giriniz: "):
    """Kullanıcıdan pozitif ondalıklı sayı alımı için tasarlandı."""
    sayı = get_float(metin)
    while sayı <= 0:
        sayı = get_pos_float(metin)
    else:
        return sayı

def get_neg_float(metin="Lütfen Negatif Bir Ondalıklı Sayı Giriniz: "):
    """Kullanıcıdan negatif ondalıklı sayı alımı için tasarlandı."""
    sayı = get_float(metin)
    while sayı >= 0:
        sayı = get_neg_float(metin)
    else:
        return sayı

def get_zero(metin="Lütfen Sıfır Değerini Giriniz: "):
    """Kullanıcıdan sıfır sayısının alımı için tasarlandı."""
    sayı = get_float(metin)
    while sayı != 0.0:
        sayı = get_zero(metin)
    else:
        return sayı
