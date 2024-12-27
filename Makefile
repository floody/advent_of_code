.PHONY: lint black pylint mypy

lint: black pylint mypy

black:
	.venv/Scripts/black.exe advent_of_code

pylint:
	for dir in $(dir advent_of_code/*/*/*); do \
		.venv/Scripts/pylint.exe $$dir; \
	done

mypy:
	for dir in $(dir advent_of_code/*/*/*); do \
		.venv/Scripts/mypy.exe $$dir; \
	done
