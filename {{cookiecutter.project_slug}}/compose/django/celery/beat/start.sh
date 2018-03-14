#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

rm -f /app/celerybeat.pid || true
rm -f /app/celerybeat-schedule || true

celery -A config beat -l INFO -s /app/celerybeat-schedule --pidfile=/app/celerybeat.pid
