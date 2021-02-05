init:
	chmod +x .githooks/pre-commit; \
	git config core.hooksPath .githooks; \
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt
