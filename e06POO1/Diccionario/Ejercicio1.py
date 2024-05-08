"""
 Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y
 una contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”.
 El usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene
 acceso al área restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados
 en un diccionario.

 Author= Óscar Martín-Castaño Carrillo
 Date: 12/03/2024
"""
SECURITY = {"username": "admin", "password": "admin"}
tries = 3

while True:
    user = input('Introduce tu nombre de usuario para acceder al área restringida: ')
    if user in SECURITY["username"]:
        while True:
            password = input('Introduce tu contraseña para poder acceder: ')
            if password not in SECURITY["password"]:
                tries -= 1
                print(f"Lo siento la contraseña introducida no es correcta, tienes {tries} intentos")
                if tries == 0:
                    print('No se puede acceder, acabaste con todos los intentos para acceder')
                    exit(0)
            else:
                print('Lo lograste, accediste al área restringida')
                exit(0)
    else:
        print('Lo siento, no se encuentra en el diccionario el nombre de usuario')
