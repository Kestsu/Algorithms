from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    try:
        encrypt_message("ABCDEF", '9999999')
    except TypeError:
        raise TypeError("tipo inválido para key")

    try:
        encrypt_message(9999999, 1)
    except TypeError:
        raise TypeError("tipo inválido para message")

    assert encrypt_message("ABCDEF", 1) == "A_FEDCB"
    assert encrypt_message("ABCDEF", 2) == "FEDC_BA"
    assert encrypt_message("ABCDEF", 9) == "FEDCBA"
