<table>
    <tr>
        <td>
            <a href="#Accepted">Accepted</a>
        </td><td>
            <a href="#Binary">Binary</a>
        </td><td>
            <a href="#Integer">Integer</a>
        </td><td>
            <a href="#List">List</a>
        </td><td>
            <a href="#Regex">Regex</a>
        </td><td>
            <a href="#String">String</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Alpha">Alpha</a>
        </td><td>
            <a href="#Date">Date</a>
        </td><td>
            <a href="#IP">IP</a>
        </td><td>
            <a href="#Mail">Mail</a>
        </td><td>
            <a href="#Required">Required</a>
        </td><td>
            <a href="#UUIDv1">UUIDv1</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Base32">Base32</a>
        </td><td>
            <a href="#Decimal">Decimal</a>
        </td><td>
            <a href="#IPv4">IPv4</a>
        </td><td>
            <a href="#Max">Max</a>
        </td><td>
            <a href="#RequiredIf">RequiredIf</a>
        </td><td>
            <a href="#UUIDv3">UUIDv3</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Base64">Base64</a>
        </td><td>
            <a href="#Dict">Dict</a>
        </td><td>
            <a href="#IPv6">IPv6</a>
        </td><td>
            <a href="#Min">Min</a>
        </td><td>
            <a href="#Same">Same</a>
        </td><td>
            <a href="#UUIDv4">UUIDv4</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Between">Between</a>
        </td><td>
            <a href="#Hex">Hex</a>
        </td><td>
            <a href="#JSON">JSON</a>
        </td><td>
            <a href="#Octal">Octal</a>
        </td><td>
            <a href="#Size">Size</a>
        </td>
    </tr>
    
</table>



<a name="Accepted" />

#### Accepted

The field under validation must be 'yes', 'on', '1', or 'true' as String or True as boolena. This is useful for validating "Terms of Service" acceptance.
```python
>>> from validator import validate

>>> reqs = {'value' : '1'}
>>> rule = {'value' : 'accepted'}
>>> validate(reqs, rule)
True

>>> reqs = {'value' : '0'}
>>> rule = {'value' : 'accepted'}
>>> validate(reqs, rule)
False
```
Aliases:
['accepted']

<a name="Alpha" />

#### Alpha

The field under validation must be entirely alphabetic characters
```python
>>> from validator import validate

>>> reqs = {'value' : 'KillerBunny'}
>>> rule = {'value' : 'alpha'}
>>> validate(reqs, rule)
True

>>> reqs = {'value' : '326forever'}
>>> rule = {'value' : 'alpha'}
>>> validate(reqs, rule)
False
```
Aliases:
['alpha']

<a name="Base32" />

#### Base32

The field under validation must be a valid Base32 encoded
```python
>>> from validator import validate

>>> reqs = {"data" : "KZAUYSKEIFKE6URAIZKFOII="}
>>> rule = {"data" : "base32"}
>>> validate(reqs, rule)
True

>>> reqs = {"data" : "Not Encoded"}
>>> rule = {"data" : "base32"}
>>> validate(reqs, rule)
False
```
Aliases:
['base32']

<a name="Base64" />

#### Base64

The field under validation must be a valid Base64 encoded
```python
>>> from validator import validate

>>> reqs = {"data" : "VmFsaWRhdG9yIEZUVyE="}
>>> rule = {"data" : "base64"}
>>> validate(reqs, rule)
True

>>> reqs = {"data" : "Not Encoded"}
>>> rule = {"data" : "base64"}
>>> validate(reqs, rule)
False
```
Aliases:
['base64']

<a name="Between" />

#### Between

The field under validation must have a size between the given min and max
```python
>>> from validator import validate

>>> reqs = {"age" : 10}
>>> rule = {"age" : "between:6,18"}
>>> validate(reqs, rule)
True

>>> reqs = {"age" : 23}
>>> rule = {"age" : "between:6,18"}
>>> validate(reqs, rule)
False
```
Aliases:
['between']

<a name="Binary" />

#### Binary

