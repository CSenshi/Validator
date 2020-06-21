# Contributing

### Table of Contents
* **[Setting up environment](#Setting-up-environment)**
* **[Creating new Rule](#Creating-new-Rule)**
   * **[`__init__`](#init)**
   * **[`__from_str__`](#from_str)**
   * **[`check`](#check)**
   * **[Error Messages](#Error-Messages)**
   * **[Using other rules](#Using-other-rules)**
   * **[Accessing Neighbour Rules](#Accessing-Neighbour-Rules)**
* **[Testing](#Testing)**
* **[Code Style](#Code-Style)**

<a name="Setting-up-environment"></a>
## Setting up environment
First of all we need to set up our project with easy to go commands. Just run following commands and you will be ready to go:
* ``` make install ``` Will install all of packages used by project
* ``` make ``` Will generate rules.py file which is used to import rules

At this point you are done with setting up your project and should be able to start coding.

<a name="Creating-new-Rule"></a>
## Creating new Rule
If you wish to contribute with new rule, please use our written generator to generate new rule template class and tests
* ``` make rule F_NAME=new_rule ``` Will generate new rule in rules_src/ folder. Takes in one argument F_NAME which is rule's file name and automatically generates rule's class name which will be NewRule (converted to CapWords convention)

```bash
$ make rule F_NAME=new_rule 
```
Running make rule command will result in creating following file:
```python3
from validator.rules_src import Rule


class NewRule(Rule):
    """
    <Insert Rule Documentation Here>

    Examples:
    >>> NewRule().check(...)
    True

    >>> NewRule().check(...)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        pass

    def __from_str__(self):
        pass
```

<a name="init"></a>
* **`__init__`:**

    This is Constructor for your rule. If your rule depends on arguments please initialize them here.
    
    Example:
    `rule = {'name' : 'between:18,25'}` in this Between rule '18' and '25' are arguments that are passed in the init function.
    ```python
    def __init__(self, min_value, max_value):
        Rule.__init__(self)
        self.min_value = min_value
        self.max_value = max_value
    ```
    
<a name="from_str"></a>
* **`__from_str__`:**

    This is function that converts arguments into needed types. When rules are called as string all of the arguments are parsed and then passed to constructor as string, so if you need convert them, please use this function.
    
    Example:
    As we have seen in the upper example `rule = {'name' : 'between:18,25'}`'18' and '25' are arguments that are passed in the init function, but they are passed as string values. შo we will have to convert them to integers. Conversion should happen in the given method
    ```python
    def __from_str__(self):
        self.min_value = int(self.min_value)
        self.max_value = int(self.max_value)
    ```

<a name="check"></a>
* **`check`:**

    This is the method that validates data. It takes only one argument, it represents data that should be validated
    
    Example:
    ```python
    def check(self, arg):
        if self.min_value <= arg <= self.max_value:
            return True
        return False
    ```

<a name="Error-Messages"></a>
* **Error Messages:**

    Each rule is child of main `Rule` Class, which has method `set_errror_message(str)`. Please use this method to set error message when validation fails.
                

    Example:
    we will just modify already written check method to following
    ```python
    def check(self, arg):
        if self.min_value <= arg <= self.max_value:
            return True
        self.set_errror_message(f"Expected Between: {self.min_value} and {self.min_value}, Got: {size}")
        return False
    ```

<a name="Using-other-rules"></a>
* **Using other rules:**

    As you can already see generated rule is subclass of main `Rule` class. And then in the `__init__` method we initialize `Rule` class 
    ```python
    ...
    class NewRule(Rule):
        def __init__(self):
            Rule.__init__(self)
    ...
    ```
    You can use any other rule(s) instead of main `Rule` class and use their functionality. Let's use `Min` and `Max` rules 
    
    Example:
    1. Import rules
    ```python
    from validator.rules_src.max import Max
    from validator.rules_src.min import Min
    ```
    2. Change class extends
    ```python
    class Between(Max, Min):
    ```
    3. Change `__init__`
    ```python
    def __init__(self, min_value, max_value):
        Min.__init__(self, min_value)
        Max.__init__(self, max_value)
    ```
    4. Change `__from_str__`:
    ```python
    def __from_str__(self):
        Min.__from_str__(self)
        Max.__from_str__(self)
    ```
    5. Change `check`(when using parrent rule's check method it is not necessary to use `set_error_message()` as parrent rule will set it automaticaly):
    ```python
    def check(self, arg):
        if Min.check(self, arg) and Max.check(self, arg):
            return True
        return False
    ```

<a name="Accessing-Neighbour-Rules"></a>
* **Accessing Neighbour Rules:**

    Each Rule class instance has an instance variable `self.rpv`. It is instance of class `RPV (RulePipeValidator` and is used to communicate with neighbour rules.
    
    Example:
    ```python 
    rule = {'age' : 'integer|max:18',
            'name': 'required|min:2'}
    ```
    `Max` and `Integer` rules will have same variable 'self.rpv' containing two values in list `[Integer(), Max(18)]`. For 'name' rules `Required` and `Min` will also have same instance variable `self.rpv`, Which will contain two values in list `[Required(), Min(2)]`

<a name="Testing"></a>
## Testing
For testing we use pytest framework. All of the tests are located in the tests/ directory. As you can see we write speerate kind of tests in seperate functions, so please use it to make testing even better. We also support doctests and we do preffer 2 doctests for each rule(one for True evaluation and second for False), it will make easier for users to know what given rule is capable of doing. Finally, the code conduct, we test PEP standards and code formating using tools defined in Code Style.

We provide some testing with Makefile:

* ``` make test ``` Will check for all tests (default tests, doctests, formatting checks and pep8 standards)
* ``` make pytest ``` Will check only for pytests written in tests directory
* ``` make doctest ``` Will check only for doctests written for each rule in rules_src
* ``` make check ``` Will check for correct formatting of code and pep8 standards

Our Makefile also supports testing specifying rule. For Example, if you want to check tests only for Rule called Min just use it as follows: ```make test TEST=min```

<a name="Code-Style"></a>
## Code Style
Code formatting is checked using [Black](https://github.com/psf/black). You can install those tools manually and use them as you will, but we do recommend using our make commad.

* ``` make fix ``` 

It will reformat all of .py files using black standards and will try to fix most of pep8 problems(Be aware that you will most likely need to modify some code by hand, but don't worry, ```make check``` will output exactly what lines errored).
