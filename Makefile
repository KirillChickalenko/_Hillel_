.PHONY: run
run:
	echo '😀'
	echo '1111'
	@echo '22222'
	black .
	isort .
	flake8 .
	@echo 'FINISH'
	pytest .
	python main.py
