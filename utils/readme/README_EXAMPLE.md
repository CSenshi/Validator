# Validator

Validator is a Python library for dealing with request validating.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Validator.

```bash
pip install validator
```

## Usage

```python
from validator import Validator

reqs = {"name": "Jon Doe",
        "age": 33,
        "mail": "jon_doe@gmail.com"}

rule = {"name": "required",
         "age": "integer|min:18",
         "mail": "required|mail"}

validate(request, rules)   # returns True
```
Validator can take multiple kind of rules:

#### * [Strings](#usage-1)
#### * [Array of Strings](#usage-2)
#### * [Array of Rules](#usage-3)
#### * [Other Miscellaneous](#usage-4)

<a name='usage-1'/>

#### Strings

```python
rule = {"name": "required",
        "age": "integer|min:18",
        "mail": "required|mail"}
```
<a name='usage-2'/>

#### Array of Strings
```python
rule = {"name": ["required"],
        "age": ["integer", "min:18"],
        "mail": ["required", "mail"]}
```

<a name='usage-3'/>

#### Array of Rules
```python
from validator import rules as R

rules = {"name": [R.Required()],
        "age": [R.Integer(), R.Min(18)],
        "mail": [R.Requried(), R.Mail()]}
```

<a name='usage-4'/>

#### Other Miscellaneous
```python
from validator import rules as R

rules = {"name": R.Required(),           # no need for Array Brackets if one rule
        "age": [R.Integer, R.Min(18)],
        "mail": [R.Requried, R.Mail]}   # no need for class initialization with brakcets () 
                                        # if no arguments are passed to rule
```

## Rules
<!-- CD4A678E95173E4BE5E27E2C8169F -->

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) before making PR :)

## License
[MIT](https://choosealicense.com/licenses/mit/)
