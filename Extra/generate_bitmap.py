"""
Generador de bitmap 128x64 - "CLASSIC SPACE INVADERS"
Diseño limpio y clasico:
  - Fila 1: 5 aliens tipo Squid (parte superior)
  - Fila 2: 6 aliens tipo Crab (debajo)
  - Campo de estrellas (puntos simples)
  - Recuadro doble limpio en el centro (zona de texto)
  - 3 bunkers clasicos abajo
  - Nave del jugador en la base con suelo
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

W, H = 128, 64
canvas = [[0]*W for _ in range(H)]

def px(x, y, v=1):
    if 0 <= x < W and 0 <= y < H:
        canvas[y][x] = v

def hline(x1, x2, y, v=1):
    for x in range(x1, x2+1): px(x, y, v)

def vline(x, y1, y2, v=1):
    for y in range(y1, y2+1): px(x, y, v)

def rect(x1, y1, x2, y2, v=1):
    hline(x1, x2, y1, v); hline(x1, x2, y2, v)
    vline(x1, y1, y2, v); vline(x2, y1, y2, v)

def fill(x1, y1, x2, y2, v=1):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1): px(x, y, v)

def spr(rows, cols, ox, oy):
    for ri, row in enumerate(rows):
        for ci in range(cols):
            if (row >> (cols - 1 - ci)) & 1:
                px(ox + ci, oy + ri)

# ═══════════════════════════════════════════════
#  FILA 1 — Squid (8 x 8) — 5 aliens, y=1
# ═══════════════════════════════════════════════
SQUID = [
    0b00111100,   # ..XXXX..
    0b01111110,   # .XXXXXX.
    0b11011011,   # XX.XX.XX
    0b11111111,   # XXXXXXXX
    0b01111110,   # .XXXXXX.
    0b00100100,   # ..X..X..
    0b01011010,   # .X.XX.X.
    0b10100101,   # X.X..X.X
]
# 5 aliens x 12px (8px sprite + 4px gap) = 56px → start x=36
for i in range(5):
    spr(SQUID, 8, 36 + i * 12, 1)

# ═══════════════════════════════════════════════
#  FILA 2 — Crab (8 x 8) — 6 aliens, y=11
# ═══════════════════════════════════════════════
CRAB = [
    0b01000010,   # .X....X.
    0b00111100,   # ..XXXX..
    0b01111110,   # .XXXXXX.
    0b11011011,   # XX.XX.XX
    0b11111111,   # XXXXXXXX
    0b01111110,   # .XXXXXX.
    0b01011010,   # .X.XX.X.
    0b10100101,   # X.X..X.X
]
# 6 aliens x 11px (8px + 3px gap) = 63px → start x=32
for i in range(6):
    spr(CRAB, 8, 32 + i * 11, 11)

# ═══════════════════════════════════════════════
#  ESTRELLAS — solo puntos simples
# ═══════════════════════════════════════════════
stars = [
    # Esquinas y bordes superiores
    (3, 1),  (11, 3),  (24, 0),  (80, 0),  (98, 2),  (115, 1), (125, 4),
    (2, 5),  (20, 7),  (120, 6), (127, 9),
    # Entre las filas de aliens
    (6, 9),  (18, 10), (115, 9),  (124, 10),
    # Laterales del recuadro (x<10 y x>117)
    (4, 22), (7, 27),  (2, 32),   (5, 37),  (8, 42),
    (122, 23),(125, 28),(120, 33),(124, 38),(121, 43),
    # Debajo del recuadro
    (3, 46),  (14, 45), (28, 46), (45, 45), (82, 45), (96, 46), (113, 45), (124, 46),
    # Zona bunkers (lados)
    (5, 50),  (127, 51),
]
for (x, y) in stars:
    px(x, y)

# ═══════════════════════════════════════════════
#  RECUADRO DE TEXTO — doble borde limpio
#  Exterior: x=10, y=20  hasta  x=117, y=44
#  Interior: x=12, y=22  hasta  x=115, y=42
# ═══════════════════════════════════════════════
fill(10, 20, 117, 44, 0)   # garantizar interior negro
rect(10, 20, 117, 44)       # borde exterior
rect(12, 22, 115, 42)       # borde interior

# ═══════════════════════════════════════════════
#  BUNKERS CLASICOS (8 x 6) — 3 escudos
# ═══════════════════════════════════════════════
BUNKER = [
    0b01111110,   # .XXXXXX.
    0b11111111,   # XXXXXXXX
    0b11111111,   # XXXXXXXX
    0b11111111,   # XXXXXXXX
    0b11000011,   # XX....XX
    0b11000011,   # XX....XX
]
spr(BUNKER, 8, 22, 47)   # izquierda
spr(BUNKER, 8, 60, 47)   # centro
spr(BUNKER, 8, 98, 47)   # derecha

# ═══════════════════════════════════════════════
#  LASER del jugador (linea punteada)
# ═══════════════════════════════════════════════
px(64, 53)
px(64, 54)
px(64, 55)

# ═══════════════════════════════════════════════
#  NAVE DEL JUGADOR (11 x 5), centrada
# ═══════════════════════════════════════════════
PLAYER = [
    0b00000100000,   # .....X.....
    0b00001110000,   # ....XXX....
    0b01111111100,   # .XXXXXXXXX.
    0b11111111110,   # XXXXXXXXXX.  (wait, 11 bits)
    0b11111111110,   # XXXXXXXXXX.
]
# center: 128/2 - 11/2 = 58
spr(PLAYER, 11, 58, 56)

# ═══════════════════════════════════════════════
#  SUELO (2 lineas solidas al fondo)
# ═══════════════════════════════════════════════
hline(0, 127, 62)
hline(0, 127, 63)

# ═══════════════════════════════════════════════
#  CONVERTIR Y GUARDAR
# ═══════════════════════════════════════════════
def to_bytes():
    out = []
    for row in canvas:
        for bi in range(16):
            b = 0
            for bit in range(8):
                b |= row[bi*8 + bit] << (7 - bit)
            out.append(b)
    return out

raw = to_bytes()
lines = ["const unsigned char menu_principal[] PROGMEM = {"]
for i in range(0, len(raw), 16):
    chunk = raw[i:i+16]
    lines.append("    " + ", ".join(f"0x{b:02x}" for b in chunk) + ",")
lines[-1] = lines[-1].rstrip(",")
lines.append("};")

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Bitmap_nuevo.cpp")
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"OK: {len(raw)} bytes -> {path}")

# ── Preview ASCII ──────────────────────────────
print()
for row in canvas:
    print("".join("X" if p else "." for p in row))
