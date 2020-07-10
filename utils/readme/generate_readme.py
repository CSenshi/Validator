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

    for file in files:
        rule = {"name": "", "description": "", "code": ""}

        # Get Absolute Path
        module_abs_path = f"validator.rules_src.{file}"
        pkg = importlib.import_module(module_abs_path)

        # Import all classes from given modules
        names = [x for x in pkg.__dict__ if not x.startswith("_")]
        class_name = names[-1]

        rule["name"] = class_name

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

        description = description.strip().replace("\n", ". ").replace("..", ".")
        rule["description"] = description

        RULES_ALL.append(rule)

    # Divide into chunks
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    tm = Template(open(TEMPLATE_HTML).read())
    msg = tm.render(rules=list(chunks(RULES_ALL, rule_per_row)))
    re.write(msg)
