from validator.rules import UUIDv1


def test_uuidv1_01():
    assert UUIDv1().check("0d14fbaa-8cd6-11e7-b2ed-28d244cd6e76")

    assert UUIDv1().check("799da764-c93b-11ea-87d0-0242ac130003")

    assert UUIDv1().check("95068962-c93b-11ea-87d0-0242ac130003")

    assert UUIDv1().check("99a8baee-c93b-11ea-87d0-0242ac130003")


def test_uuidv1_02():
    assert not UUIDv1().check("sdar@quecompde")

    assert not UUIDv1().check("[]")

    assert not UUIDv1().check(
        ["563ea4aa-c939-11ea-87d0-0242ac130003", "563ea4aa-c939-11ea-87d0-0242ac130003"]
    )

    assert not UUIDv1().check("bba617b4-364b-4a0d-9e96-cb8a24ef1bec")

    assert not UUIDv1().check("a3bb189e-8bf9-3888-9912-ace4e6543002")
