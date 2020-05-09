PYTEST_TEST=.
DOCEST_TEST=validator/

# Rules Genarot
RULES_GENERATOR_SCRIPT := utils/generate_rules_import.py
GENERATED_RULES_FILE := validator/rules.py

ifdef TEST
	PYTEST_TEST=tests/rules/test_$(TEST).py 
	DOCEST_TEST=validator/rules_src/$(TEST).py
endif

init:
	@echo Generating rules python file...
	chmod 755 $(RULES_GENERATOR_SCRIPT)
	$(RULES_GENERATOR_SCRIPT) $(GENERATED_RULES_FILE)
	@echo Done!

clean:
ifneq ("$(wildcard $(GENERATED_RULES_FILE))","")
	@echo removing generated rules file...
	rm $(GENERATED_RULES_FILE)
endif

test: doctest pytest

install:
	pip3 install -r requirements.txt

doctest:
	pytest --doctest-modules $(DOCEST_TEST)
	@echo ""

pytest:
	pytest $(PYTEST_TEST)
	@echo ""

.PHONY: init test