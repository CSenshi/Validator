#!/usr/bin/env python3
import pkgutil
import importlib
from pathlib import Path
import sys
import os
import sys, inspect
import pprint


validator_path = os.path.abspath(Path(__file__).parent.parent.parent)
sys.path += [validator_path]

KEY = "CD4A678E95173E4BE5E27E2C8169F"

README = "README.md"
README_EXAMPLE = "utils/readme/README_EXAMPLE.md"
HTML_DIV_EXAMPLE = "utils/readme/readme_rules_div_example.html"
HTML_REF_EXAMPLE = "utils/readme/readme_rule_ref_example.html"


def writeRules():
    div_str = open(HTML_DIV_EXAMPLE).read()
    ref_str = open(HTML_REF_EXAMPLE).read()

    for (_, file, _) in pkgutil.iter_modules(['validator/rules_src']):
        # Get Absolute Path
        module_abs_path = f"validator.rules_src.{file}"
        pkg = importlib.import_module(module_abs_path)


        # Import all classes from given modules
        names = [x for x in pkg.__dict__ if not x.startswith("_")]
        class_name = names[-1] 

        # get all clases from file
        clsmembers = inspect.getmembers(sys.modules[module_abs_path], inspect.isclass)
        
        # get doc from file
        cur_class = dict(clsmembers)[class_name]
        doc = cur_class.__doc__
        
        print(doc)
        
with open(README_EXAMPLE, "r") as ex, open(README, "w") as re:
    while True:
        line = ex.readline()
        if not line:
            break
        if KEY in line:
            writeRules()