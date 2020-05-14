from validator.__parser__.translator import Translator
from validator import rules as R

r = range


# This method loops through classes and checks its instance
def instanceChecker(target_str, result_arr, flag):
    assert_flag = True
    # Make target easy to read
    if not flag:
        target_arr = target_str.split("|")
    else:
        target_arr = target_str

    target_arr = [_.capitalize() for _ in target_arr]
    for _ in r(0, len(target_arr)):
        if ":" in target_arr[_]:
            target_arr[_] = target_arr[_].split(":")[0]

    # Check instances taken from rules
    for _ in r(0, len(result_arr)):
        assert_flag = assert_flag and (
            isinstance(result_arr[_], R.__all__[target_arr[_]])
        )
    return assert_flag


def test_translator_basic():
    target_str = "required"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = "required|min:30"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = "required|min:30|max:40|mail"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)

    target_str = "mail|between:10,20"
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert instanceChecker(target_str, result_arr, False)


def test_translator_mid():
    target_arr = [
        ["required"],
        ["required", "mail", "max:30"],
        ["required", "min:20", "max:30"],
        ["required", "between:10,20"],
    ]
    for _ in target_arr:
        target_str = _
        translator = Translator(target_str)
        result_arr = translator.translate()
        assert instanceChecker(target_str, result_arr, True)


def test_translator_single():
    min_value, max_value = 10, 20
    target_str = "between:" + str(min_value) + "," + str(max_value)
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert (result_arr[0].max_value == max_value) and (
        result_arr[0].min_value == min_value
    )

    # min
    target_str = "min:" + str(min_value)
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].min_value == min_value

    # max
    target_str = "max:" + str(max_value)
    translator = Translator(target_str)
    result_arr = translator.translate()
    assert result_arr[0].max_value == max_value


# many features checking value
def test_translator_many():
    min_value, max_value = 10, 20
    # between min
    target_str = (
        "between:" +
        str(min_value) +
        "," +
        str(max_value) +
        "|min:" +
        str(min_value))
    translator = Translator(target_str)
    result_arr = translator.translate()

    assert (
        (result_arr[0].max_value == max_value)
        and (result_arr[0].min_value == min_value)
        and ((result_arr[1].min_value == min_value))
    )

    # betweeen max
    target_str = (
        "between:" +
        str(min_value) +
        "," +
        str(max_value) +
        "|max:" +
        str(max_value))
    translator = Translator(target_str)
    result_arr = translator.translate()

    assert (
        (result_arr[0].max_value == max_value)
        and (result_arr[0].min_value == min_value)
        and ((result_arr[1].max_value == max_value))
    )

    # betweeen max min
    target_str = (
        "between:"
        + str(min_value)
        + ","
        + str(max_value)
        + "|max:"
        + str(max_value)
        + "|min:"
        + str(min_value)
    )
    translator = Translator(target_str)
    result_arr = translator.translate()

    assert (
        (result_arr[0].max_value == max_value)
        and (result_arr[0].min_value == min_value)
        and (result_arr[1].max_value == max_value)
        and (result_arr[2].min_value == min_value)
    )
