# Validator

Validator is a Python library for dealing with request validating.

### Table of Contents
* **[Installation](#Installation)**
* **[Overview](#Overview)**
   * **[Usage](#Usage)**
   * **[Error Messages](#Error-Messages)**
   * **[Validating Arrays](#Validating-Arrays)**
   * **[Rules](#Rules)**
   * **[Rules Interconnection](#Rules-Interconnection)**
   * **[Custom Rules](#Custom-Rules)**
* **[Contributing](#Contributing)**
* **[License](#License)**

<a name="Installation"></a>
## Installation

Use the package manager [pip](https://pypi.org/project/validator/) to install Validator.

```bash
pip install validator
```

<a name="Overview"></a>

<a name="Usage"></a>
## Usage

User should pass request dictionary and rules dictionary for validating data in the request.

Please see examples below:

```python
from validator import validate

reqs = {"name": "Jon Doe",
        "age": 33,
        "mail": "jon_doe@gmail.com"}

rule = {"name": "required",
        "age": "integer|min:18",
        "mail": "required|mail"}

result = validate(request, rules) # True
```
`valiadte()` returns either True or False.

Another option is to use `Validator` class
```python
from validator import Validator

reqs = {...}
rule = {...}

val = Validator(request, rules)
result = val.validate() # True
```

<a name="Error-Messages"></a>
### Error Messages
Validator allows user to have a look at failed validations

```python
from validator import validate

reqs = {"name": "",
        "mail": "jon_doe"}

rule = {"name": "required",
        "mail": "mail"}

result, errors = validate(reqs, rule, return_errors=True)

"""
result = True
errors = {'name': {'Required': 'Field was empty'},
          mail': {'Mail': 'Expected a Mail, Got: jon_doe'}}
"""
```

Or you can use `Validator` class for error messages as well (result and errors are same).

```python
val = Validator(request, rules)
result = val.validate()
errors = val.get_error_messages()
```


<a name="Validating-Arrays"></a>
### Validating Arrays
Validator comes with `validate_many()` function, which validates multiple requests. Function takes list of requests and one rule. This rule is checked for all the requests. If one or more requests fail validation function returns False, otherwise (if all pass) True. For more details see example below:

Validation Passes:
```python
from validator import validate_many

requests = [{"name": "Jon"},
            {"name": "Rob"},
            {"name": "Tom"},
            {"name": "Greg"}]
rule = {"name": 'required|min:3'}

result = validate_many(requests, rule) # True
```
We can also ahve a look at failde validations and error messages. `validate_many()` takes third argument as boolean, indicating return of error messages.

Validation Fails:
```python
from validator import validate_many

requests = [{"name": "Jon"},
            {"name": ""},
            {"name": "Yo"},
            {"name": "Greg"}]
rule = {"name": 'required|min:3'}

result, errors = validate_many(requests, rule, return_errors=True)
"""
result = False
errors = [{},
          {'name': {'Min': 'Expected Maximum: 3, Got: 0', 'Required': 'Field was empty'}},
          {'name': {'Min': 'Expected Maximum: 3, Got: 2'}},
          {}]
"""
```

<a name="Rules"></a>
## Rules

Validator Rules can be used in different ways. Please see some examples below:

#### Strings

```python
rule = {"name": "required",
        "age": "integer|min:18",
        "mail": "required|mail"}
```
#### Array of Strings
```python
rule = {"name": ["required"],
        "age": ["integer", "min:18"],
        "mail": ["required", "mail"]}
```

#### Array of Rules
```python
from validator import rules as R

rules = {"name": [R.Required()],
        "age": [R.Integer(), R.Min(18)],
        "mail": [R.Requried(), R.Mail()]}
```


#### Other Miscellaneous
```python
from validator import rules as R

rules = {"name": R.Required(),           # no need for Array Brackets if one rule
        "age": [R.Integer, R.Min(18)],
        "mail": [R.Requried, R.Mail]}   # no need for class initialization with brakcets () 
                                        # if no arguments are passed to rule
```

#### *All of rules are listed in [RULES.md](https://github.com/CSenshi/Validator/blob/master/RULES.md) file*


<a name="Rules-Interconnection"></a>
## Rules Interconnection
Rules can affect each other. Let's take a look at `Size` rule. It takes 1 argument and checks if data is equal to given value (example: `'size:10'`).


* Case 1: checks for length of '18' to be 18. len('18') is 2, therefore it is False.
```python
reqs = {'age' : '18'}
rule = {'age' : 'size:18'}

validate(reqs, rule)
"""
result = False
errors = {'age': {'Size': 'Expected Size:18, Got:2'}}
"""
```

* Case 2: checks if int representation of '18' is equal to 18. (int('18') = 18), therefore it is True.
```python
reqs = {'age' : '18'}
rule = {'age' : 'integer|size:18'}

validate(reqs, rule) # True
```

<a name="Custom-Rules"></a>
## Custom Rules
We give users ability to advance and use their own checkers. Write function and use is as a rule. See examples below:
1. Use defined functions: 
    ```python3
    from validator import validate

    def func_age(x):
        return x >= 18

    req = {"age": 30}
    rules = {"age": func_age}

    validate(req, rules)
    ```
2. Use Lambda functions: 
    ```python3
    from validator import validate

    req = {"age": 30}
    rules = {"age": lambda x: x >= 18}

    validate(req, rules)
    ```
3. Any callable class *(NOTE: Pass class instance and not class itself)*:
    ```python3
    from validator import validate

    class checker:
      def __init__(self):
          pass

      def __call__(self, x):
          return x >= 456

    req = {"age": 30}
    rules = {"age": checker()}

    validate(req, rules)
    ```
4. Custom Rule:
    ```python3
    from validator import validate
    from validator.rules import Rule

    class AgeRule(Rule):
        def __init__(self, min):
            Rule.__init__(self)
            self.min = min

        def check(self, arg):
            return self.min <= arg

    req = {"age": 30}
    rules = {"age": AgeRule(18)}

    validate(req, rules)
    ```

<a name="Contributing"></a>
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please see [CONTRIBUTING.md](https://github.com/CSenshi/Validator/blob/master/CONTRIBUTING.md) before making PR :)


<a name="License"></a>
## License
[MIT](https://choosealicense.com/licenses/mit/)
