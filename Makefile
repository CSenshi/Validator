PYTEST_TEST=.
DOCEST_TEST=validator/

# Rules Genarot
RULES_GENERATOR_SCRIPT := utils/generate_rules_import.py
GENERATED_RULES_FILE := validator/rules.py

ifdef TEST
	PYTEST_TEST=tests/rules/test_$(TEST).py 
	DOCEST_TEST=validator/rules_src/$(TEST).py
endif

ifdef PEP8
	SHOW_PEP=--show-pep8 
endif

init:
	@echo Generating rules python file...
	chmod 755 $(RULES_GENERATOR_SCRIPT)
	$(RULES_GENERATOR_SCRIPT) $(GENERATED_RULES_FILE)
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

# Check for formating and PEP8 standarts
check: _check_format _check_standarts

_check_format:
	black --check .

_check_standarts:
	pycodestyle --show-source $(SHOW_PEP) .


# Fix formating and most of PEP8 standarts
fix: _fix_format _fix_style

_fix_format:
	black .

_fix_style:
	autopep8 --in-place --aggressive --aggressive --recursive .


.PHONY: init test