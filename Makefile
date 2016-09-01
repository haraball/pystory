init:
	pip install -e .

test:
	pytest

clean:
	rm -fr build dist .egg pystory.egg-info

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload 
	rm -fr build dist .egg pystory.egg-info

