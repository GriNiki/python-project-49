install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poytry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl