#!/bin/sh

# Abort script at first error, when a command exits with non-zero status (except in until or while loops, if-tests, list constructs)
set -o errexit
# Causes a pipeline to return the exit status of the last command in the pipe that returned a non-zero return value.
set -o pipefail
# Attempt to use undefined variable outputs error message, and forces an exit
set -o nounset
# Export all defined variables
set -o allexport

cmd="$@"

source /app/.venv/bin/activate

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect("$DATABASE_URL")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

if [ -z ${DATABASE_URL} ]; then
  echo "DATABASE_URL not set, continuing";
else
  until postgres_ready; do
    echo "Postgres cannot be reached..., retrying in 1 second!";
    sleep 1
  done
fi


if [[ -z $cmd ]]; then
  python manage.py migrate --no-input
  python manage.py collectstatic --no-input
  if [ ${AUTO_RELOAD} ]
  then
    gunicorn --config=gunicorn.py config.wsgi --reload
  else
    gunicorn --config=gunicorn.py config.wsgi
  fi
else
  echo "Running command passed (by the compose file)"
  exec $cmd
fi
