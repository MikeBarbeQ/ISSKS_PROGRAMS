# Ordezkatze-letrak 
final_key = {
    'A': 'D', 'Q': 'B', 'R': 'C', 'O': 'F', 'U': 'G', 'M': 'H', 'C': 'I',
    'G': 'J', 'T': 'L', 'P': 'M', 'J': 'N', 'I': 'O', 'D': 'P', 'S': 'Q',
    'K': 'R', 'N': 'S', 'H': 'T', 'Z': 'U', 'V': 'Y', 'X': 'E', 'E': 'A',
    'F': 'X', 'L': 'Z'
}

# Textu zifratuta
ciphertext = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI.
DXKNIJCOCREQE TE HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIVCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ.
NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCVI ET DKIRXNI KXVITZRCIJEKCI XJ PEKRME.
NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXVITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXКСІК
HKCZJOI OKEJSZCNHE.
"""

# Textua deszifratzeko kodea
def decrypt(text, key): #'decrypt' funtzioa definitzen da
    decrypted_text = "" #'decrypted_text' aldagaia definitzen da eta barruan hutsik dagoena

    for char in text.upper(): #Bucle que recorre el texto caracter por caracter. '.upper()' letra larrietara bihurtzen ditu
        if char in key: #Comprueba si el carácter actual (char) existe como una clave en nuestro diccionario 'key'
            decrypted_text += key[char] #Busca el valor asociado a la clave char en el diccionario Ej. A->D
        else:
            decrypted_text += char
    return decrypted_text

# Desciframos y mostramos el mensaje final
decrypted_message = decrypt(ciphertext, final_key) #Llamamos a la función decrypt que creamos antes
print("--- MENSAJE FINAL DESCIFRADO ---\n")
print(decrypted_message)