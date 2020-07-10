#!/usr/bin/env python3
import os, sys
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader

ROOT_DIR = Path(__file__).parent.parent.parent.absolute()
RULE_TEMPLATE_PATH = os.path.join(ROOT_DIR, "utils/generate_rule/rule_template.py.txt")
TEST_TEMPLATE_PATH = os.path.join(ROOT_DIR, "utils/generate_rule/test_template.py.txt")


def read_file(file_path):
    # returns content of the file
    template = ""
    with open(file_path, "r") as temp:
        template = temp.read()
    return template


def get_class_name(file_name):
    # transforms file name into camelcased class name
    return "".join([x.title() for x in file_name.lower().split("_")])


def create_rule_file(file_name):
    # get class name for the file
    class_name = get_class_name(file_name)

    # get full path for the rule file
    rule_path = os.path.join(ROOT_DIR, "validator/rules_src", file_name.lower() + ".py")

    tm = Template(open(RULE_TEMPLATE_PATH).read())
    file_content = tm.render(name=class_name)

    with open(rule_path, "x") as f:
        f.write(file_content)
    return rule_path


def create_test_file(file_name):
    # get class name for the file
    class_name = get_class_name(file_name)

    # get full path for the test file
    test_path = os.path.join(
        ROOT_DIR, "tests/rules", "test_" + file_name.lower() + ".py"
    )

    tm = Template(open(TEST_TEMPLATE_PATH).read())
    file_content = tm.render(name=class_name, file_name=file_name.lower())

    # write test file
    with open(test_path, "x") as f:
        f.write(file_content)
    return test_path


if __name__ == "__main__":
    # get file name from passed argument
    file_name = sys.argv[1]
    # create rule file sample
    rule_file_path = create_rule_file(file_name)
    # create test file sample
    test_file_path = create_test_file(file_name)

    print("Generation of sample rule and tests completed successfully.\n")
    print(f"Rule -  {rule_file_path}")
    print(f"Test -  {test_file_path}")
