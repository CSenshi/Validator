from validator.__parser__.parser import Parser
from validator import rules as R


def test_parser_text_simple():
    key = "firstName"
    rules = {key: "required"}
    parsed_rules = Parser(rules).parse()

    assert len(parsed_rules) == 1
    assert key in parsed_rules.keys()
    assert len(parsed_rules[key]) == 1
    assert isinstance(parsed_rules[key][0], R.Required)

    key = "age"
    min_val, max_val = 32, 18
    rules = {key: f"min:{min_val}|max:{max_val}"}
    parsed_rules = Parser(rules).parse()

    assert len(parsed_rules) == 1
    assert key in parsed_rules.keys()
    assert len(parsed_rules[key]) == 2
    assert isinstance(parsed_rules[key][0], R.Min)
    assert isinstance(parsed_rules[key][1], R.Max)
    assert parsed_rules[key][0].min_value == min_val
    assert parsed_rules[key][1].max_value == max_val


def test_parser_arrays_simple():
    key1, key2 = "credits_amount", "semester"
    min_val, max_val = 10, 100

    rules = {key1: [f"between:{min_val},{max_val}"], key2: ["required"]}
    parsed_rules = Parser(rules).parse()

    assert len(parsed_rules) == 2
    assert key1 in parsed_rules.keys()
    assert key2 in parsed_rules.keys()
    assert isinstance(parsed_rules[key1][0], R.Between)
    assert isinstance(parsed_rules[key2][0], R.Required)
    assert parsed_rules[key1][0].min_value == min_val
    assert parsed_rules[key1][0].max_value == max_val

    rules = {key1: [R.Required, R.Mail], key2: R.Required}
    parsed_rules = Parser(rules).parse()

    assert isinstance(parsed_rules[key1][0], R.Required)
    assert isinstance(parsed_rules[key1][1], R.Mail)
    assert isinstance(parsed_rules[key2][0], R.Required)

    min_val, max_val = -31, 1928
    rules = {
        key1: [R.Required(), R.Max(max_val), R.Min(min_val)],
        key2: [R.Mail(), R.Between(min_val, max_val)],
    }
    parsed_rules = Parser(rules).parse()

    assert isinstance(parsed_rules[key1][0], R.Required)
    assert isinstance(parsed_rules[key1][1], R.Max)
    assert isinstance(parsed_rules[key1][2], R.Min)
    assert isinstance(parsed_rules[key2][0], R.Mail)
    assert isinstance(parsed_rules[key2][1], R.Between)

    assert parsed_rules[key1][1].max_value == max_val
    assert parsed_rules[key1][2].min_value == min_val
    assert parsed_rules[key2][1].min_value == min_val
    assert parsed_rules[key2][1].max_value == max_val


def test_parser_mixed():
    pass
