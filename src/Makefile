.PHONY: install frontend messages pip node_modules

install: pip node_modules frontend

pip:
	pip install -r requirements/dev.txt

node_modules:
	npm install

frontend:
	npm run gulp

watch:
	npm run gulp sass:watch

messages:
	django-admin.py compilemessages

clean:
	npm run gulp clean
