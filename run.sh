#!/bin/bash

DB_HOST=${DB_HOST}
DB_HOST=${DB_HOST}
DB_PORT=${DB_PORT}
DB_PORT=-${DB_PORT}

if [ "$DB_PASS" = "**ChangeMe**" ] && [ -n "$DB_1_ENV_MYSQL_PASS" ]; then
    DB_PASS="$DB_1_ENV_MYSQL_PASS"
fi

echo "=> Using the following MySQL/MariaDB configuration:"
echo "========================================================================"
echo "      Database Host Address:  $DB_HOST"
echo "      Database Port number:   $DB_PORT"
echo "      Database Name:          $DB_NAME"
echo "      Database Username:      $DB_USER"
echo "========================================================================"

python manage.py runserver 0.0.0.0:80

