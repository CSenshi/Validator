from validator import Validator, validate, validate_many, rules as R

# !!! TEST : Class Validator !!! #
def test_01_validator_simple():
    request = {"age": 23}
    rule = {"age": [R.Integer, R.Min(18)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 13}
    rule = {"age": [R.Integer, R.Min(18)]}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": 13}
    rule = {"age": [R.Integer, R.Max(18)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"name": "Jon"}
    rule = {"name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert result

    request = {"name": ""}
    rule = {"name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert not result


def test_02_validator_simple():
    request = {"age": 23}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 33}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)]}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": 23, "name": "Jon"}
    rule = {"age": [R.Integer, R.Min(18)], "name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 23, "name": ""}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)], "name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert not result


def test_03_validator_error_msg():
    request = {"age": 100}
    rule = {"age": [R.Integer, R.Between(18, 90)]}
    val = Validator(request, rule)
    result = val.validate()
    errors = val.get_error_messages()
    assert not result
    assert "age" in errors.keys()
    assert "Between" in errors["age"].keys()

    request = {"age": 28, "name": "John", "surname": "Krasinski"}
    rule = {
        "age": [R.Integer, R.Between(18, 50)],
        "name": [R.Required()],
        "surname": [R.Required(), R.Mail()],
    }
    val = Validator(request, rule)
    result = val.validate()
    errors = val.get_error_messages()

    # Test General
    assert not result
    assert len(errors) == 1
    assert "surname" in errors.keys()

    # Test Error 1
    mail_err = errors["surname"]
    assert len(mail_err) == 1
    assert "Mail" in mail_err.keys()


def test_04_validator_error_msg():
    request = {
        "age": 53,
        "name": "Peter",
        "surname": "Griffin",
        "profession": "",
        "mail": "petergriffin.com",
    }
    rule = {
        "age": [R.Integer, R.Between(18, 50), R.Required()],
        "name": [R.Required()],
        "surname": [R.Required()],
        "profession": [R.Required, R.Mail],
        "mail": [R.Required(), R.Mail()],
    }
    val = Validator(request, rule)
    result = val.validate()
    errors = val.get_error_messages()

    # Test General
    assert not result
    assert len(errors) == 3
    assert "age" in errors
    assert "profession" in errors
    assert "mail" in errors

    # Test Error 1
    age_err = errors["age"]
    assert len(age_err) == 1
    assert "Between" in age_err

    # Test Error 2
    profession_err = errors["profession"]
    assert len(profession_err) == 2
    assert "Required" in profession_err
    assert "Mail" in profession_err

    # Test Error 3
    mail_err = errors["mail"]
    assert len(mail_err) == 1
    assert "Mail" in mail_err


def test_05_validator_empty():
    # Checking for empty rules to work
    request = {
        "age": 53,
        "name": "Peter",
        "surname": "Griffin",
        "profession": "brewer",
        "mail": "peter@griffin.com",
    }
    rule = {
        "age": "",
        "name": [""],
        "surname": [],
        "profession": [R.Required],
        "mail": [R.Required(), R.Mail()],
    }
    val = Validator(request, rule)
    result = val.validate()

    assert result

    # Testing if other rules still work with empty ones
    request["mail"] = "pg.com"
    val = Validator(request, rule)
    result = val.validate()

    assert not result


# !!! TEST : Function validate !!! #
def test_06_validate_simple():
    request = {"age": 23}
    rule = {"age": [R.Integer, R.Min(18)]}
    result = validate(request, rule)
    assert result

    request = {"age": 13}
    rule = {"age": [R.Integer, R.Min(18)]}
    result = validate(request, rule)
    assert not result

    request = {"age": 13}
    rule = {"age": [R.Integer, R.Max(18)]}
    result = validate(request, rule)
    assert result

    request = {"name": "Jon"}
    rule = {"name": [R.Required()]}
    result = validate(request, rule)
    assert result

    request = {"name": ""}
    rule = {"name": [R.Required()]}
    result = validate(request, rule)
    assert not result


def test_07_validate_simple():
    request = {"age": 23}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)]}
    result = validate(request, rule)
    assert result

    request = {"age": 33}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)]}
    result = validate(request, rule)
    assert not result

    request = {"age": 23, "name": "Jon"}
    rule = {"age": [R.Integer, R.Min(18)], "name": [R.Required()]}
    result = validate(request, rule)
    assert result

    request = {"age": 23, "name": ""}
    rule = {"age": [R.Integer, R.Min(18), R.Max(30)], "name": [R.Required()]}
    result = validate(request, rule)
    assert not result


