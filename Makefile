PYTHON ?= python3

.PHONY: test validate package check

test:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests -v

validate:
	$(PYTHON) tools/package_skill.py --validate-only

package:
	$(PYTHON) tools/package_skill.py

check: test validate package
