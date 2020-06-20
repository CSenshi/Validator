#!/usr/bin/env python3
import pkgutil
import importlib
from pathlib import Path
import sys
import os
import sys, inspect
import pprint

# "Hacking" to see package of validaor
validator_path = os.path.abspath(Path(__file__).parent.parent.parent)
sys.path += [validator_path]

# file names needed
RULESMD = "RULES.md"
HTML_DIV_EXAMPLE = "utils/readme/readme_rules_div_example.html"
HTML_REF_EXAMPLE = "utils/readme/readme_rule_ref_example.html"
RULE_DESC_EXAMPLE = "utils/readme/readme_rules_desc_example.html"


with open(RULESMD, "w") as re:
    div_str = open(HTML_DIV_EXAMPLE).read()
    ref_str = open(HTML_REF_EXAMPLE).read()
    rule_desc = open(RULE_DESC_EXAMPLE).read()

    all_rules_refs = ""
    all_rules_desc = ""
    files = [file for (_, file, _) in pkgutil.iter_modules(["validator/rules_src"])]
    files = sorted(files, key=lambda x: x.lower())
    for file in files:
        # Get Absolute Path
        module_abs_path = f"validator.rules_src.{file}"
        pkg = importlib.import_module(module_abs_path)

        # Import all classes from given modules
        names = [x for x in pkg.__dict__ if not x.startswith("_")]
        class_name = names[-1]

        # 1. make string result
        all_rules_refs += ref_str.format(rule=class_name)

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

        description = description.strip().replace("\n", ". ").replace("..", ".")
        all_rules_desc += rule_desc.format(
            rule=class_name, rule_description=description, rule_tests=tests
        )

    all_rules_refs = div_str.format(rules_ref=all_rules_refs)
    re.write(all_rules_refs)
    re.write(all_rules_desc)
