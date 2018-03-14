#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn --config=gunicorn.py config.wsgi
