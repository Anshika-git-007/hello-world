.PHONY: bootstrap clean test
.DEFAULT_GOAL := test

test: clean lint
	@py.test test/ --cov app.py -s

clean:
	@find . -type f -name '*.pyc' -delete

bootstrap:
	@pip install -r requirements.txt
