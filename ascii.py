# Enkodiranje/dekodiranje plain texta u ASCII kod. Moguće četiri vrste enkodiranja - binary, octal, decimal, hexadecimal.
# Vrijednost baza koje se prosljeđuju fukcijama mogu biti: 2 (binary), 8 (octal), 10 (decimal) ili 16 (hexadecimal).

# funkcija za enkodiranje plain teksta u ASCII kod
# ascii_encoding_base baza vrste ASCII kodiranja koji se izvodi. Vrijednost može biti: 2 (binary), 8 (octal), 10 (decimal) ili 16 (hexadecimal).
def ascii_encode(text, ascii_encoding_base):
    ascii_encoded = ""
    # Provjera je li ispravno unesena baza (2, 8, 10 ili 16). Prekidanje postupka ako nije i vraćanje teksta greške.
    if ascii_encoding_base not in [2, 8, 10, 16]:
        ascii_encoded = "Greška! Funkciji ascii_encode(...) proslijeđen neispravna baza enkodiranja: " + ascii_encoding_base
        return ascii_encoded
    if ascii_encoding_base == 2:
        for char in text:
            ascii_encoded += bin(ord(char))[2:] + " "
    elif ascii_encoding_base == 8:
        for char in text:
            ascii_encoded += oct(ord(char))[2:] + " "
    elif ascii_encoding_base == 10:
        for char in text:
            ascii_encoded += str(ord(char)) + " "
    elif ascii_encoding_base == 16:
        for char in text:
            ascii_encoded += hex(ord(char))[2:] + " "
    return ascii_encoded
                

# funkcija za dekodiranje texta iz ASCII koda u plain text
# ascii_encoding_base baza vrste ASCII dekodiranja koji se izvodi. Vrijednost može biti: 2 (binary), 8 (octal), 10 (decimal) ili 16 (hexadecimal). 
def ascii_decode(text, ascii_encoding_base):
    ascii_decoded = ""
    # Provjera je li ispravno unesena baza (2, 8, 10 ili 16). Prekidanje postupka ako nije i vraćanje teksta greške.
    if ascii_encoding_base not in [2, 8, 10, 16]:
        ascii_decoded = "Greška! Funkciji ascii_decode(...) proslijeđen neispravna baza enkodiranja: " + ascii_encoding_base
        return ascii_decoded
    text = text.split()
    for value in text:
        ascii_decoded += chr(int(value, ascii_encoding_base))
    return ascii_decoded
