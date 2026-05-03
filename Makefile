
.PHONY: test coverage clean build black

PYTHON := python3

# run tests without coverage
test:
	$(PYTHON) -m unittest discover -s tests/

# run tests with coverage
coverage:
	coverage run -m unittest discover .
	coverage report -m

# clean up build artifacts and coverage data
clean:
	rm -rf build dist *.egg-info .coverage

# build the packaged distribution
build: clean
	$(PYTHON) -m build

# build the package and deploy to PyPI development
publish-test: build
	$(PYTHON) -m twine upload --repository testpypi dist/*

# build the package and deploy to PyPI production
publish-prod: build
	$(PYTHON) -m twine upload dist/*
	
# lint and formatting the whole codebase with omitted --fast
# to skip the safety check
black:
	black . --fast