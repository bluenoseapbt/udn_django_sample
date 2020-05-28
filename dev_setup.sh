#!/bin/bash
virtualenv -p python3 -q venv
source venv/bin/activate
export CFLAGS="-I/usr/local/include -L/usr/local/lib"

# install requirements
for req in `ls requirements/`; do
    echo "installing requirement [$req]..."
    pip3 install -q -r requirements/${req}
done

