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
<a href="#Integer">Integer</a>
<a href="#IP">IP</a>
<a href="#IPv4">IPv4</a>
<a href="#IPv6">IPv6</a>
<a href="#List">List</a>
<a href="#Mail">Mail</a>
<a href="#Max">Max</a>
<a href="#Min">Min</a>
<a href="#Required">Required</a>
<a href="#RequiredIf">RequiredIf</a>
<a href="#Size">Size</a>
</p>
</div><a name="Between"/>

#### Between

The field under validation must have a size between the given min and max


```python

>>> Between(2, 15).check(23)
False

>>> Between(2, 15).check(12)
True


```
<a name="Integer"/>

#### Integer

The field under validation must be an Integer


```python

>>> Integer().check('123')
True

>>> Integer().check('string')
False


```
<a name="IP"/>

#### IP

The field under validation must be an IP address.


```python

>>> IP().check('127.0.0.1')
True

>>> IP().check('0.299.2.1')
False


```
<a name="IPv4"/>

#### IPv4

The field under validation must be an IPv4 address.


```python

>>> IPv4().check('127.0.0.1')
True

>>> IPv4().check('0.299.2.1')
False


```
<a name="IPv6"/>

#### IPv6

The field under validation must be an IPv6 address.


```python

>>> IPv6().check('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
True

>>> IPv6().check('2001:0db8:85a3:9876:1234:8a2e')
False


```
<a name="List"/>

#### List

The field under validation must be a list (Python array)


```python

>>> List().check([1, 2, 3])
True

>>> List().check(123)
False


```
<a name="Mail"/>

#### Mail

The field under validation must be formatted as an e-mail address


```python

>>> Mail().check('abcd@ef.gh')
True

>>> Mail().check('aaa.com')
False


```
<a name="Max"/>

#### Max

The field under validation must be less than or equal to a maximum value


```python

>>> Max(18).check(23)
False

>>> Max(18).check(15)
True


```
<a name="Min"/>

#### Min

The field under validation must be greater than or equal to a minimum value


```python

>>> Min(18).check(23)
True

>>> Min(18).check(15)
False


```
<a name="Required"/>

#### Required

The field under validation must be present in the input data and not empty


```python

>>> Required().check('Not Empty')
True

>>> Required().check('')
False


```
<a name="RequiredIf"/>

#### RequiredIf

Some Description...


```python

>>> RequiredIf('a').check('abc')
True

>>> RequiredIf('z').check('abc')
False


```
<a name="Size"/>

#### Size

The field under validation must have a size matching the given value.
For string data, value corresponds to the number of characters.
For numeric data, value corresponds to a given integer value (the attribute must also have the numeric or integer rule).
For an array, size corresponds to the count of the array.


```python

>>> Size(6).check('string')
True

>>> Size(12).check('string')
False


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
