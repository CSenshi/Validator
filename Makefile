init:
	pip3 install -r requirements.txt

test: doctest pytest

doctest:
	pytest --doctest-modules validator/
	@echo ""

pytest:
	pytest
	@echo ""

.PHONY: init test