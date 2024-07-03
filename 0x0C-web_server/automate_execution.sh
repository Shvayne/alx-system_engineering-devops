#!/usr/bin/env bash

Directory="$(dirname "$0")"

find "$Directory" -type f ! -name '*.*' -exec chmod +x {} \;

