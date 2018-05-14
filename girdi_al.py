def get_char(metin):
    girdi_char = ''
    metin = str(metin)
    kabul = "abcçdefgğhıijklmnoöprsştuüvyzqwxABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX"
    girdi_char = str(input(metin))
    while len(girdi_char) != 1:
            girdi_char = get_char("Lütfen Tek Bir harf Giriniz: ")
    else:
        if girdi_char not in kabul:
            girdi_char = get_char("Lütfen Bir Harf Giriniz: ")
    return girdi_char

def get_string(metin):
    while True:
        try:
            metin = str(metin)
            girdi_string = str(input(metin))
        except ValueError as e:
            print("Lütfen bir string giriniz")
            print('#' * 50)
            continue
        else:
            return girdi_string

def get_int(metin):
    while True:
        try:
            metin = str(metin)
            girdi_int = int(input(metin))
        except ValueError as e:
            print("Lütfen bir tam sayı giriniz")
            print('#' * 50)
            continue
        else:
            return girdi_int

def get_pos_int():
    sayı = get_int("Lütfen Pozitif Bir Sayı Girin: ")
    while sayı <= 0:
        sayı = get_pos_int()
    else:
        return sayı

def get_neg_int():
    sayı = get_int("Lütfen Negatif Bir Sayı Girin: ")
    while sayı >= 0:
        sayı = get_neg_int()
    else:
        return sayı

def get_float(metin):
    while True:
        try:
            metin = str(metin)
            girdi_float = float(input(metin))
        except ValueError as e:
            print("Lütfen bir ondalıklı sayı giriniz")
            print('#' * 50)
            continue
        else:
            return girdi_float

def get_pos_float():
    sayı = get_float("Lütfen Pozitif Bir Sayı Girin: ")
    while sayı <= 0:
        sayı = get_pos_float()
    else:
        return sayı

def get_neg_float():
    sayı = get_float("Lütfen Negatif Bir Sayı Girin: ")
    while sayı >= 0:
        sayı = get_neg_float()
    else:
        return sayı

def get_zero():
    sayı = get_float("Lütfen Pozitif Bir Sayı Girin: ")
    while sayı != 0.0:
        sayı = get_zero()
    else:
        return sayı
