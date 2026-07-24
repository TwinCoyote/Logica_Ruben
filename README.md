# LogicaProgramacion

Este repositorio contiene ejercicios de programación en Python y ejemplos de lógica.

## Origen de los ejercicios

- Ejercicios sacados de un libro de Python hecho por **mouredev**.
- Ejercicios y contenido sacados de la página:
  - https://retosdeprogramacion.com/ejercicios
- Ejercicios también sacados de **LeetCode**.

## Contenido

- Ejercicios de lógica y programación en Python.
- Un roadmap con guías y conceptos de programación.

## Uso de `scriptRuben.py`

Este script descarga los retos de programación desde https://retosdeprogramacion.com/ejercicios y crea un archivo Python con la información del reto solicitado.

### Requisitos

- Python 3
- Paquetes: `requests`, `beautifulsoup4`

Instalación:

```bash
pip install requests beautifulsoup4
```

### Ejecución

```bash
python scriptRuben.py "Numero de reto"
```

### Qué hace

- extrae los retos de la web y guarda `Retos_programacion.json`
- crea la carpeta `Ejercicios_Logica` si no existe
- genera un archivo como `Ejercicios_Logica/40_Top_algoritmos.py`
- elimina los caracteres inválidos de Windows en el nombre del archivo

## Nota

El repositorio incluye tanto ejercicios clásicos como material de aprendizaje basado en recursos públicos y plataformas de retos de programación.

## 🤖 Sistema de Revisión Automática con IA

Se ha implementado un CLI que utiliza la API de Gemini para revisar automáticamente tus soluciones de programación.

### Estructura del proyecto reto_cli:

```
reto_cli/
│
├── cli.py                    # Punto de entrada del CLI
│
├── core/
│   ├── review.py            # Orquestador de revisión con IA
│   ├── create.py            # Creación de nuevos retos
│   ├── extract_solution.py  # Extrae código de archivos
│   ├── build_prompt.py      # Construye prompts para la IA
│   ├── ai_client.py         # Cliente de Gemini API
│   ├── parse_response.py    # Parsea respuestas JSON
│   └── reporter.py          # Formatea y muestra resultados
│
├── repository/
│   ├── challenge_repository.py   # Acceso a datos de retos
│   └── file_repository.py        # Localiza archivos de soluciones
│
├── ui/
│   └── reporter.py          # Interfaz de usuario para reportes
│
├── data/
│   └── Retos_programacion.json   # Datos de los retos
│
└── .env                     # Variables de entorno
```

### Requisitos

- Python 3.10+
- Paquetes:
  ```bash
  pip install google-genai python-dotenv
  ```

### Configuración

1. Crear un archivo `.env` en la carpeta `reto_cli/`:

   ```
   API_KEY=tu_clave_de_api_gemini
   DEBUG=false
   ```

2. Obtener la API Key desde [Google AI Studio](https://aistudio.google.com/apikey)

### Uso del CLI

#### Revisar una solución

```bash
python reto_cli/cli.py review <numero_reto>
```

**Ejemplo:**

```bash
python reto_cli/cli.py review 27
```

**Salida esperada:**

```
Challenge: Cuadrado y Triangulo 2D
================================

Code Analysis

Strengths
__________
✔ Correct use of object-oriented programming
✔ Proper calculation of geometric properties
✔ Clear method implementations

Potential Bugs
_______________
✖ Missing input validation for negative dimensions

Suggestions
-----------
→ Add docstrings to all methods
→ Consider using dataclasses for simpler code
→ Add type hints for better code clarity
```

#### Crear un nuevo reto

```bash
python reto_cli/cli.py create <numero_reto>
```

### Cómo funciona la revisión

1. **Extrae el código**: Busca y carga el archivo de la solución
2. **Construye el prompt**: Prepara una instrucción detallada para la IA
3. **Consulta Gemini API**: Envía el código para análisis
4. **Parsea respuesta**: Convierte la respuesta JSON en estructura de datos
5. **Muestra resultado**: Formatea y presenta el análisis al usuario

### Variables de entorno

| Variable  | Descripción                   | Ejemplo          |
| --------- | ----------------------------- | ---------------- |
| `API_KEY` | Clave de acceso a Gemini API  | `sk-...`         |
| `DEBUG`   | Habilita respuestas simuladas | `true` o `false` |

### Estructura de datos de revisión

El analizador retorna una estructura con:

- **Strengths**: Fortalezas del código
- **Bugs**: Posibles errores o problemas
- **Suggestions**: Recomendaciones de mejora

### Notas

- El repositorio incluye tanto ejercicios clásicos como material de aprendizaje basado en recursos públicos
- Las revisiones requieren conexión a internet y una API Key válida
- Se puede usar `DEBUG=true` para pruebas sin consumir cuota de API
