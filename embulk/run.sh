#!/bin/bash
set -euxo pipefail

keyword=$1
diff_path="./diffs/${keyword}.yml"

keyword=${keyword} embulk run configs/config.yml.liquid -c "$diff_path"
