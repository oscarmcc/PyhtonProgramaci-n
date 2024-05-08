"""
Realiza un programa que sepa decir la capital de un país (en caso de conocer la respuesta) y que, además, sea capaz de
aprender nuevas capitales. En principio, el programa solo conoce las capitales de España, Portugal y Francia.
Estos datos deberán estar almacenados en un diccionario. Los datos sobre capitales que vaya aprendiendo el programa se
deben almacenar en el mismo diccionario. El usuario sale del programa escribiendo la palabra “salir”.
"""
capitals = {"España": "Madrid", "Portugal": "Lisboa", "Francia": "Paris"}
while True:
    country = input("Escribe el nombre de un país y te diré su capital: ")
    if country in capitals:
        print(capitals[country])
    elif country == "salir":
        exit(0)
    else:
        capital_of_country = input(f"No conozco la respuesta ¿cuál es la capital de {country}?: ")
        capitals[country] = capital_of_country
        print("Gracias por enseñarme nuevas capitales")
