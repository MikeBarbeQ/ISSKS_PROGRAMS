from collections import Counter

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
esp_freq = "eaolsnrdruitcpmyqbhgfvjñzxkw"

def clean_text(text):
    return ''.join(ch for ch in text if ch.isalpha()).upper()

# Calcular frecuencias
cleaned = clean_text(ciphertext)
freq = Counter(cleaned)
total = len(cleaned)
cipher_freq_order = ''.join([letra for letra, _ in freq.most_common()])

print("Frecuencias en el criptograma:")
for letra, count in freq.most_common():
    print(f"{letra}: {count/total*100:.2f}%")

print("\nOrden de frecuencia (cripto):", cipher_freq_order)
print("Orden de frecuencia (español):", esp_freq)

# Mapeo inicial automático
mapa = {}
for i in range(min(len(cipher_freq_order), len(esp_freq))):
    mapa[cipher_freq_order[i]] = esp_freq[i]

# Añadir identidades para letras no cifradas (números, puntuación)
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if ch not in mapa:
        mapa[ch] = ch  # inicialmente no cambia

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

# Bucle interactivo
while True:
    print("\n" + "="*60)
    print("Texto actual descifrado:")
    print("="*60)
    current = decrypt(ciphertext, mapa)
    print(current)
    print("="*60)
    
    cmd = input("\nIntroduce cambio (ej: 'X->E') o 'fin' para terminar: ").strip().upper()
    if cmd == 'FIN':
        break
    if '->' in cmd:
        partes = cmd.split('->')
        if len(partes) == 2 and len(partes[0]) == 1 and len(partes[1]) == 1:
            cif, pla = partes[0], partes[1]
            mapa[cif] = pla
            print(f"Cambio realizado: {cif} -> {pla}")
        else:
            print("Formato incorrecto. Usa: LETRA_CIFRADA->LETRA_PLANA")
    else:
        print("Comando no reconocido.")

print("\nMapeo final:")
for c in sorted(mapa.keys()):
    if mapa[c] != c:
        print(f"{c} -> {mapa[c]}")