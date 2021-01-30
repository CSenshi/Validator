from validator.parser.parser import Parser
from validator import rules as R
from validator import exceptions as exc
from .rules_wrapper import RulesWrapper as RW

"""
Validator class takes 2 inputs:
1. request to be validated
2. rules to be validated with

Following class is responsible for validating request with given rules
"""


class Validator:
    def __init__(self, request, rules):
        self.request = request
        self.rules = Parser(rules).parse()
        self.errors = {}
        self.validated_data = {}

    def validate(self):
        # check for internal error (incorrect rules)
        if not self.check_rules():
            raise exc.RulesFormatError

        # 1. Initialize Rules Wrapper
        rw = RW(self.request, self.rules)

        # 2. Run validation
        rw.run()

        # 3. get errors
        self.errors = rw.get_errors()

        # 4. get validated data
        self.validated_data = rw.get_validated_data()

        # 5. return result
        return rw.get_result()

    def get_errors(self):
        # return error messages logged on validation
        return self.errors

    def get_validated_data(self):
        # return data that has been validated
        return self.validated_data

    def check_rules(self):
        # check for rules' type (should be dictionary)
        if not type(self.rules) is dict:
            False

        for _, value in self.rules.items():
            # check for dictionary's value's type (should be list)
            if not type(value) is list:
                False
            for rule in value:
                # check for each value being R.Rule class instance
                if not isinstance(rule, R.Rule):
                    False

        return True


def validate(req, rules, return_info=False):
    """
    Validates request with given rules

    Parameters:
        req (dict): request
        rules (dict): rules
        return_info (bool): True/False according the necessity of returning error messages (False by default)

    Returns:
        result (bool): the result of the validation (if return_info parameter was False)
        OR
        (result, error_messages): pair of the validation result and error messages object (if return_info was True)
    """
    val = Validator(req, rules)
    result = val.validate()
    if return_info:
        errors = val.get_errors()
        validated_data = val.get_validated_data()
        # if return_info was True return pair as a tuple
        return result, validated_data, errors
    # return validation result
    return result


def validate_many(requests, rules, return_info=False):
    """
    Validates many requests with given rules

    Parameters:
        requests (list): requests
        rules (dict): rules
        return_info (bool): True/False according the necessity of returning error messages (False by default)

    Returns:
        result (bool): the result of the validation (if return_info parameter was False)
        OR
        (result, error_messages): pair of the validation result and error messages object (if return_info was True)
    """

    def get_validation_result(
        _results, _validated_datas, _errors, _return_info=return_info
    ):
        return (
            all(_results)
            if not _return_info
            else (all(_results), _validated_datas, _errors)
        )

    results, validated_datas, errors = [], [], []
    for request in requests:
        if return_info:
            result, _validated_data, _errors = validate(request, rules, return_info)
            errors.append(_errors)
            validated_datas.append(_validated_data)
        else:
            result = validate(request, rules)

        results.append(result)

    return get_validation_result(results, validated_datas, errors)
