from validator.rules import UUIDv4
from validator import validate


def test_uuidv4_01():
    assert UUIDv4().check("0d713a92-8406-489e-b0bd-24af3d1da2fa")

    assert UUIDv4().check("e96e74e2-f106-4ad7-9467-322ba6cb3c78")

    assert UUIDv4().check("f17fcd28-3dbc-41ff-9a27-545af3e87f0d")


def test_uuidv4_02():
    assert not UUIDv4().check("dasda@rergetert")

    assert not UUIDv4().check("[131]")

    assert not UUIDv4().check(
        ["0d713a92-8406-489e-b0bd-24af3d1da2fa", "e96e74e2-f106-4ad7-9467-322ba6cb3c78"]
    )

    assert not UUIDv4().check("addee3a2-c941-11ea-bbd4-ab0012dacf6c")

    assert not UUIDv4().check("b3bf2958-c941-11ea-9e44-2fd4f688a758")


def test_uuidv4_03():
    assert validate({"val": "0d713a92-8406-489e-b0bd-24af3d1da2fa"}, {"val": "uuidv4"})

    assert validate({"val": "e96e74e2-f106-4ad7-9467-322ba6cb3c78"}, {"val": "uuidv4"})

    assert not validate(
        {
            "val": [
                "0d713a92-8406-489e-b0bd-24af3d1da2fa",
                "e96e74e2-f106-4ad7-9467-322ba6cb3c78",
            ]
        },
        {"val": "uuidv4"},
    )

    assert not validate(
        {"val": "addee3a2-c941-11ea-bbd4-ab0012dacf6c"}, {"val": "uuidv4"}
    )
