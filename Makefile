.PHONY: run

VENV=venv
ACTIVATE=$(VENV)/bin/activate

run:
	@. $(ACTIVATE) && ( \
		uvicorn src.main:app --reload \
	)
