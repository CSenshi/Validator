from validator.rules import JSON


def test_json_01():
    assert JSON().check("{}")

    assert JSON().check('{ "age":100}')

    assert JSON().check('{"age":100 }')

    assert JSON().check(
        '[ {"name":"Ram", "email":"Ram@gmail.com"},  {"name":"Bob", "email":"bob32@gmail.com"}]'
    )

    assert JSON().check(
        '{"data" : [ {"name":"Ram", "email":"Ram@gmail.com"},  {"name":"Bob", "email":"bob32@gmail.com"}]}'
    )

    assert JSON().check('{"age":100 }')


def test_json_02():
    assert not JSON().check("{asdf}")

    assert not JSON().check("{'age':100 }")

    assert not JSON().check("nawuteny-6603@com")

    assert not JSON().check(
        '{[ {"name":"Ram", "email":"Ram@gmail.com"},  {"name":"Bob", "email":"bob32@gmail.com"}]}'
    )

    assert not JSON().check(
        '{data : [ {"name":"Ram", "email":"Ram@gmail.com"},  {"name":"Bob", "email":"bob32@gmail.com"}]}'
    )

    assert not JSON().check([1, 3, 3])
