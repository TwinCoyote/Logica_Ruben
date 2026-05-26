import requests
from io import open
from PIL import Image, UnidentifiedImageError
import math
from io import BytesIO


url = "https://img.wattpad.com/71c062adfb5232c991e539f734f4f139d1d43205/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4d6833715f67725a444f79707a773d3d2d34342e313562363061366635666633326166373539343539303337363032312e6a7067?s=fit&w=720&h=720"

# url = "https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#image-sequences"


def image(link):
    try:
        response = requests.get(link)

        mem = BytesIO(response.content)

        im = Image.open(mem)

        # ancho
        # -----  =  aspect radio
        # alto
        # print(im)
        # print(im.size)

        i = im.size
        ancho = i[0]
        alto = i[1]

        # print(ancho)
        # print(alto)

        mcd = math.gcd(ancho, alto)
        ancho = ancho // mcd
        alto = alto // mcd

        return f"Su aspect Radio es {ancho} : {alto}"

    except requests.exceptions.MissingSchema:
        return "Url No Valida"
    except SyntaxError:
        return "Escribe bien el url"
    except UnidentifiedImageError:
        print(f"Error: El contenido en {url} no es una imagen válida.")
        return None


print(image(url))
