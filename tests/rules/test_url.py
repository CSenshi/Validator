from validator.rules import URL


def test_mail_01():
    assert URL().check("sdar.ge")

    assert URL().check("http://localhost:3000/")

    assert URL().check("http://123.0.0.1:3000/")

    assert URL().check("http://123.0.0.1:3000")

    assert URL().check("www.awavufo.com")

    assert URL().check("https://hangouts.google.com/")

    assert URL().check("ftp://yandex.ru")

    assert URL().check("https://docs.python.org/3/howto/regex.html?ad=13&aqwe=13#asd")


def test_mail_02():
    assert not URL().check(["1," "123"])

    assert not URL().check("@yopmail")

    assert not URL().check("1233")

    assert not URL().check(
        "https://docs.python.org/3/howto/regex.html?ad=13&&aqwe=13#asd"
    )
