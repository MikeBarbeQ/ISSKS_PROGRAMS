import re
from collections import Counter

# Pega aquí el texto cifrado completo del laboratorio
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

# Lista de palabras en español que sospechas que están en el texto
known_words = ['DURRUTI', 'QUE', 'CLASE', 'HISTORIA', 'FRENTE', 'EL', 'LA']

def get_word_pattern(word):
    """
    Convierte una palabra en un patrón numérico basado en la repetición de letras.
    Ejemplo: 'HOLA' -> '0.1.2.3', 'CASA' -> '0.1.2.1', 'DURRUTI' -> '0.1.2.2.1.3.4'
    """
    word = word.upper()
    next_num = 0
    letter_nums = {}
    pattern = []
    for letter in word:
        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1
        pattern.append(letter_nums[letter])
    return '.'.join(pattern)

# 1. Limpiamos el texto cifrado: lo ponemos en mayúsculas y extraemos solo las palabras.
# Usamos una expresión regular para encontrar todas las secuencias de letras.
cipher_words = re.findall(r'[A-Z]+', ciphertext.upper())

# 2. Recorremos cada palabra que queremos buscar
for known_word in known_words:
    # Calculamos el patrón y la longitud de nuestra palabra conocida
    known_pattern = get_word_pattern(known_word)
    known_length = len(known_word)

    print(f"--- Buscando palabras con el patrón de '{known_word}' (Longitud: {known_length}) ---")

    # Usamos un Counter para encontrar y contar todas las palabras cifradas que coincidan
    potential_matches = Counter(
        word for word in cipher_words
        if len(word) == known_length and get_word_pattern(word) == known_pattern
    )

    # 3. Mostramos los resultados
    if not potential_matches:
        print("No se encontraron coincidencias.\n")
    else:
        for word, count in potential_matches.items():
            print(f"  -> Se encontró '{word}', que se repite {count} vez/veces.")
        print() # Añade una línea en blanco para separar los resultados