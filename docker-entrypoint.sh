#!/bin/bash

# usage: file_env VAR [DEFAULT]
#    ie: file_env 'XYZ_DB_PASSWORD' 'example'
# (will allow for "$XYZ_DB_PASSWORD_FILE" to fill in the value of
#  "$XYZ_DB_PASSWORD" from a file, especially for Docker's secrets feature)
file_env() {
    local var="$1"
    local fileVar="${var}_FILE"
    local def="${2:-}"
    if [ "${!var:-}" ] && [ "${!fileVar:-}" ]; then
        echo >&2 "error: both $var and $fileVar are set (but are exclusive)"
        exit 1
    fi
    local val="$def"
    if [ "${!var:-}" ]; then
        val="${!var}"
    elif [ "${!fileVar:-}" ]; then
        val="$(< "${!fileVar}")"
    fi
    export "$var"="$val"
    unset "$fileVar"
}

: ${LISTEN_PORT:=8000}
: ${LISTEN_ADDRESS:=0.0.0.0}

file_env TRELLO_APIKEY
file_env TRELLO_TOKEN

if [[ -z ${TRELLO_APIKEY} || -z ${TRELLO_TOKEN} ]]; then
  echo >&2 "ERROR: missing TRELLO_APIKEY or TRELLO_TOKEN"
  sleep 5
  exit 1
fi

if [[ "$1" ]]; then
  cmd="$@"
else
  python manage.py migrate
  cmd="python manage.py runserver ${LISTEN_ADDRESS}:${LISTEN_PORT}"
fi

exec ${cmd}

