#!/bin/bash

set -euo pipefail

DB_HOST="CHANGE_ME_DB_HOST"
DB_USER="CHANGE_ME_DB_USER"
DB_PASS="CHANGE_ME_DB_PASSWORD"

if ! command -v mysql >/dev/null 2>&1; then
  echo "mysql client belum ter-install. Install mysql atau mariadb client terlebih dahulu."
  exit 1
fi

MYSQL_PWD="$DB_PASS" mysql \
  --host="$DB_HOST" \
  --user="$DB_USER" \
  --connect-timeout=5 \
  --batch \
  --skip-column-names \
  --execute="SHOW DATABASES;"