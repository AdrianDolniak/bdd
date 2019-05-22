.PHONY: test

lint:
	flake8 ssh.py web.py

test_ssh:
	behave ssh.feature

test_web:
	behave web.feature

test:
	behave