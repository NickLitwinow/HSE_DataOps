include .env
export

MIGRATIONS_DIR = ./migrations

.PHONY: dev.install db.migration.new db.migrate db.rollback

dev.install:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

db.migration.new:
	. venv/bin/activate && yoyo new --sql $(MIGRATIONS_DIR) -m "$(name)"

db.migrate:
	. venv/bin/activate && yoyo apply --database $(DATABASE_URL) $(MIGRATIONS_DIR) --no-config-file --batch

db.rollback:
	. venv/bin/activate && yoyo rollback --database $(DATABASE_URL) $(MIGRATIONS_DIR) --no-config-file --batch
