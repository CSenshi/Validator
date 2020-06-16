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
<!-- CD4A678E95173E4BE5E27E2C8169F -->
<div>
<p>
<a href="#Between">Between</a>
<a href="#Mail">Mail</a>
<a href="#Max">Max</a>
<a href="#Min">Min</a>
<a href="#Required">Required</a>
<a href="#RequiredIf">RequiredIf</a>
</p>
</div><a name="Between"/>

#### Between
```python

The field under validation must have a size between the given min and max

>>> Between(2, 15).check(23)
False

>>> Between(2, 15).check(12)
True


```
<a name="Mail"/>

#### Mail
```python

The field under validation must be formatted as an e-mail address

>>> Mail().check('abcd@ef.gh')
True

>>> Mail().check('aaa.com')
False


```
<a name="Max"/>

#### Max
```python

The field under validation must be less than or equal to a maximum value

>>> Max(18).check(23)
False

>>> Max(18).check(15)
True


```
<a name="Min"/>

#### Min
```python

The field under validation must be greater than or equal to a minimum value

>>> Min(18).check(23)
True

>>> Min(18).check(15)
False


```
<a name="Required"/>

#### Required
```python

The field under validation must be present in the input data and not empty

>>> Required().check('Not Empty')
True

>>> Required().check('')
False


```
<a name="RequiredIf"/>

#### RequiredIf
```python

>>> RequiredIf('a').check('abc')
True

>>> RequiredIf('z').check('abc')
False


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
