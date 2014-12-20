clean:
	rm -f *.pyc

test: clean
	nosetests test*.py