def test_08_validate_error_msg():
    request = {"age": 100}
    rule = {"age": [R.Integer, R.Between(18, 90)]}
    result, validated_data, errors = validate(request, rule, return_info=True)
    assert not result
    assert "age" in errors.keys()
    assert "Between" in errors["age"].keys()

    request = {"age": 28, "name": "John", "surname": "Krasinski"}
    rule = {
        "age": [R.Integer, R.Between(18, 50)],
        "name": [R.Required()],
        "surname": [R.Required(), R.Mail()],
    }
    result, validated_data, errors = validate(request, rule, return_info=True)

    # Test General
    assert not result
    assert len(errors) == 1
    assert "surname" in errors.keys()

    # Test Error 1
    mail_err = errors["surname"]
    assert len(mail_err) == 1
    assert "Mail" in mail_err.keys()


def test_09_validate_error_msg():
    request = {
        "age": 53,
        "name": "Peter",
        "surname": "Griffin",
        "profession": "",
        "mail": "petergriffin.com",
    }
    rule = {
        "age": [R.Integer, R.Between(18, 50), R.Required()],
        "name": [R.Required()],
        "surname": [R.Required()],
        "profession": [R.Required, R.Mail],
        "mail": [R.Required(), R.Mail()],
    }
    result, validated_data, errors = validate(request, rule, return_info=True)

    # Test General
    assert not result
    assert len(errors) == 3
    assert "age" in errors
    assert "profession" in errors
    assert "mail" in errors

    # Test Error 1
    age_err = errors["age"]
    assert len(age_err) == 1
    assert "Between" in age_err

    # Test Error 2
    profession_err = errors["profession"]
    assert len(profession_err) == 2
    assert "Required" in profession_err
    assert "Mail" in profession_err

    # Test Error 3
    mail_err = errors["mail"]
    assert len(mail_err) == 1
    assert "Mail" in mail_err


# !!! TEST : Function validate_many !!! #
def test_10_validate_many():
    requests = [{"age": 19}, {"age": 20}, {"age": 21}, {"age": 22}]
    rule = {"age": [R.Integer, R.Min(18)]}
    result = validate_many(requests, rule)
    assert result

    requests = [{"age": 11}, {"age": 12}, {"age": 13}, {"age": 14}]
    rule = {"age": [R.Integer, R.Min(18)]}
    result = validate_many(requests, rule)
    assert not result

    requests = [{"age": 11}, {"age": 12}, {"age": 13}, {"age": 14}]
    rule = {"age": [R.Integer, R.Max(18)]}
    result = validate_many(requests, rule)
    assert result

    requests = [{"age": 21}, {"age": 22}, {"age": 23}, {"age": 24}]
    rule = {"age": [R.Integer, R.Max(18)]}
    result = validate_many(requests, rule)
    assert not result

    requests = [{"name": "Jon"}, {"name": "Rob"}, {"name": "Greg"}, {"name": "Tom"}]
    rule = {"name": "required|min:3"}
    result = validate_many(requests, rule)
    assert result

    requests = [{"name": "Jon"}, {"name": ""}, {"name": ""}, {"name": "Tom"}]
    rule = {"name": [R.Required()]}
    result = validate_many(requests, rule)
    assert not result


