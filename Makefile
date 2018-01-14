help:
	@echo '
	@echo 'Usage:                                                                           '
	@echo '     make requirements.py        install requirements for local development      '
	@echo '     make quality                run isort and PEP8                              '
	@echo '     make run_tests              run all python tests from tests directory       '
	@echo '

requirements.py:
	pip install -r requirements/requirements.txt

quality:
	isort --check-only --recursive .
	pycodestyle *.py tests/*.py

run_tests: quality
	nosetests
