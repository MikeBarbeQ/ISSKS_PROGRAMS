from collections import Counter
import re

ciphertext = """
RU AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI ANNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCUCNPI OKXJHXDIDZTCNHE AX TE ACKKRRCU EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IRAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RU
TEN DXKNUETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNUCOCREQE TE HKEACRCU KXVITZRCUEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEGEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTUE XT 22 AX JhCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCU. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCVI ET DKIRXNI KXVITZRCUEKCI XJ PERNME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XINHETCLCNPI, RU TE RIPDTCRCAEA AXT UIQCKKJI AXT OKXJHX DIDZTEK V AX TE ACKKRRCU EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXVITZRCU, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RU XTTI XT DNIHXKCIK
HKCZJOI OKEJSZCNHE.
"""

# Frecuencias del español (ordenadas)
esp_freq_order = "EAOLSNRDUITCPMYQBHGFVJÑZXKW"

# Palabras comunes en español
common_words = ["EL", "LA", "DE", "EN", "QUE", "ES", "UN", "POR", "CON", "PARA", "UNA", "SU", "LOS", "LAS", "SE", "DEL", "AL", "LO", "COMO", "MÁS", "PERO", "SUS", "LE", "HA", "ME", "SI", "SIN", "SOBRE", "ESTE", "YA", "CUANDO", "TODO", "ESTA", "ERAN", "SER", "HASTA", "DESDE", "ESTABA", "MI", "PORQUE", "MUY", "AÑOS", "SOY", "TIENE", "MEJOR", "FUE", "HACIA"]

def clean_text(text):
    return ''.join(ch for ch in text if ch.isalpha()).upper()

def get_frequency_order(text):
    cleaned = clean_text(text)
    freq = Counter(cleaned)
    return ''.join([letra for letra, _ in freq.most_common()])

def decrypt(text, mapping):
    result = []
    for ch in text:
        if ch.upper() in mapping:
            if ch.isupper():
                result.append(mapping[ch.upper()].upper())
            else:
                result.append(mapping[ch.upper()].lower())
        else:
            result.append(ch)
    return ''.join(result)

def find_short_words(text, length=2):
    """Encuentra palabras cortas repetidas para adivinar artículos/preposiciones"""
    words = re.findall(r'\b[A-Z]{%d}\b' % length, text.upper())
    freq = Counter(words)
    return [word for word, count in freq.most_common() if count > 2]

def auto_suggest_mapping(ciphertext):
    cipher_freq = get_frequency_order(ciphertext)
    
    # Mapeo inicial por frecuencia
    mapping = {}
    for i in range(min(len(cipher_freq), len(esp_freq_order))):
        mapping[cipher_freq[i]] = esp_freq_order[i]
    
    # Detectar palabras de 2 letras comunes
    short_words = find_short_words(ciphertext, 2)
    print("Palabras de 2 letras más frecuentes:", short_words[:5])
    
    # Sugerir artículos/preposiciones
    common_2_letter = ["EL", "LA", "DE", "EN", "UN", "ES", "SE", "AL", "LO", "SU"]
    
    for cipher_word in short_words[:3]:
        for common_word in common_2_letter:
            if len(cipher_word) == len(common_word):
                print(f"¿'{cipher_word}' podría ser '{common_word}'?")
                for i in range(len(cipher_word)):
                    if cipher_word[i] in mapping:
                        if mapping[cipher_word[i]] != common_word[i]:
                            print(f"  Conflicto: {cipher_word[i]} -> {mapping[cipher_word[i]]} pero debería ser {common_word[i]}")
                    else:
                        mapping[cipher_word[i]] = common_word[i]
                        print(f"  Sugerido: {cipher_word[i]} -> {common_word[i]}")
    
    return mapping

def interactive_decrypt(ciphertext):
    mapping = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        mapping[letter] = letter  # Inicialmente sin cambios
    
    while True:
        # Auto-sugerencias
        cipher_freq = get_frequency_order(ciphertext)
        print("\n" + "="*70)
        print("FRECUENCIAS (Cifrado -> Español):")
        print("Cifrado: ", cipher_freq)
        print("Español: ", esp_freq_order)
        
        # Mostrar mapeo actual
        print("\nMAPEO ACTUAL:")
        changes = [(c, p) for c, p in mapping.items() if c != p]
        if changes:
            for c, p in sorted(changes):
                print(f"{c} -> {p}")
        else:
            print("(Sin cambios aún)")
        
        # Mostrar texto descifrado parcialmente
        print("\nTEXTO PARCIALMENTE DESCIFRADO:")
        print("="*70)
        current = decrypt(ciphertext, mapping)
        print(current)
        print("="*70)
        
        # Sugerir siguiente cambio basado en frecuencias
        cipher_freq_current = get_frequency_order(ciphertext)
        for cipher_char in cipher_freq_current:
            if mapping[cipher_char] == cipher_char:  # Si aún no se ha mapeado
                esp_char = esp_freq_order[cipher_freq_current.index(cipher_char) % len(esp_freq_order)]
                print(f"\nSUGERENCIA: Probablemente '{cipher_char}' -> '{esp_char}'")
                break
        
        # Entrada del usuario
        cmd = input("\nComando ('X->E' para sustituir, 'auto' para sugerencias automáticas, 'fin' para terminar): ").strip().upper()
        
        if cmd == 'FIN':
            break
        elif cmd == 'AUTO':
            # Aplicar sugerencia automática
            for cipher_char in cipher_freq_current:
                if mapping[cipher_char] == cipher_char:
                    esp_char = esp_freq_order[cipher_freq_current.index(cipher_char) % len(esp_freq_order)]
                    mapping[cipher_char] = esp_char
                    print(f"Aplicado automáticamente: {cipher_char} -> {esp_char}")
                    break
        elif '->' in cmd:
            partes = cmd.split('->')
            if len(partes) == 2 and len(partes[0]) == 1 and len(partes[1]) == 1:
                cif, pla = partes[0], partes[1]
                mapping[cif] = pla
                print(f"Cambio realizado: {cif} -> {pla}")
            else:
                print("Formato incorrecto. Usa: LETRA_CIFRADA->LETRA_PLANA")
        else:
            print("Comando no reconocido.")
    
    return mapping

# Ejecutar el programa interactivo
print("ANÁLISIS CRIPTOGRÁFICO AUTOMÁTICO")
print("==================================")

cipher_freq = get_frequency_order(ciphertext)
print("Frecuencias en el criptograma:")
cleaned = clean_text(ciphertext)
freq = Counter(cleaned)
total = len(cleaned)
for letra, count in freq.most_common():
    print(f"{letra}: {count:3d} ({count/total*100:.2f}%)")

final_mapping = interactive_decrypt(ciphertext)

print("\n" + "="*70)
print("Mapeo final completo:")
for c in sorted(final_mapping.keys()):
    if final_mapping[c] != c:
        print(f"{c} -> {final_mapping[c]}")