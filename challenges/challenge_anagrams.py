# def sort_string(string):
#     characters = list(string)
# # Cria uma lista de caracteres a partir da string.
#     for i in range(len(characters)):
#         # Encontra o caractere mais pequeno entre os caracteres da lista.
#         smallest_char = min(characters[i:])
#         # Encontra o índice do caractere mais pequeno.
#         smallest_char_index = characters.index(smallest_char)
#         # Troca o caractere da lista no índice atual com mais pequeno.
#         characters[i], characters[smallest_char_index] = characters[
#             smallest_char_index], characters[i]

#     return ''.join(characters)


def ordena_string(string):
    lista_string_ordenada = []

    for i in range(len(string)):
        lista_string_ordenada.append(min(string))
        string = string.replace(min(string), "", 1)

    return ''.join(lista_string_ordenada)


def is_anagram(first_string, second_string):
    yes_or_no = False

    if first_string != '':
        first_string = ordena_string(first_string.lower())
    if second_string != '':
        second_string = ordena_string(second_string.lower())

    if first_string == '' or second_string == '':
        return (first_string, second_string, yes_or_no)

    if first_string == second_string:
        yes_or_no = True
    return (first_string, second_string, yes_or_no)


if __name__ == '__main__':
    print(is_anagram('', ''))
