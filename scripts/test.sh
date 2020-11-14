#!/bin/bash
pycodestyle --max-line-length=100 --ignore=E742,W391 hype/
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Python Lint Error"
    exit $retVal
fi

python -m mypy --ignore-missing-imports hype/
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Python Type Checking Error"
    exit $retVal
fi

python -m pytest --cov=hype/ tests/
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Python Test Error"
    exit $retVal
fi