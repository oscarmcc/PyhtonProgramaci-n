def print_title(title, char_decorator='-'):
    print(char_decorator * len(title))
    print(title)
    print(char_decorator * len(title))


def menu(options):
    max_len_word = options[0]
    for n in range(1, len(options)):
        if len(max_len_word) < len(options[n]):
            max_len_word = options[n]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    print('-' * (len(max_len_word) + 3))


def input_int():
    while True:
        try:
            number = int(input('Introduce un número entero '))
            return number
        except ValueError:
            print('Por favor introduce un número válido')


def remove_duplicates_in_array(array):
    any_duplicates = []
    for number in array:
        if number not in any_duplicates:
            any_duplicates.append(number)
    return any_duplicates


def invert_words_from_array(array):
    return [word[::-1] for word in array]


def identify_matrix(n):
    result = []
    for i in range(n):
        matrix = []
        for j in range(n):
            if i == j:
                matrix.append(1)
            else:
                matrix.append(0)
        result.append(matrix)
    return result


def transposed_matrix(array):
    result = []
    num_rows = len(array)
    num_cols = len(array[0])
    for j in range(num_cols):
        row = [array[i][j] for i in range(num_rows)]
        result.append(row)
    return result


if __name__ == '__main__':
    print_title('Hola Caracola')
    print(menu(['Hola Caracola', '', 'corazón', 'esternocleidomastoideo es un músculo']))
    print(remove_duplicates_in_array([1, 2, 2, 4, 4, 8, 1]))
    print(invert_words_from_array(['hola', 'caracola']))
    print(identify_matrix(3))
    print(transposed_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
