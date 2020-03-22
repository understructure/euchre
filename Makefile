
init:
		python3 -m venv .venv; \
		( \
		source .venv/bin/activate; \
		pip install -r requirements.txt; \
		python setup.py develop \
		)
		pre-commit uninstall; \
		pre-commit install -t pre-push; \
		python setup.py develop

format:
		source venv/bin/activate; \
		black .

lint:
		source venv/bin/activate; \
		flake8

build:
		python setup.py sdist bdist_wheel

test:
		source venv/bin/activate; \
		pytest --timeout=60
