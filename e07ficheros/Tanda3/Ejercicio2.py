import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # This alphabet has 26 letters.


def is_valid_base(base):
    try:
        int_base = int(base)
        if int_base > 25 or int_base < -25:
            raise ValueError
    except ValueError:
        print("Base de codificación no válida.")
        exit(1)
    return int_base


def base_input_menu():
    given_base = input("Introduce una base de codificación para el documento: ")
    return is_valid_base(given_base)


def encrypt_text(text):
    base = base_input_menu()
    return cypher_in_caesar(base, text)


def cypher_in_caesar(caesar_degree, sentence):
    global ALPHABET
    width_sentence = len(sentence)
    alphabet = ALPHABET
    switch_lower = False
    alphabet_position = 0

    for n in range(0, width_sentence):
        chosen_character = sentence[n]
        if chosen_character.isalpha() is True and ord(chosen_character) < 123:
            if chosen_character.islower() is True:
                chosen_character = chosen_character.upper()
                switch_lower = True
            for o in range(0, 26):
                if chosen_character == alphabet[o]:
                    alphabet_position = o
                    break
            caesar_addition = alphabet_position + caesar_degree
            if caesar_addition > (len(alphabet) - 1):
                caesar_addition = (caesar_addition % (len(alphabet)))
            elif caesar_addition < 0:
                caesar_addition = 26 + caesar_addition
            cyphered_letter = alphabet[caesar_addition]
            if switch_lower is True:
                cyphered_letter = cyphered_letter.lower()
                switch_lower = False
            sentence = sentence[:n] + cyphered_letter + sentence[(n+1):]
    return sentence


def return_doc_encryption(document):
    with open(document, "rt", encoding="utf8") as source:
        text1_content = source.read()
        return encrypt_text(text1_content)


def rewrite_document(given_text, document2):
    with open(document2, "wt", encoding="utf8") as destination:
        print(given_text, file=destination)


def full_encrypting(text1, text2):
    try:
        doc_encryption = return_doc_encryption(text1)
        try:
            rewrite_document(doc_encryption, text2)
        except FileNotFoundError or PermissionError:
            print(f"ERROR 3: No se ha podido escribir ningún archivo {text2}")
            exit(1)
    except FileNotFoundError:
        print(f"ERROR 2: No se ha encontrado ningún archivo {text1}")
        exit(1)


def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("ERROR 1: Número de parámetros incorrecto.")
        exit(1)
    elif len(sys.argv) == 2:
        allow_rewrite_key = input("No se ha introducido ningún nombre de fichero de destino. Introduzca Y si quiere"
                                  " sobreescribir el fichero arriba mencionado: ")
        if allow_rewrite_key == "y" or allow_rewrite_key == "Y":
            only_doc_name = sys.argv[1]
            full_encrypting(only_doc_name, only_doc_name)
            print(f"El archivo {only_doc_name} se ha sobreescrito con éxito.")
        else:
            exit(1)
    else:
        source_file_name = sys.argv[1]
        destination_file_name = sys.argv[2]
        full_encrypting(source_file_name, destination_file_name)


if __name__ == "__main__":
    main()
