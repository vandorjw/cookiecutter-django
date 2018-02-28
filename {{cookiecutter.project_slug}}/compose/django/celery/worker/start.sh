#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

celery -A config worker -l INFO -Q default --concurrency=2
