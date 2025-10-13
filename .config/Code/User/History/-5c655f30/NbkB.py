# Clave de sustitución final obtenida a través del criptoanálisis
# (Ciphertext_Letter -> Plaintext_Letter)
final_key = {
    'R': 'C', 'I': 'O', 'J': 'N', 'A': 'D', 'Z': 'U', 'K': 'R', 'H': 'T',
    'P': 'P', 'C': 'I', 'E': 'A', 'X': 'E', 'T': 'L', 'S': 'Q', 'N': 'S',
    'G': 'B', 'D': 'F', 'O': 'M', 'Q': 'V', 'V': 'Y', 'M': 'G'
    # Las letras U, W, Ñ, etc., no aparecen en el texto cifrado.
}

# Texto cifrado
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

def decrypt(text, key):
    """Descifra un texto usando el mapa de sustitución."""
    decrypted_text = ""
    for char in text.upper():
        if char in key:
            decrypted_text += key[char]
        else:
            decrypted_text += char  # Mantener espacios, comas, números, etc.
    return decrypted_text

# Obtenemos y mostramos el mensaje descifrado
decrypted_message = decrypt(ciphertext, final_key)
print("\n--- MENSAJE DESCIFRADO ---\n")
print(decrypted_message)