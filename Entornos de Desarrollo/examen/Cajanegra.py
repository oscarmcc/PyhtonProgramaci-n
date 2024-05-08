"""
Clase "Numeros"

Autor: Jaime Rabasco Ronda
Fecha: 09/03/2023.
"""


class Numeros:

    def __init__(self):
        numero = 0

    """
    Comprueba si un numero es primo
    """

    def primo(self, num):
        bandera = True
        for i in range(2, num - 1, 1):
            if num % i == 0:
                bandera = False
        return bandera

    """
    Devuelve el resultado de elevar un n mero a un exponente
    """

    def potencia(self, base, exponente):
        total = 1
        if base == 0 and exponente == 0:
            return "Indeterminacion"
        else:
            for i in range(1, exponente + 1, 1):
                total *= base
            return total

    """
    Devuelve la secuencia de Fibonacci de un número
    """

    def fibonnacci(self, num):
        ant1 = 1
        ant2 = 0
        actual = 0
        if num == 0 or num == 1:
            return num
        for i in range(2, num + 1, 1):
            actual = ant1 + ant2
            ant2 = ant1
            ant1 = actual
        return actual

    """
    Devuelve si un número es perfecto. Un número es perfecto cuando es igual
	a la suma de sus divisores propios positivos, sin incluirse él mismo Ej:
    6 Es Perfecto, sus divisores 1,2,3. 6=1+2+3.
    """

    def perfecto(self, num):
        suma = 0
        for i in range(1, num, 1):
            if (num % i == 0):
                suma = suma + i
        if (suma == num):
            return True
        else:
            return False

    """
    Un Número n es Abundante si la sumas de sus divisores es mayor que 2n.
    Por Ejemplo: 24,sus divisores son 1, 2, 3, 4, 6, 8, 12 y 24, cuya suma es 60. Puesto que 60 es mayor que 2 x 24, el número 24 es abundante. Y su abundancia es 60 menos 2 x 24 = 12.
    Ejemplos: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102
    """

    def abundante(self, num):
        suma = 0
        for i in range(1, num, 1):
            if (num % i == 0):
                suma = suma + i
        if suma > num:
            return suma - num
        else:
            return -1

    """
    Un Número n Narcisista es aquel que es igual a la suma de sus dígitos elevados a la potencia de su número de cifras.
	 Por Ejemplo:
	 	371 es un número narcisista, ya que: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
	 	93084 es un número narcisista, ya que: 9^5 + 3^5 + 0^5 + 8^5 + 4^5 = 59049 + 243 + 0 + 32768 + 1024 = 93084
	 Ejemplos: Solo hay 88 en base decimal, son los siguientes:
	 	1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651, 40028394225, 42678290603, 44708635679, 49388550606, 82693916578, 94204591914, 28116440335967, 4338281769391370, 4338281769391371, 21897142587612075, 35641594208964132, 35875699062250035, 1517841543307505039, 3289582984443187032, 4498128791164624869, 4929273885928088826
    """

    def narcisista(self, num):
        num_cadena = str(num)
        longitud_num = len(num_cadena)
        suma = 0
        for letra in num_cadena:
            # Carácter a entero
            cifra_actual = int(letra)
            # Elevar ese carácter a la potencia dada por la longitud del número
            elevado = pow(cifra_actual, longitud_num)
            # El resultado lo añadimos a suma
            suma = suma + elevado
        # Comprobar si la suma al elevar es igual al número que recibimos
        if num == suma:
            return True
        else:
            return False

    """
    Un Número de Muchausen es aquel al que la suma de sus dígitos (en base 10), elevados a la misma
	 potencia de ellos mismos es el mismo número

	 Por Ejemplo: 3435= 3^3+4^4+3^3+5^5 = 27+256+27+3125=3435
	 	1 es un número muchausen
	 Si no lo es, el método devuelve la diferencia de cálculo
	 Ejemplo:
	 	123 = 1^1+2^2+3^3 = 1+ 4 + 9 = -91
	 	752 = .... = 825920
	 	34 = ......= 249
	 	.......
	"""

    def munchausen(self, num):
        suma = 0
        num_cadena = str(num)
        longitud_num = len(num_cadena)
        for letra in num_cadena:
            # Carácter a entero
            cifra_actual = int(letra)
            # Elevar ese carácter a la potencia dada por la longitud del número
            # elevado = pow(cifra_actual, longitud_num)
            # El resultado lo añadimos a suma
            suma = suma + pow(cifra_actual, cifra_actual)
        # Comprobar si la suma al elevar es igual al número que recibimos
        if num == suma:
            return 0
        else:
            return False

    """
    Números Automórficos: Números cuyo cuadrado termina con el mismo número. Por ejemplo, 5^2 = 25, y 25 termina en 5.
	Números automórficos: 5, 6, 25, 76, 376, 625, 9376
	"""

    def automorficos(self, num):
        # Verificamos si el número es menor que 0
        if num < 0:
            return False
        # Calculamos el cuadrado del número
        cuadrado = num ** 2
        # Convertimos ambos, el número y su cuadrado, a cadenas para facilitar la comparación
        str_n = str(num)
        str_cuadrado = str(cuadrado)
        # Comparamos si el final del cuadrado es igual al número original
        return str_cuadrado.endswith(str_n)

    """
    Números Harshad: Números que son divisibles por la suma de sus dígitos.
	Números Harshad: [1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100]
	"""

    def harshad(self, num):
        # Verificar primero si el número es entero positivo
        if num <= 0:
            return False  # Los números negativos o cero no pueden ser Harshad

        numero_str = str(num)
        suma_digitos = 0

        # Calculamos la suma de los dígitos sin usar una comprensión de lista en una sola línea
        for digito in numero_str:
            suma_digitos += int(digito)

        # Verificamos si el número es divisible por la suma de sus dígitos
        return num % suma_digitos == 0

    """
    Números Cuadrados Perfectos: Números que son el cuadrado de algún número entero. Son un subconjunto de los números cuadrados mencionados anteriormente.
	Números Cuadrados Perfectos: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	"""

    def cuadrado_perfecto(self, num):
        # Verificamos primero si el número es entero positivo
        if num < 0:
            return False  # Los números negativos no pueden ser cuadrados perfectos

        # Calculamos la raíz cuadrada del número y verificar si es un entero
        raiz = num ** 0.5
        return raiz.is_integer()


numero = Numeros()
print(numero.primo(9))
print(numero.potencia(2, 4))
print(numero.fibonnacci(5))
print(numero.perfecto(6))
print(numero.abundante(12))

print(numero.narcisista(4))
print(numero.narcisista(153))
print(numero.narcisista(370))
print(numero.narcisista(371))
print(numero.narcisista(200))

print(numero.munchausen(0))
print(numero.munchausen(3435))
print(numero.munchausen(123))
print(numero.munchausen(752))
print(numero.munchausen(34))
print("----------------")
print(numero.automorficos(25))
print(numero.harshad(-20))
print(numero.harshad(18))
print(numero.cuadrado_perfecto(20))
print(numero.cuadrado_perfecto(-20))
