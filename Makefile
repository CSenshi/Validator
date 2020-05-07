init:
	pip3 install -r requirements.txt

test:
	pytest --doctest-modules validator/
	pytest

.PHONY: init test