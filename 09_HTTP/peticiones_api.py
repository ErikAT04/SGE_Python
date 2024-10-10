#Un API es un contrato que permite a los desarrolladores interactuar con una aplicación por medio de varias interfaces
#Una RESTful API es una API que se ajusta a convenciones relacionadas a HTTP (errores, hipervínculos, etc)
#Un endpoint es un punto donde interactúan el API cliente y el servidor. En este punto se hace la petición y se reciben los recursos de dicha petición

import os
import requests

pokemonName = input("Ingrese el nombre o número de un pokémon")
if not pokemonName.isdigit():
    pokemonName = pokemonName.lower()

url = "https://pokeapi.co/api/v2/pokemon/" + pokemonName + "/"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    listaDatosPKMN = [data["name"], data["id"], data["height"], data["weight"], data["types"]]
    print(listaDatosPKMN)
else:
    print("Error del pokémon introducid")