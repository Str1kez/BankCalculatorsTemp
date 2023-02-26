PYTHONPATH=PYTHONPATH=${PWD}
PYTHON=$(PYTHONPATH) python3

credit:
	$(PYTHON) credit_calc/main.py

deposit:
	$(PYTHON) deposit_calc/main.py

