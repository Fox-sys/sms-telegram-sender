#!/usr/bin/env bash
set -e
if [ -z "$API_LOG_LEVEL" ]; then
  API_LOG_LEVEL=info
fi
if [ -z "$API_PORT" ]; then
  API_PORT=8080
fi


exec python -m src.run.main host=0.0.0.0 port="$API_PORT" log_level="$API_LOG_LEVEL" forwarded_allow_ips=* timeout_keep_alive=30 workers=20