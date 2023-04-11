.PHONY: run

VENV=venv
ACTIVATE=$(VENV)/bin/activate

run:
	@. $(ACTIVATE) && ( \
		uvicorn src.main:app --reload \
	)

freeze:
	@. $(ACTIVATE) && ( \
		pip freeze >requirements.txt \
	)

install:
	@. $(ACTIVATE) && ( \
		pip install -r requirements.txt \
	)
