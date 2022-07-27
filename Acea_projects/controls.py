import re
def controllaCF(codice_fiscale):
    CODICE_REGEXP = "^[0-9A-Z]{16}$"
    SETDISP = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18, 20,
        11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23 ]
    ORD_ZERO = ord('0')
    ORD_A = ord('A')

    if 0 == len(codice_fiscale):
        return ""
    if(16 != len(codice_fiscale)):
        return ("La lunghezza del codice fiscale non &egrave;\n" +
                "corretta: il codice fiscale dovrebbe essere lungo\n" +
                "esattamente 16 caratteri.")
    codice_fiscale = codice_fiscale.upper()
    match = re.match(CODICE_REGEXP, codice_fiscale)
    if not match:
        return ("Il codice fiscale contiene dei caratteri non validi:\n" +
                    "i soli caratteri validi sono le lettere e le cifre.")
    s = 0
    for i in range(1,14,2):
        c = codice_fiscale[i]
        if c.isdigit():                
            s += ord(c) - ORD_ZERO
        else:
            s += ord(c) - ORD_A
    for i in range(0,15,2):
        c = codice_fiscale[i]
        if c.isdigit():
            c = ord(c) - ORD_ZERO
        else:
            c = ord(c) - ORD_A
        s += SETDISP[c]
    if (s % 26 + ORD_A != ord(codice_fiscale[15])):
        return ("Il codice fiscale non &egrave; corretto:\n" +
                "il codice di controllo non corrisponde.")
    return ""

def controllaPIVA(partita_iva):
    IVA_REGEXP = "^[0-9]{11}$"
    ORD_ZERO = ord('0')

    if 0 == len(partita_iva):
        return ""
    if 11 != len(partita_iva):
        return ("La lunghezza della partita IVA non &egrave;\n" +
                "corretta: la partita IVA dovrebbe essere lunga\n" +
                "esattamente 11 caratteri.\n")
    match = re.match(IVA_REGEXP, partita_iva)
    if not match:
        return ("La partita IVA contiene dei caratteri non ammessi:\n" +
                "la partita IVA dovrebbe contenere solo cifre.\n")
    s = 0
    for i in range(0, 10, 2):
        s += ord(partita_iva[i]) - ORD_ZERO
    for i in range(1, 10, 2):
        c = 2 * (ord(partita_iva[i]) - ORD_ZERO)
        if c > 9:
            c -= 9
        s += c

    if (10 - s%10)%10 != ord(partita_iva[10]) - ORD_ZERO:
        return ("La partita IVA non &egrave; valida:\n" +
                "il codice di controllo non corrisponde.")
    return ""