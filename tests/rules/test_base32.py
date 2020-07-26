from validator.rules import Base32


def test_base32_01():
    assert Base32().check("MFZWIZQ=")

    assert Base32().check("MFRA====")

    assert Base32().check("MZXXE3LBM5SQ====")

    assert Base32().check("MZXXE3LBM5SQ====")

    assert Base32().check("GEZDGNBVGY3TQ===")


def test_base32_02():
    assert not Base32().check("hbsdf")

    assert not Base32().check("!@#")

    assert not Base32().check("bfjhsdf HGHG &^&&")

    assert not Base32().check("29i03r09j....")

    assert not Base32().check("olgak9999")
