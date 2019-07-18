#!/bin/bash

function listContains () {
    containsItem="False"
    
    local pattern="$1"
    shift
    local array=("$@")
    for arg in $array; do
        if [ "$arg" = "$pattern" ]; then
            containsItem="True"
        fi
    done

    echo $containsItem
}

args=("$@")

# help option
if [ $(listContains "--help" "${args[@]}") = "True" ]; then
python3 - <<END
from os.path import dirname, abspath
cwd = dirname(abspath(__file__))
import sys
sys.path.append(cwd)
import table_generator
print(table_generator.__doc__)
END
fi

# find file
file="none"
for arg in $@; do
    if [ -f $arg ]; then
        file="$arg"
    fi
done

if [ $file = "none" ]; then
    echo "invalid or unspecified filepath input"
    exit 1
fi

# header option
header="False"
if [ $(listContains "-h" "${args[@]}") = "True" ]; then
    header="True"
fi

# complete file option
completeFile="False"
if [ $(listContains "-c" "${args[@]}") = "True" ]; then
    completeFile="True"
fi

# run python script
python3 table_generator.py $file $completeFile $header
