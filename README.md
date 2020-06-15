# Validator

Validator is a Python library for dealing with request validating.

## Installation (Not Released Yet)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Validator.

```bash
pip install ...
```

## Usage

```python
from validator import Validator


request = {
    "firstName": "Jon",
    "lastName": "Doe",
    "age": 33,
    "mail": "jon_doe@gmail.com",
}

rules = {
    "firstName": "required",
    "lastName": "required",
    "age": "required|min:18",
    "mail": "required|mail",
}

Validator(request, rules).validate()   # returns True

```

## Rules

<div>
<p>
<a href="#Between">Between</a>
<a href="#Mail">Mail</a>
<a href="#Max">Max</a>
<a href="#Min">Min</a>
<a href="#Required">Required</a>
</p>
</div>

<a name="Between"/>

#### Between
The field under validation must have a size between the given min and max 

<a name="Mail"/>

### Mail
The field under validation must be formatted as an e-mail address 

<a name="Max"/>

### Max
The field under validation must be less than or equal to a maximum value 

<a name="Min"/>

### Min
The field under validation must be greater than or equal to a minimum value 

<a name="Required"/>

### Required
The field under validation must be present in the input data and not empty 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
