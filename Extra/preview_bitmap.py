"""
Previsualización visual del bitmap generado
"""
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

# Parsear el .cpp generado y mostrar en ASCII art
with open("Bitmap_nuevo.cpp", "r") as f:
    content = f.read()

# Extraer los bytes
hex_vals = re.findall(r'0x([0-9a-fA-F]{2})', content)
raw_bytes = [int(h, 16) for h in hex_vals]

print(f"Total bytes: {len(raw_bytes)}")
print("=" * 130)
print("PREVIEW (128x64)  X=blanco, .=negro")
print("=" * 130)

for row in range(64):
    line = ""
    for byte_i in range(16):
        b = raw_bytes[row * 16 + byte_i]
        # Invertir: en PROGMEM 0xFF=negro, 0x00=blanco
        b = b ^ 0xFF
        for bit in range(7, -1, -1):
            if (b >> bit) & 1:
                line += "X"
            else:
                line += "."
    print(line)
