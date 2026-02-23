#!/bin/sh
set -e
mkdir -p /data && chown -R 999:999 /data && chmod -R 750 /data
exec gosu app "$@"
