"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas
dentro de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho
trabajo. Por ejemplo, la función es_capicúa() resulta trivial teniendo voltea() y la función siguiente_primo() también
es muy fácil de implementar teniendo es_primo().

Prohibido usar funciones de conversión del número a una cadena.

Author: Óscar Martín-Castaño Carrillo
Date: 04/12/2023
"""


def voltea(number_to_flip):
    digito_flip = 0
    while number_to_flip != 0:
        rest = number_to_flip % 10
        number_to_flip //= 10
        digito_flip = digito_flip * 10 + rest
    return digito_flip


def es_capicua(capicua):
    digit_flip = voltea(capicua)
    if capicua == digit_flip:
        print(f'El número {capicua} es capicúa')
    else:
        print(f"El número {capicua} no es capicúa")


def es_primo(prime):
    if prime < 2:
        return False
    for i in range(2, int(prime ** 0.5) + 1):
        if prime % i == 0:
            return False
    return True


def siguiente_primo(next):
    prime = next
    while True:
        prime += 1
        if es_primo(prime):
            print(f"El siguiente primo es {prime}")
            break


def digits(digit):
    repetitions = 0
    while digit != 0:
        digit //= 10
        repetitions += 1
    return repetitions


def n_digits(digit_n, n):
    position = digits(digit_n)
    while position != 0:
        rest = digit_n % 10
        digit_n //= 10
        position -= 1
        if n == rest:
            print(f"La posición es {position}")
            found = True
            break
        else:
            found = False
    return found


def position_n_digit(position_digit, n):
    position = n_digits(position_digit, n)
    if not position:
        print(-1)


def quita_por_detras(digit, n):
    digit //= 10 ** n
    return digit


def quita_por_delante(digit_before, n):
    digit = voltea(digit_before)
    before = quita_por_detras(digit, n)
    after = voltea(before)
    return after


def pega_por_detras(add, number, n=1):
    addition = add * (10 ** n) + number
    return addition


def pega_por_delante(add, number):
    digit = voltea(add)
    before = pega_por_detras(digit, number)
    after = voltea(before)
    return after


def trozo_numero(number, first_position, last_position):
    first = quita_por_delante(number, first_position)
    piece = quita_por_detras(first, last_position)
    return piece


def junta_numero(number, number_to_add):
    repetitions = digits(number_to_add)
    final_number = pega_por_detras(number, number_to_add, repetitions)
    return final_number


if __name__ == '__main__':
    voltea(123)
    es_capicua(121)
    es_capicua(122)
    verificar = 163
    if es_primo(verificar):
        print('Es primo')
    else:
        print('No es primo')
    siguiente_primo(9)
    digits(1234)
    n_digits(1234, 1)
    n_digits(34567, 5)
    n_digits(29293, 9)
    position_n_digit(1234, 2)
    position_n_digit(3321, 4)
    position_n_digit(136792, 8)
    print(quita_por_detras(1234, 2))
    print(quita_por_detras(1234, 6))
    print(quita_por_detras(12554, 4))
    print(quita_por_delante(1234, 1))
    print(quita_por_delante(345679, 4))
    print(pega_por_detras(2345, 6))
    print(pega_por_delante(12345, 6))
    print(trozo_numero(1234567, 2, 2))
    print(trozo_numero(145627894, 4, 5))
    print(junta_numero(1234, 56))
    print(junta_numero(12986, 4512))
