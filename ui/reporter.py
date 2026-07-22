

# * Succes


def show_succes(x: tuple[str, str, str]) -> None:
    '''# Print a succes message with the path on the console'''
    print(f"✔ {x[1]}\n")
    print(f"Ruta:\n{x[2]}")
    return None

# * Error


def show_error(x: tuple[str, int]) -> None:
    '''Print a error message with the number on the console.'''
    print(f"✖ El reto {x[1]} no existe.")
    return None


# * Info


def show_info(msg: str) -> None:
    '''Print a custom message like info'''
    print(f"ℹ {msg}...")
    return None
