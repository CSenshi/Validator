from validator.rules import Binary

# True test
def test_binary_01():
    assert Binary().check("0")

    assert Binary().check("000000")

    assert Binary().check("1")

    assert Binary().check("111111")

    assert Binary().check("000111")

    assert Binary().check("010101010010")

    assert Binary().check("0b010101010010")

    assert Binary().check("0b1")


def test_binary_02():
    assert not Binary().check("b01")

    assert not Binary().check("b0101010")

    assert not Binary().check("abrakadabra")

    assert not Binary().check("01201021")

    assert not Binary().check("1231231")

    assert not Binary().check("000002")

    assert not Binary().check("2")

    assert not Binary().check("0b111112000")
