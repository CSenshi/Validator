from validator.parser.parser import Parser
from validator import rules as R


# checks if input dictionary has the same keys target dictionary
# and in those keys, the samme rules are written as an array
def instances_checker(input_dict, target_dict):
    for key in target_dict.keys():
        if input_dict[key] and len(input_dict[key]) == len(target_dict[key]):
            for i in range(len(input_dict[key])):
                if not isinstance(input_dict[key][i], target_dict[key][i].__class__):
                    return False
        else:
            return False

    # if all match, all is left to do, is to check if their lengths are the same
    return len(input_dict) == len(target_dict)


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
    assert parsed_rules[key][0].min == min_val
    assert parsed_rules[key][1].max == max_val


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
    assert parsed_rules[key1][0].min == min_val
    assert parsed_rules[key1][0].max == max_val

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

    assert parsed_rules[key1][1].max == max_val
    assert parsed_rules[key1][2].min == min_val
    assert parsed_rules[key2][1].min == min_val
    assert parsed_rules[key2][1].max == max_val


def test_parser_mixed_01():
    # checking abstract university student object rules
    rules = {
        "name": R.Required(),
        "suranme": R.Required,
        "university_mail": [R.Required, "mail"],
        "faculty_name": [R.Required],
        "current_semester": ["required", R.Min(1)],
        "credits_amount": [R.Required, R.Between(0, 240)],
        "credits_current_semester": [R.Min(0), R.Max(75)],
        "debt": [R.Max(0)],
    }
    parsed_rules_goal = {
        "name": [R.Required()],
        "suranme": [R.Required()],
        "university_mail": [R.Required(), R.Mail()],
        "faculty_name": [R.Required()],
        "current_semester": [R.Required(), R.Min(1)],
        "credits_amount": [R.Required(), R.Between(0, 240)],
        "credits_current_semester": [R.Min(0), R.Max(75)],
        "debt": [R.Max(0)],
    }
    parsed_rules = Parser(rules).parse()

    assert instances_checker(parsed_rules, parsed_rules_goal)
    assert parsed_rules["current_semester"][1].min == 1
    assert parsed_rules["credits_amount"][1].min == 0
    assert parsed_rules["credits_amount"][1].max == 240
    assert parsed_rules["credits_current_semester"][0].min == 0
    assert parsed_rules["credits_current_semester"][1].max == 75
    assert parsed_rules["debt"][0].max == 0


def test_parser_mixed_02():
    # checking abstract football match object rules
    rules = {
        "team1": "required",
        "team2": R.Required,
        "team1_goals": ["required", "mail"],
        "team2_goals": [R.Required],
        "offides": [R.Required()],
        "fouls": [R.Required()],
        "corner_kicks": "required|min:1",
        "penalties": ["max:0"],
        "yellow_cards": [R.Required(), R.Between(0, 240)],
        "red_cards": [R.Min(0), R.Max(75)],
    }
    parsed_rules_goal = {
        "team1": [R.Required()],
        "team2": [R.Required()],
        "team1_goals": [R.Required(), R.Mail()],
        "team2_goals": [R.Required()],
        "offides": [R.Required()],
        "fouls": [R.Required()],
        "corner_kicks": [R.Required(), R.Min(1)],
        "penalties": [R.Max(0)],
        "yellow_cards": [R.Required(), R.Between(0, 240)],
        "red_cards": [R.Min(0), R.Max(75)],
    }
    parsed_rules = Parser(rules).parse()

    assert instances_checker(parsed_rules, parsed_rules_goal)
    assert parsed_rules["corner_kicks"][1].min == 1
    assert parsed_rules["yellow_cards"][1].min == 0
    assert parsed_rules["yellow_cards"][1].max == 240
    assert parsed_rules["red_cards"][0].min == 0
    assert parsed_rules["red_cards"][1].max == 75
