# Contributing

## Setting up environment
First of all we need to set up our project with easy to go commands. Just run following commands and you will be ready to go:
* ``` make install ``` Will install all of packages used by project
* ``` make ``` Will generate rules.py file which is used to import rules

At this point you are done with setting up your project and should be able to start coding.

## Creating new Rule
If you wish to contribute with new rule, please use our written generator to generate new rule template class and tests
* ``` make generate-rule F_NAME=new_rule ``` Will generate new rule in rules_src/ folder. Takes in one argument F_NAME which is rule's file name and automatically generates rule's class name which will be NewRule (converted to CapWords convention)

## Testing
For testing we use pytest framework. All of the tests are located in the tests/ directory. As you can see we write speerate kind of tests in seperate functions, so please use it to make testing even better. We also support doctests and we do preffer 2 doctests for each rule(one for True evaluation and second for False), it will make easier for users to know what given rule is capable of doing. Finally, the code conduct, we test PEP standards and code formating using tools defined in Code Style.

We provide some testing with Makefile:

* ``` make test ``` Will check for all tests (default tests, doctests, formatting checks and pep8 standards)
* ``` make pytest ``` Will check only for pytests written in tests directory
* ``` make doctest ``` Will check only for doctests written for each rule in rules_src
* ``` make check ``` Will check for correct formatting of code and pep8 standards

Our Makefile also supports testing specifying rule. For Example, if you want to check tests only for Rule called Min just use it as follows: ```make test TEST=min```

## Code Style
[PEP 8](https://www.python.org/dev/peps/pep-0008/) is used as coding convention for project and 
we use tool [autopep8](https://github.com/hhatto/autopep8) for checking pep standarts. Code formatting is checked using [Black](https://github.com/psf/black). You can install those tools manually and use them as you will, but we do recommend using our make commad.

* ``` make fix ``` 

It will reformat all of .py files using black standards and will try to fix most of pep8 problems(Be aware that you will most likely need to modify some code by hand, but don't worry, ```make check``` will output exactly what lines errored).
