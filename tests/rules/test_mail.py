from validator.rules import Mail


def test_mail_01():
    assert Mail().check("sdar@quecompde.ga")

    assert Mail().check("awavufo@yopmail.com")

    assert Mail().check("nawuteny@gmail.com")

    assert Mail().check("rapattullatta@yandex.ru")


def test_mail_02():
    assert not Mail().check("sdar@quecompde")

    assert not Mail().check("@yopmail.com")

    assert not Mail().check("nawuteny-6603@com")

    assert not Mail().check("rapattullatta-2328@z")
