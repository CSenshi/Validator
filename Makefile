PYTEST_TEST=.
DOCEST_TEST=validator/

# files
RULES_IMPORT_GENERATOR_SCRIPT := utils/generate_rules_import.py
RULES_TEMPLATE_GENERATOR_SCRIPT := utils/generate_rule/generate_rule_sample.py
README_TEMPLATE_GENERATOR_SCRIPT := utils/readme/generate_readme.py
GENERATED_RULES_FILE := validator/rules.py

ifdef TEST
	PYTEST_TEST=tests/rules/test_$(TEST).py 
	DOCEST_TEST=validator/rules_src/$(TEST).py
endif


init:
	$(RULES_IMPORT_GENERATOR_SCRIPT) $(GENERATED_RULES_FILE)

install:
	pip3 install -r requirements.txt

clean:
	git clean -xdf

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
	$(RULES_TEMPLATE_GENERATOR_SCRIPT) $(F_NAME)

readme: init
	$(README_TEMPLATE_GENERATOR_SCRIPT)

# Upload to pip
pip-upload: build-dist upload-dist

build-dist:
	python3 setup.py bdist_wheel sdist

upload-dist:
	twine upload dist/*

.PHONY: init test
