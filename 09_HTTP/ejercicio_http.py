"""
- Servicio Web: Aplicaciones Web que permiten la comunicación entre dos dispositivos electrónicos en red
- RESTful API: Interfaz utilizada para intercambiar información por la red entre dos dispositivos.
  Puede ser leida (GET), actualizada(PUT), creada(POST) o borrada(DELETE)
- Protocolo HTTP: Protocolo de transferencia de Hipertexto, utilizado para intercambiar documentos de hipermedia (html)
- Peticiones HTTP: Mensajes enviados desde una máquina cliente a un servidor para iniciar una acción (GET, PUT, POST, DELETE)
- Respuestas HTTP:
    - 200: OK (Aceptado)
    - 400: Bad Request (Petición no encontrada)
    - 500: Internal Server Error (Error del servidor)
"""

import requests #Python deja que el usuario pueda hacer peticiones por http con la librería Request

x = requests.get('https://www.google.com/a')

print(x.status_code) #Imprime el código de la respuesta

if x.status_code == 404:
    print("Error de petición")
else:
    print(x.text)  # Imprime el HTML en este caso de la web