# pylint: disable = C0103,C0114


#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */


# import re
# texto = "Tengo 25 años y 3 perros"

# resultado = re.findall(r"\d+", texto)

# print(resultado)

# import re


# texto = "Mi código es 123 y mi edad 22"

# tex = re.findall(r"\d+", texto)
# print(tex)


# import re

# texto = "Año 2025, habitación 99, folio 123456"

# tex = re.findall(r".", texto)
# print(tex)

# import re

# texto = "123456"

# tex = re.findall(r"^\d+$", texto)

# print(tex)


# import re

# email = "Ru-bén@gmail.com"

# x = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+$", email)
# print(x)


# import re

# telefono = "AB123XZ"

# x = re.findall(r"^[A-Z]{2}\d{3}[A-Z]{2}$", telefono)
# print(x)

# import re

# texto = """Contacto: ruben@gmail.com
# IP: 192.168.1.1
# Web: https://openai.com
# Tel: 8112345678
# #python"""

# correo = re.findall(r"[\w-]+@[\w\.]+\.\w+", texto)
# ip = re.findall(r"\d+\.\d+\.\d+\.\d+", texto)
# web = re.findall(r"https?:\/\/\w+\.\w+", texto)
# tel = re.findall(r"\d{10}", texto)
# hashtag = re.findall(r"#\w+$", texto)

# print("\n", correo, "\n", ip, "\n", web, "\n", tel, "\n", hashtag)

import re

texto = """
[INFO] Usuario: ruben123
Email: ruben.dev@gmail.com
IP: 192.168.0.15
URL: https://api.openai.com/v1/users
Telefono: 8112345678
MAC: AA:BB:CC:DD:EE:FF
Hashtag: #PythonMaster
Error code: ERR-500
Precio: $3,450.99
Fecha: 2026-05-12
"""

username = re.findall(r"Usuario:\s*(\w+)", texto)
email = re.findall(r"[\w]+@", texto)

print(username, email)
