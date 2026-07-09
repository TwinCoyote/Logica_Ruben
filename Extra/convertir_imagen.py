import sys
import os

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Instalando la libreria 'Pillow' para procesar imagenes...")
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageOps

def convertir_imagen(ruta_imagen, archivo_salida="bitmap_generado.cpp", umbral=128, invertir=False, pantalla_completa=True):
    try:
        # Abrir y convertir a escala de grises
        img = Image.open(ruta_imagen).convert('L')
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return

    # Si se requiere para pantalla OLED 128x64
    if pantalla_completa:
        # Redimensionar la imagen para que encaje en 128x64 manteniendo proporciones
        img.thumbnail((128, 64), Image.Resampling.LANCZOS)
        
        # Crear un lienzo (canvas) negro de 128x64
        lienzo = Image.new('L', (128, 64), color=0 if not invertir else 255)
        
        # Centrar la imagen en el lienzo
        offset_x = (128 - img.width) // 2
        offset_y = (64 - img.height) // 2
        lienzo.paste(img, (offset_x, offset_y))
        
        img = lienzo
        w, h = 128, 64
    else:
        w, h = img.size
        
    pixels = img.load()
    bytes_list = []
    
    # Calculo de bytes por fila para arreglos Adafruit GFX (empaquetado horizontal)
    bytes_per_row = (w + 7) // 8
    
    for y in range(h):
        for x_byte in range(bytes_per_row):
            b = 0
            for bit in range(8):
                x = x_byte * 8 + bit
                if x < w:
                    valor = pixels[x, y]
                    es_encendido = valor > umbral if not invertir else valor < umbral
                    
                    if es_encendido:
                        b |= (1 << (7 - bit))
            bytes_list.append(b)
            
    # Guardar en archivo C++
    with open(archivo_salida, "w") as f:
        f.write(f"// Generado automaticamente desde: {os.path.basename(ruta_imagen)}\n")
        f.write(f"// Ancho: {w}, Alto: {h}\n")
        f.write(f"const unsigned char bitmap_imagen [] PROGMEM = {{\n")
        
        for i in range(0, len(bytes_list), 16):
            chunk = bytes_list[i:i+16]
            f.write("    " + ", ".join(f"0x{b:02x}" for b in chunk) + ",\n")
        f.write("};\n")
        
    print(f"\n¡Éxito! El bitmap ha sido guardado en '{archivo_salida}'.")
    print(f"Dimensiones: {w}x{h} píxeles.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python convertir_imagen.py <ruta_a_tu_imagen.png>")
        print("Ejemplo: python convertir_imagen.py mi_fantasma.png")
    else:
        convertir_imagen(sys.argv[1])
