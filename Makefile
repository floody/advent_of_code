.PHONY: lint black pylint mypy

lint: black pylint mypy

black:
	.venv/Scripts/black.exe advent_of_code

pylint:
	.venv/Scripts/pylint.exe advent_of_code/*/*

mypy:
	for dir in $(dir advent_of_code/*/*/*); do \
		.venv/Scripts/mypy.exe $$dir; \
	done
