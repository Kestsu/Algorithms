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


# def ordena_string(string):
#     lista_string_ordenada = []

#     for i in range(len(string)):
#         lista_string_ordenada.append(min(string))
#         string = string.replace(min(string), "", 1)

#     return ''.join(lista_string_ordenada)


def merge_sort(input_list: list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left == []:
        result += right
    else:
        result += left

    return result


def is_anagram(first_string, second_string):
    yes_or_no = False

    if first_string != '':
        first_string = merge_sort(list(first_string.lower()))
    if second_string != '':
        second_string = merge_sort(list(second_string.lower()))
    if first_string == '' or second_string == '':
        return (''.join(first_string), ''.join(second_string), yes_or_no)

    if first_string == second_string:
        yes_or_no = True
    return (''.join(first_string), ''.join(second_string), yes_or_no)


if __name__ == '__main__':
    print(is_anagram('pedra', 'perdaaa'))
