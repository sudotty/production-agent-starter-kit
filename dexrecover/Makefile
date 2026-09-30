.PHONY: install test smoke

install:
	python -m pip install -e .

test:
	python -m unittest discover -s tests -v

smoke:
	dexrecover --help
