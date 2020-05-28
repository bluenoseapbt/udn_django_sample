#!/bin/bash

virtualEnv=$(which virtualenv) >/dev/null
if [[ ${virtualEnv} == "" ]]; then
    echo "Could not find the virtualenv command. Please install or update your path."
    exit -1
fi

pythonVersion=$(which python3) >/dev/null
if [[ ${pythonVersion} == "" ]]; then
    echo "Could not find the python3 command. Please install or update your path."
    exit -1
fi

virtualenv -p python3 -q venv
source venv/bin/activate
export CFLAGS="-I/usr/local/include -L/usr/local/lib"

# install requirements
for req in `ls requirements/`; do
    echo "installing requirement [$req]..."
    pip3 install -q -r requirements/${req}
done

