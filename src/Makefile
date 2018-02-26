.PHONY: install frontend messages pip node_modules

install: pip node_modules frontend

pip:
	pip install -r requirements/dev.txt

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
