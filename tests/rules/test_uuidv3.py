from validator.rules import UUIDv3
from validator import validate


def test_uuid_v3_01():
    assert UUIDv3().check("f6c83289-fa9d-3ff0-94d4-1bd6ba6323e2")
    assert UUIDv3().check("e2b83871-74c7-3ccd-82c1-4c361d631051")
    assert UUIDv3().check("57021542-a02e-3989-8648-f6f2a73aff60")


def test_uuid_v3_02():
    assert not UUIDv3().check("zgogi15@freeuni")
    assert not UUIDv3().check("[131]")
    # uuid version 4 and 1
    assert not UUIDv3().check(
        ["f49612d0-c9c2-11ea-8f3c-000000000000", "60e637fc-eeb9-40f7-a801-f8b36d3cdfd3"]
    )
    # uuid version 5
    assert not UUIDv3().check("32597292-ffee-5208-89e5-c6edd636a4a8")
    # uuid version 1
    assert not UUIDv3().check("9e337c6a-c9c3-11ea-89ae-000000000000")


def test_uuid_v3_03():
    assert validate({"val": "f6c83289-fa9d-3ff0-94d4-1bd6ba6323e2"}, {"val": "UUIDv3"})
    assert validate({"val": "f6c83289-fa9d-3ff0-94d4-1bd6ba6323e2"}, {"val": "UUIDv3"})
    assert not validate(
        {
            "val": [
                "db168366-c9c3-11ea-bc9e-000000000000",
                "198047cd-39c3-57be-8da2-7a35eb3c5200",
            ]
        },
        {"val": "UUIDv3"},
    )

    assert not validate(
        {"val": "074eaa42-79e8-4bbe-b396-e44e9d7dffaa"}, {"val": "UUIDv3"}
    )