The field under validation must be a binary number
```python
>>> from validator import validate

>>> reqs = {"date" : "010101010010"}
>>> rule = {"date" : "binary"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "0b010101010010"}
>>> rule = {"date" : "binary"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "0123012"}
>>> rule = {"date" : "binary"}
>>> validate(reqs, rule)
False
```
Aliases:
['binary', 'bin']

<a name="Date" />

#### Date

The field under validation must be an Integer
```python
>>> from validator import validate

>>> reqs = {"date" : "25-08-1900"}
>>> rule = {"date" : "date"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "32-12-2020"}
>>> rule = {"date" : "date"}
>>> validate(reqs, rule)
False
```
Aliases:
['date']

<a name="Decimal" />

#### Decimal

The field under validation must be a decimal number
```python
>>> from validator import validate

>>> reqs = {'value' : '23'}
>>> rule = {'value' : 'decimal'}
>>> validate(reqs, rule)
True

>>> reqs = {'value' : '2F'}
>>> rule = {'value' : 'decimal'}
>>> validate(reqs, rule)
False
```
Aliases:
['dec', 'decimal']

<a name="Dict" />

#### Dict

The field under validation must be a dictionary (Python map)
```python
>>> from validator import validate

>>> reqs = {"data" : {"key1" : "val1", "key2" : "val2"} }
>>> rule = {"data" : "dict"}
>>> validate(reqs, rule)
True

>>> reqs = {"data" : ["val1", "val2", "val3", "val4"]}
>>> rule = {"data" : "dict"}
>>> validate(reqs, rule)
False
```
Aliases:
['dict']

<a name="Hex" />

#### Hex

The field under validation must be a hexadecimal number
```python
>>> from validator import validate

>>> reqs = {"date" : "A1B2c3"}
>>> rule = {"date" : "hex"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "0xA1b2C3"}
>>> rule = {"date" : "hex"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "abcdefgh"}
>>> rule = {"date" : "hex"}
>>> validate(reqs, rule)
False
```
Aliases:
['hexadecimal', 'hex']

<a name="Integer" />

#### Integer

The field under validation must be an Integer
```python
>>> from validator import validate

>>> reqs = {"num" : "23"}
>>> rule = {"num" : "integer"}
>>> validate(reqs, rule)
True

>>> reqs = {"num" : "value"}
>>> rule = {"num" : "integer"}
>>> validate(reqs, rule)
False
```
Aliases:
['integer']

<a name="IP" />

#### IP

The field under validation must be an IP address.
```python
>>> from validator import validate

>>> reqs = {"ip_addr" : "192.168.0.1" }
>>> rule = {"ip_addr" : "ip"}
>>> validate(reqs, rule)
True

>>> reqs = {"ip_addr" : "0.123:2:1" }
>>> rule = {"ip_addr" : "ip"}
>>> validate(reqs, rule)
False
```
Aliases:
['ip']

<a name="IPv4" />

#### IPv4

The field under validation must be an IPv4 address.
```python
>>> from validator import validate

>>> reqs = {"ipv4_addr" : "127.0.0.1"}
>>> rule = {"ipv4_addr" : "ipv4"}
>>> validate(reqs, rule)
True

>>> reqs = {"ipv4_addr" : "0.299.2.1"}
>>> rule = {"ipv4_addr" : "ipv4"}
>>> validate(reqs, rule)
False
```
Aliases:
['ipv4']

<a name="IPv6" />

#### IPv6

The field under validation must be an IPv6 address.
```python
>>> from validator import validate

>>> reqs = {"ipv6_addr" : "2001:0db8:85a3:0000:0000:8a2e:0370:7334"}
>>> rule = {"ipv6_addr" : "ipv6"}
>>> validate(reqs, rule)
True

>>> reqs = {"ipv6_addr" : "2001:0db8:85a3:9876:1234:8a2e"}
>>> rule = {"ipv6_addr" : "ipv6"}
>>> validate(reqs, rule)
False
```
Aliases:
['ipv6']

<a name="JSON" />

#### JSON

The field under validation must be formatted as an JSON
```python
>>> from validator import validate

>>> reqs = {"value" : '{ "age":100}'}
>>> rule = {"value" : "json"}
>>> validate(reqs, rule)
True

>>> reqs = {"value" : "aaa.com"}
>>> rule = {"value" : "json"}
>>> validate(reqs, rule)
False
```
Aliases:
['json']

