from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("ABCDEF", 1) == "A_FEDCB"
    assert encrypt_message("ABCDEF", 2) == "FEDC_BA"
    # assert encrypt_message("ABCDEF", 9) == "FEDCBA"
    assert encrypt_message("OIO", 3) == "OIO"
    with pytest.raises(TypeError):
        encrypt_message("ABCDEF", "999999")
        encrypt_message(999999, 1)
    # with pytest.raises(TypeError, match="tipo inválido para message"):
