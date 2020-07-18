<table>
    <tr>
        <td>
            <a href="#Between">Between</a>
        </td><td>
            <a href="#Binary">Binary</a>
        </td><td>
            <a href="#Date">Date</a>
        </td><td>
            <a href="#Hex">Hex</a>
        </td><td>
            <a href="#Integer">Integer</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#IP">IP</a>
        </td><td>
            <a href="#IPv4">IPv4</a>
        </td><td>
            <a href="#IPv6">IPv6</a>
        </td><td>
            <a href="#JSON">JSON</a>
        </td><td>
            <a href="#List">List</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Mail">Mail</a>
        </td><td>
            <a href="#Max">Max</a>
        </td><td>
            <a href="#Min">Min</a>
        </td><td>
            <a href="#Regex">Regex</a>
        </td><td>
            <a href="#Required">Required</a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="#Same">Same</a>
        </td><td>
            <a href="#Size">Size</a>
        </td><td>
            <a href="#String">String</a>
        </td>
    </tr>
    
</table>




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

<a name="Max" />

#### Max

The field under validation must be less than or equal to a maximum value. Given value is evaluated according to `Size` rule
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

<a name="Min" />

#### Min

The field under validation must be greater than or equal to a minimum value. Given value is evaluated according to `Size` rule
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

<a name="Size" />

#### Size

The field under validation must have a size matching the given value. For string data, value corresponds to the number of characters. For numeric data, value corresponds to a given integer value (the attribute must also have the numeric or integer rule). For an array, size corresponds to the count of the array.
```python
>>> from validator import validate

# Checks for string length
>>> reqs = {"value" : "something"}
>>> rule = {"value" : "size:9"}
>>> validate(reqs, rule)
True

# Checks for Integer value
>>> reqs = {"value" : "18"} # "18" and 18 would be same
>>> rule = {"value" : "integer|size:18"}
>>> validate(reqs, rule)
True

# Checks for List length
>>> reqs = {"value" : ["a", "b", "c"]}
>>> rule = {"value" : "list|size:3"}
>>> validate(reqs, rule)
True
```

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

