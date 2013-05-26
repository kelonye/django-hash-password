publish:
	@python setup.py sdist upload

clean:
	@rm -rf build dist django_hash_password.egg-info $(shell find -name ='*.pyc')

.PHONY: publish clean