.PHONY: install frontend messages pip node_modules requirements upgrade

install: pip node_modules frontend

requirements: requirements/base.in
	pip-compile --output-file requirements/base.txt requirements/base.in

pip:
	pip install -r requirements/dev.txt

upgrade:
	pip install pip-tools pur
	pur --skip=Django --no-recursive -r requirements/base.in -r requirements/docker.txt
	pip-compile --upgrade --output-file requirements/base.txt requirements/base.in
# Allow recursive upgrade with base.txt being regenerated
	pur --skip=Django -r requirements/dev.txt

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

coverage:
	py.test --reuse-db --nomigrations --cov --cov-report=term-missing
