.PHONY: run
run:
	python main.py

.PHONY: connect
connect:
	python client.py

.DEFAULT_GOAL := run