<a name="List" />

#### List

The field under validation must be a list (Python array)
```python
>>> from validator import validate

>>> reqs = {"arr" : [1, 2, 3]}
>>> rule = {"arr" : "list"}
>>> validate(reqs, rule)
True

>>> reqs = {"arr" : 123}
>>> rule = {"arr" : "list"}
>>> validate(reqs, rule)
False
```
Aliases:
['list']

<a name="Mail" />

#### Mail

The field under validation must be formatted as an e-mail address
```python
>>> from validator import validate

>>> reqs = {"email_addr" : "abcd@ef.gh"}
>>> rule = {"email_addr" : "mail"}
>>> validate(reqs, rule)
True

>>> reqs = {"email_addr" : "aaa.com"}
>>> rule = {"email_addr" : "mail"}
>>> validate(reqs, rule)
False
```
Aliases:
['mail']

<a name="Max" />

#### Max

The field under validation must be less than or equal to a maximum value
Given value is evaluated according to `Size` rule
```python
>>> from validator import validate

>>> reqs = {"age" : 15}
>>> rule = {"age" : "max:18"}
>>> validate(reqs, rule)
True

>>> reqs = {"age" : 23}
>>> rule = {"age" : "max:18"}
>>> validate(reqs, rule)
False
```
Aliases:
['max']

<a name="Min" />

#### Min

The field under validation must be greater than or equal to a minimum value.
Given value is evaluated according to `Size` rule
```python
>>> from validator import validate

>>> reqs = {"age" : 23}
>>> rule = {"age" : "min:18"}
>>> validate(reqs, rule)
True

>>> reqs = {"age" : 13}
>>> rule = {"age" : "min:18"}
>>> validate(reqs, rule)
False
```
Aliases:
['min']

<a name="Octal" />

#### Octal

The field under validation must be an octal number
```python
>>> from validator import validate

>>> reqs = {"date" : "73021"}
>>> rule = {"date" : "octal"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "0o73021"}
>>> rule = {"date" : "octal"}
>>> validate(reqs, rule)
True

>>> reqs = {"date" : "23489"}
>>> rule = {"date" : "octal"}
>>> validate(reqs, rule)
False
```
Aliases:
['oct', 'octal']

<a name="Regex" />

#### Regex

The field under validation must match the given regular expression.
```python
>>> from validator import validate

>>> reqs = {"value" : "PythonValidator"}
>>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
>>> validate(reqs, rule)
True

>>> reqs = {"value" : "Python_Validator"}
>>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
>>> validate(reqs, rule)
False
```
Aliases:
['regex']

<a name="Required" />

#### Required

The field under validation must be present in the input data and not empty
```python
>>> from validator import validate

>>> reqs = {"value" : "Not Empty"}
>>> rule = {"value" : "required"}
>>> validate(reqs, rule)
True

>>> reqs = {"value" : ""}
>>> rule = {"value" : "required"}
>>> validate(reqs, rule)
False
```
Aliases:
['required']

<a name="RequiredIf" />

#### RequiredIf

The field under validation must be present and not empty if the anotherfield field is equal to any value.
```python
>>> from validator import validate

>>> reqs = {'under_age' : 'no'}
>>> rule = {'parent' : 'required_if:under_age,yes'}
>>> validate(reqs, rule)
True

>>> reqs = {'under_age' : 'yes',
...         'parent': 'John Doe'}
>>> rule = {'parent' : 'required_if:under_age,yes'}
>>> validate(reqs, rule)
True

>>> reqs = {'under_age' : 'yes'}
>>> rule = {'parent' : 'required_if:under_age,yes'}
>>> validate(reqs, rule)
False
```
Aliases:
['requiredif']

<a name="Same" />

#### Same

The given field must match the field under validation
```python
>>> from validator import validate

>>> reqs = {"old_pass": "password",
...         "new_pass": "password"}
>>> rule = {"new_pass": "same:old_pass"}
>>> validate(reqs, rule)
True

>>> reqs = {"old_pass": "password",
...         "new_pass": "changed_password"}
>>> rule = {"new_pass": "same:old_pass"}
>>> validate(reqs, rule)
False
```
Aliases:
['same']