def test_11_validate_many_errors_msg():
    requests = [{"age": 11}, {"age": 12}, {"age": 13}, {"age": 14}]
    rule = {"age": [R.Integer, R.Min(18)]}
    result, _, errors = validate_many(requests, rule, True)
    assert not result
    assert 4 == len(errors)
    assert "age" in errors[0]
    assert "age" in errors[1]
    assert "age" in errors[2]
    assert "age" in errors[3]
    assert "Min" in errors[0]["age"]
    assert "Min" in errors[1]["age"]
    assert "Min" in errors[2]["age"]
    assert "Min" in errors[3]["age"]
    assert "Got: 11" in errors[0]["age"]["Min"]
    assert "Got: 12" in errors[1]["age"]["Min"]
    assert "Got: 13" in errors[2]["age"]["Min"]
    assert "Got: 14" in errors[3]["age"]["Min"]

    requests = [{"age": 11}, {"age": 12}, {"age": 23}, {"age": 14}]
    rule = {"age": [R.Integer, R.Max(18)]}
    result, _, errors = validate_many(requests, rule, True)
    assert not result
    assert 4 == len(errors)
    assert {} == errors[0]
    assert {} == errors[1]
    assert {} == errors[3]
    assert "age" in errors[2]
    assert "Max" in errors[2]["age"]
    assert "Got: 23" in errors[2]["age"]["Max"]

    requests = [{"name": "Jon"}, {"name": ""}, {"name": ""}, {"name": "Tom"}]
    rule = {"name": [R.Required()]}
    result, _, errors = validate_many(requests, rule, True)
    assert not result
    assert 4 == len(errors)
    assert {} == errors[0]
    assert "name" in errors[1]
    assert "name" in errors[2]
    assert {} == errors[3]
    assert "Required" in errors[1]["name"]
    assert "Required" in errors[2]["name"]
    assert "Field was empty" in errors[1]["name"]["Required"]
    assert "Field was empty" in errors[2]["name"]["Required"]


def test_12_validate_many_errors_msg():
    requests = [
        {"first_name": "Jon", "last_name": "Doe", "age": 40},
        {"first_name": "", "last_name": "Doe", "age": 40},
        {"first_name": "Jon", "last_name": "", "age": 40},
        {"first_name": "Jon", "last_name": "Doe", "age": 10},
        {"first_name": "", "last_name": "", "age": 10},
    ]
    rule = {
        "first_name": R.Required,
        "last_name": R.Required,
        "age": [R.Integer, R.Min(18)],
    }

    result, _, errors = validate_many(requests, rule, True)

    assert not result
    assert len(errors) == 5

    assert len(errors[0]) == 0

    assert len(errors[1]) == 1
    assert "first_name" in errors[1]

    assert len(errors[2]) == 1
    assert "last_name" in errors[2]

    assert len(errors[3]) == 1
    assert "age" in errors[3]

    assert len(errors[4]) == 3
    assert "first_name" in errors[4]
    assert "last_name" in errors[4]
    assert "age" in errors[4]


#  !!! TEST: validated data !!! #


def test_13_validated_data():
    req = {"a": 1, "b": 2, "c": 3}
    rules = {"a": "required"}

    val = Validator(req, rules)
    result = val.validate()
    validated_data = val.get_validated_data()

    assert result
    assert validated_data == {"a": 1}

    reqs = {
        "first_name": "Jon",
        "last_name": "Doe",
        "age": 33,
        "mail": "jondoe@gmail.com",
        "_token": "WpH0UPfy0AXzMtK2UWtJ",
        "_cookie_data": "e9Uixp8hzUySy6bw3MuZ",
        "_session_id": "ZB7q7uIVdWBKgSCSSWAa",
    }
    rule = {
        "first_name": "required",
        "last_name": "required",
        "age": "required|min:18",
        "mail": "required|mail",
    }

    val = Validator(reqs, rule)
    result = val.validate()
    validated_data = val.get_validated_data()

    assert result
    assert len(validated_data) == 4

    assert "first_name" in validated_data
    assert "last_name" in validated_data
    assert "age" in validated_data
    assert "mail" in validated_data
    assert "_token" not in validated_data
    assert "_cookie_data" not in validated_data
    assert "_session_id" not in validated_data


def test_14_validated_data_many():
    reqs = [
        {"first_name": "Jon", "last_name": "Doe", "age": 33},
        {
            "first_name": "Nick",
            "last_name": "Bush",
            "age": 23,
            "_token": "Ou1WQdWbyTuy4y8jazwA",
        },
        {
            "first_name": "John",
            "last_name": "Watson",
            "age": 30,
            "_token": "Ou1WQdWbyTuy4y8jazwA",
        },
        {
            "first_name": "May",
            "last_name": "Afferson",
            "age": 40,
            "_cookie": "7Juhm38k8eBgo3HVDFKC",
        },
    ]

    rule = {"first_name": "required", "last_name": "required", "age": "min:18"}

    result, validated_datas, _ = validate_many(reqs, rule, return_info=True)

    # result should be True
    assert result

    # all of validated data should contain only first_name, last_name and age
    for data in validated_datas:
        assert ("first_name" in data) and ("last_name" in data) and ("age" in data)
        assert ("_token" not in data) and ("_cookie" not in data)
