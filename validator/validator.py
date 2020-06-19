from validator.parser.parser import Parser
from validator import rules as R
from validator import exceptions as exc
from .rule_pipe_validator import RulePipeValidator as RPV

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
        # check for internal error (incorrect rules)
        if not self.check_rules():
            raise exc.RulesFormatError

        self.errors = {}

    def validate(self):
        # prepare variables
        result = True

        # at this point all rules are being correctly passed
        for key in self.rules:
            rules = self.rules[key]
            data = self.request[key]

            # Interface for rules
            rpv = RPV(data, rules)
            rpv_result = rpv.execute()
            errors_on_key = rpv.get_error_messages()

            # if current validation fails change final result
            if not rpv_result:
                result = rpv_result
                self.errors[key] = errors_on_key

        return result

    def get_error_messages(self):
        # return error messages logged on validation
        return self.errors

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


def validate(req, rules, return_errors=False):
    """ 
    Validates request with given rules
  
    Parameters: 
        req (dict): request
        rules (dict): rules
        return_errors (bool): True/False according the necessity of returning error messages (False by default)
  
    Returns: 
        result (bool): the result of the validation (if return_errors parameter was False)
        OR
        (result, error_messages): pair of the validation result and error messages object (if return_errors was True)
    """
    val = Validator(req, rules)
    result = val.validate()
    if return_errors:
        errors = val.get_error_messages()
        # if return_errors was True return pair as a tuple
        return result, errors
    # return validation result
    return result


def validate_many(requests, rules, return_errors=False):
    """
       Validates many requests with given rules

       Parameters:
           requests (list): requests
           rules (dict): rules
           return_errors (bool): True/False according the necessity of returning error messages (False by default)

       Returns:
           result (bool): the result of the validation (if return_errors parameter was False)
           OR
           (result, error_messages): pair of the validation result and error messages object (if return_errors was True)
       """

    def get_validation_result(_results, _errors, _return_errors=return_errors):
        return all(_results) if not _return_errors else (all(_results), _errors)

    results, errors = [], []
    for request in requests:
        if return_errors:
            result, _errors = validate(request, rules, return_errors)
            errors.append(_errors)
        else:
            result = validate(request, rules)

        results.append(result)

    return get_validation_result(results, errors)
