from validator.rules import Date
from validator import validate


def test_date_01():
    assert Date().check("23-1-1921")

    assert Date().check("1-23-1951")

    assert Date().check("3.4.13")

    assert Date().check("31.12.20")


def test_date_02():
    assert not Date().check("23-23-1921")

    assert not Date().check("1-023.0")

    assert not Date().check("32.1.132")

    assert not Date().check("31-3")


def test_date_03_string():
    assert validate({"date": "23-1-1921"}, {"date": "date"})

    assert validate({"date": "31.12.20"}, {"date": "date"})

    assert not validate({"date": "31-3"}, {"date": "date"})
