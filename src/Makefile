.PHONY: install frontend messages pip node_modules requirements upgrade

install: pip node_modules frontend

requirements: requirements/base.in
	pip-compile -v --output-file requirements/base.txt requirements/base.in

pip:
	pip install -r requirements/dev.txt

pip-sync:
	pip-sync requirements/base.txt requirements/dev.txt

upgrade:
	pur --patch=Django -r requirements/base.in
	pur --no-recursive -r requirements/docker.txt
	pur --no-recursive -r requirements/dev.txt
	pip-compile -v --upgrade --output-file requirements/base.txt requirements/base.in

node_modules:
	npm install

frontend:
	npm run gulp

images:
	npm run gulp imagemin

watch:
	npm run gulp watch

messages:
	django-admin.py compilemessages

clean:
	npm run gulp clean

test:
	py.test --reuse-db --nomigrations

retest:
	py.test --reuse-db --nomigrations --lf -vvs

coverage:
	py.test --reuse-db --nomigrations --cov --cov-report=term-missing

isort:
	isort -w1000 --recursive ./
