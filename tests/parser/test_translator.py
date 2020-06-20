from validator.parser.translator import Translator
from validator import rules as R
from validator import exceptions as exc
import pytest

"""
1) []
2) 
"""

# This method loops through classes and checks its instance
def instanceChecker(target_str, result_arr, flag):
    assert_flag = True
    # Make target easy to read
    if not flag:
        target_arr = target_str.split("|")
    else:
        target_arr = target_str

    for _ in range(0, len(target_arr)):
        if ":" in target_arr[_]:
            target_arr[_] = target_arr[_].split(":")[0]

    # Check instances taken from rules
    for _ in range(0, len(result_arr)):
        assert_flag = assert_flag and (
            isinstance(result_arr[_], R.__all__[target_arr[_]])
        )
    return assert_flag


def test_translator_basic():
    min_value, max_value = 10, 40
    target_str = "required"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = f"required|min:{min_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = f"required|min:{min_value}|max:{max_value}|mail"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = f"mail|between:{min_value},{max_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)


# checking second step
def test_translator_mid():
    min_value, max_value = 12, 32

    target_str = ["required"]
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, True)

    target_str = ["required", "mail", f"max:{max_value}"]
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, True)

    target_str = ["required", f"min:{min_value}", f"max:{max_value}"]
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, True)

    target_str = ["required", f"between:{min_value},{max_value}"]
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, True)


def test_translator_single():
    # between
    min_value, max_value = 10, 20
    target_str = f"between:{min_value},{max_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].max == max_value
    assert result_arr[0].min == min_value

    # min
    target_str = f"min:{min_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].min == min_value

    # max
    target_str = f"max:{max_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].max == max_value


# many features checking value
def test_translator_many():
    min_value, max_value = 10, 20
    # between min
    target_str = f"between:{min_value},{max_value}|min:{min_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].max == max_value
    assert result_arr[0].min == min_value
    assert result_arr[1].min == min_value

    # betweeen max
    target_str = f"between:{min_value},{max_value}"
    target_str += f"|max:{max_value}"
    target_str = f"between:{min_value},{max_value}|max:{max_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()

    assert result_arr[0].max == max_value
    assert result_arr[0].min == min_value
    assert result_arr[1].max == max_value

    # betweeen max min
    target_str = f"between:{min_value},{max_value}|min:{min_value}"
    target_str += f"|max:{max_value}"
    translator = Translator(target_str)
    result_arr = translator.translate()

    assert result_arr[0].max == max_value
    assert result_arr[0].min == min_value
    assert result_arr[1].min == min_value
    assert result_arr[2].max == max_value


# In this method we will write bad tests for our translator method.
# Checking for NoRuleError
def test_bad_01_string():
    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = f"min:{-10}|maximum:20"
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = f"min:{-10}|maximum:20"
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = f"min:{-10}|max{20}|interval:10,20"
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = f"min:{-10}|max{20}|required_mail"
        Translator(target_str).translate()

    # some random characters.
    with pytest.raises(exc.NoRuleError):
        target_str = "./']\n"
        Translator(target_str).translate()

    # some random characters.
    with pytest.raises(exc.NoRuleError):
        target_str = "required?"
        Translator(target_str).translate()

    # some random characters.
    with pytest.raises(exc.NoRuleError):
        target_str = "min.{10}:max{20}"
        Translator(target_str).translate()


# Checking for NoRuleError with array
def test_bad_01_array():
    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = [f"min:{-10}", f"maximum:20"]
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = [f"min:{-10}", "maximum:20"]
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = [f"min:{-10}", "max{20}", "interval:10,20"]
        Translator(target_str).translate()

    # some non-exists classes.
    with pytest.raises(exc.NoRuleError):
        target_str = [f"min:{-10}", "max{20}", "required_mail"]
        Translator(target_str).translate()

    # some random characters.
    with pytest.raises(exc.NoRuleError):
        target_str = ["./']\n"]
        Translator(target_str).translate()

    # some random characters.
    with pytest.raises(exc.NoRuleError):
        target_str = ["required?"]
        Translator(target_str).translate()


# Checking for ArgsCountError and valueError
# for max, min, between args
def test_bad_02():
    # Many min arg
    with pytest.raises(exc.ArgsCountError):
        target_str = f"min:{1},{2}|max{10}"
        Translator(target_str).translate()

    with pytest.raises(exc.ArgsCountError):
        target_str = f"min:{1},{2}|max{10}"
        Translator(target_str).translate()

    # few between arg
    with pytest.raises(exc.ArgsCountError):
        target_str = f"between:|max{10}"
        Translator(target_str).translate()

    # min zero arg
    with pytest.raises(ValueError):
        target_str = f"min:|max{10}"
        Translator(target_str).translate()

    # max zero arg
    with pytest.raises(ValueError):
        target_str = f"max:|min{10}"
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = f"min:{10},{20},{30}|max{10}"
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = f"between:{10},{20},{30}|max{10}"
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = f"between:{10},{20}|max:{10},{20}"
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = "required:a"
        Translator(target_str).translate()


# Checking for ArgsCountError and valueError
# for max, min, between args
def test_bad_02_array():
    # Many min arg
    with pytest.raises(exc.ArgsCountError):
        target_str = [f"min:{1},{2}", f"max{10}"]
        Translator(target_str).translate()

    with pytest.raises(exc.ArgsCountError):
        target_str = [f"min:{1},{2}", f"max{10}"]
        Translator(target_str).translate()

    # few between arg
    with pytest.raises(exc.ArgsCountError):
        target_str = [f"between:", f"max{10}"]
        Translator(target_str).translate()

    # min zero arg
    with pytest.raises(ValueError):
        target_str = [f"min:", f"max{10}"]
        Translator(target_str).translate()

    # max zero arg
    with pytest.raises(ValueError):
        target_str = [f"max:", f"min{10}"]
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = [f"min:{10},{20},{30}", f"max{10}"]
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = [f"between:{10},{20},{30}", f"max{10}"]
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = [f"between:{10},{20}", f"max:{10},{20}"]
        Translator(target_str).translate()

    # many arg
    with pytest.raises(exc.ArgsCountError):
        target_str = ["required:a"]
        Translator(target_str).translate()


# Checking for attribute error and UnknownTranslatorArgError
def test_bad_03():
    # Bad R class
    with pytest.raises(AttributeError):
        target_str = [R.Required(), R.Min(18), R.anyclass(30)]
        Translator(target_str).translate()

    # Random class
    with pytest.raises(exc.UnknownTranslatorArgError):
        target_str = [R.Required(), R.Min(18), ConnectionError(30)]
        Translator(target_str).translate()

    # Random texts
    with pytest.raises(exc.UnknownTranslatorArgError):
        target_str = [123456789, "random text", "bad test", 5.5]
        Translator(target_str).translate()

    # Bad R class
    with pytest.raises(AttributeError):
        target_str = [R.Requireds()]
        Translator(target_str).translate()
