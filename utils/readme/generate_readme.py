#!/usr/bin/env python3
import os, sys, inspect
import pkgutil, importlib
from pathlib import Path
import pprint
from jinja2 import Template, Environment, FileSystemLoader

# "Hacking" to see package of validaor
validator_path = os.path.abspath(Path(__file__).parent.parent.parent)
sys.path += [validator_path]

# file names needed
TEMPLATE_HTML = "utils/readme/RULES_template.html"
RULES_MD = "RULES.md"
RULES_ALL = []
rule_per_row = 5

with open(RULES_MD, "w") as re:
    files = [file for (_, file, _) in pkgutil.iter_modules(["validator/rules_src"])]
    files = sorted(files, key=lambda x: x.lower())

    table_of_contents = []
    for file in files:
        rule = {"name": "", "description": "", "code": ""}

        # Get Absolute Path
        module_abs_path = f"validator.rules_src.{file}"
        pkg = importlib.import_module(module_abs_path)

        # Import all classes from given modules
        names = [x for x in pkg.__dict__ if not x.startswith("_")]
        class_name = names[-1]

        rule["name"] = class_name
        table_of_contents.append(class_name)

        # get all clases from file
        clsmembers = inspect.getmembers(sys.modules[module_abs_path], inspect.isclass)

        # get doc from file
        cur_class = dict(clsmembers)[class_name]
        doc = cur_class.__doc__

        # format doc

        # a. remove trailing newline/spaces
        doc_arr = doc.split("\n")
        doc = ""
        for line in doc_arr:
            line = line.strip()
            doc += f"{line}\n"

        splitter_str = "Examples:"

        # 2. make description,test text
        description, tests = doc.split(splitter_str)
        rule["code"] = tests.strip()

        description = description.strip()
        rule["description"] = description

        # 3. Get aliases
        class_vars = cur_class.__dict__
        aliases = {class_name.lower()}
        if "aliases" in class_vars:
            aliases.update({x for x in class_vars["aliases"]})
        rule["aliases"] = [x for x in aliases]
        RULES_ALL.append(rule)

    # Divide into chunks
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    table_of_contents = list(chunks(table_of_contents, rule_per_row))
    # ToDo: Transpose table_of_contents

    # This method take nested list as argument and tranpose it.
    def transpose_nested_matrix(table_of_contents, table_size):
        # Check true length of the matrix
        true_length = len(table_of_contents[0])
        for each_table in range(table_size):
            # if nested fill it with '_' case.
            temp_list = table_of_contents[each_table]
            if true_length != len(temp_list):
                temp_list += ["_"] * (true_length - len(temp_list))
                table_of_contents[each_table] = temp_list

        # Transpose matrix and return it
        table_of_contents = list(map(list, zip(*table_of_contents)))
        return table_of_contents

    # This method filters nested list and returns True values.
    def remove_nested_values(value):
        if value == "_":
            return False
        return True

    # transpose nested list.
    table_of_contents = transpose_nested_matrix(
        table_of_contents, len(table_of_contents)
    )
    # remove extra values.
    table_of_contents = [
        filter(remove_nested_values, each_list) for each_list in table_of_contents
    ]

    tm = Template(open(TEMPLATE_HTML).read())
    msg = tm.render(rules=RULES_ALL, table_of_contents=table_of_contents)
    re.write(msg)
