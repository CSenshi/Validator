PYTEST_TEST=.
DOCEST_TEST=validator/

# files
RULES_IMPORT_GENERATOR_SCRIPT := utils/generate_rules_import.py
RULES_TEMPLATE_GENERATOR_SCRIPT := utils/generate_rule_sample.py
README_TEMPLATE_GENERATOR_SCRIPT := utils/readme/generate_readme.py
GENERATED_RULES_FILE := validator/rules.py

ifdef TEST
	PYTEST_TEST=tests/rules/test_$(TEST).py 
	DOCEST_TEST=validator/rules_src/$(TEST).py
endif


init:
	@echo Generating rules python file...
	$(RULES_IMPORT_GENERATOR_SCRIPT) $(GENERATED_RULES_FILE)
	@echo Done!

install:
	pip3 install -r requirements.txt

clean:
ifneq ("$(wildcard $(GENERATED_RULES_FILE))","")
	@echo removing generated rules file...
	rm $(GENERATED_RULES_FILE)
endif

# Test with pytest test/ folder and doctests 
test: doctest pytest check

doctest:
	pytest --doctest-modules $(DOCEST_TEST)
	@echo ""

pytest:
	python3 -m pytest $(PYTEST_TEST)
	@echo ""

# Check for formating
check:
	black --check .

# Fix formating
fix:
	black .

# Generate files
rule:
	@echo Generating rules python file...
	$(RULES_TEMPLATE_GENERATOR_SCRIPT) $(F_NAME)

readme:
	@echo Generating rules python file...
	$(README_TEMPLATE_GENERATOR_SCRIPT)

.PHONY: init test
