from validator.rules import Mail
from validator import validate


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


def test_mail_03_string():
    assert validate({"val": "sdar@quecompde.ga"}, {"val": "mail"})

    assert validate({"val": "peter@griffin.com"}, {"val": "mail"})

    assert not validate({"val": "jeje.ge"}, {"val": "mail"})

    assert not validate({"val": "name@com"}, {"val": "mail"})