<a name="Size" />

#### Size

The field under validation must have a size matching the given value.


* For string data, value corresponds to the number of characters.

* For numeric data, value corresponds to a given integer value. The attribute must also have any of the number rules: decimal, binary, octal, hex.
If Integer rule is given it checks for all four systems with given order

* For collectons, size corresponds to the len() of the given argument. It works for: String, List, Dict, JSON
```python
>>> from validator import validate

# Checks for given number system
>>> reqs = {"value" : "42"}
>>> rule = {"value" : "decimal|size:42"}
>>> validate(reqs, rule) # Checks for Decimal Integer value
True

>>> reqs = {"value" : "0b101010"}
>>> rule = {"value" : "binary|size:42"}
>>> validate(reqs, rule) # Checks for Binary Integer value
True

>>> reqs = {"value" : "0o52"}
>>> rule = {"value" : "octal|size:42"}
>>> validate(reqs, rule) # Checks for Octal Integer value
True

>>> reqs = {"value" : "0x2a"}
>>> rule = {"value" : "hex|size:42"}
>>> validate(reqs, rule) # Checks for Hex Integer value
True

# Checks len() for given collections
>>> reqs = {"value" : "something"}
>>> rule = {"value" : "string|size:9"}
>>> validate(reqs, rule) # Checks for string length
True

>>> reqs = {"value" : ["a", "b", "c"]}
>>> rule = {"value" : "list|size:3"}
>>> validate(reqs, rule) # Checks for List length
True

>>> reqs = {"value" : {"k1":"v1", "k2":"v2", "k3":"v3", "k4":"v4"}}
>>> rule = {"value" : "dict|size:4"}
>>> validate(reqs, rule) # Checks for Dictionary length
True

>>> reqs = {"value" : '{"name":"John", "age":31, "city":"New York"}'}
>>> rule = {"value" : "json|size:3"}
>>> validate(reqs, rule) # Checks for JSON length
True
```
Aliases:
['size']

<a name="String" />

#### String

The field under validation must be a String
```python
>>> from validator import validate

>>> reqs = {"value" : "some string"}
>>> rule = {"value" : "string"}
>>> validate(reqs, rule)
True

>>> reqs = {"value" : 17}
>>> rule = {"value" : "string"}
>>> validate(reqs, rule)
False
```
Aliases:
['string']

<a name="UUIDv1" />

#### UUIDv1

The field under validation must be formatted as an uuidv1
```python
>>> from validator import validate

>>> reqs = {'data' : 'eb241bb4-c087-11ea-b3de-0242ac130004'}
>>> rule = {'data' : 'uuidv1'}
>>> validate(reqs, rule)
True

>>> reqs = {'data' : 'bba617b4-364b-4a0d-9e96-cb8a24ef1bec'}
>>> rule = {'data' : 'uuidv1'}
>>> validate(reqs, rule) # It fails because data is uuidv4
False
```
Aliases:
['uuidv1']

<a name="UUIDv3" />

#### UUIDv3

The field under validation must be formatted as an uuidv3
```python
>>> from validator import validate

>>> reqs = {'data' : 'a3bb189e-8bf9-3888-9912-ace4e6543002'}
>>> rule = {'data' : 'uuidv3'}
>>> validate(reqs, rule)
True

>>> reqs = {'data' : 'bba617b4-364b-4a0d-9e96-cb8a24ef1bec'}
>>> rule = {'data' : 'uuidv3'}
>>> validate(reqs, rule) # It fails because data is uuidv4
False
```
Aliases:
['uuidv3']

<a name="UUIDv4" />

#### UUIDv4

The field under validation must be formatted as an uuidv4
```python
>>> from validator import validate

>>> reqs = {'data' : '81368b76-31e9-41db-b28c-8c029cb435f0'}
>>> rule = {'data' : 'uuidv4'}
>>> validate(reqs, rule)
True

>>> reqs = {'data' : 'a3bb189e-8bf9-3888-9912-ace4e6543002'}
>>> rule = {'data' : 'uuidv4'}
>>> validate(reqs, rule) # It fails because data is uuidv3
False
```
Aliases:
['uuidv4']
