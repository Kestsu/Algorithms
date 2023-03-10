def encrypt_message(message: str, key: int):

    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


if __name__ == "__main__":
    print(encrypt_message("ABCDEF", 1))  # A_FEDCB
    print(encrypt_message("ABCDEF", 2))  # FEDC_BA
    print(encrypt_message("ABCDEF", 9))  # FEDCBA
    assert encrypt_message("OI", 1) == "O_I"
    assert encrypt_message("OIO", 2) == "O_IO"
    assert encrypt_message("OIO", 3) == "OIO"
