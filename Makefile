PYTEST_TEST=.
DOCEST_TEST=validator/

ifdef TEST
	PYTEST_TEST=tests/rules/test_$(TEST).py 
	DOCEST_TEST=validator/rules/$(TEST).py
endif

init:
	pip3 install -r requirements.txt

test: doctest pytest

doctest:
	pytest --doctest-modules $(DOCEST_TEST)
	@echo ""

pytest:
	pytest $(PYTEST_TEST)
	@echo ""

.PHONY: init test