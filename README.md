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

## Nueva estructura para revision con AI:

```
LOGICAPROGRAMACION/

Ejercicios_Logica/
Microcontroller_Embedded_C/
Poo/
ROAD-MAP/

reto_cli/
│
├── cli.py
│
├── core/
│   ├── create.py
│   ├── reporter.py
│
├── repository/
│   └── challenge_repository.py
│
├── data/
│   └── Retos_programacion.json
│
└── README.md

```
