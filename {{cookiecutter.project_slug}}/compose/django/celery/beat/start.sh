#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

celery -A config beat -l INFO
