#!/bin/bash

count="$1"

head -n "${count:-1}" /usr/src/objects/obj_v00.txt | xargs -n 2 sh -c 'curl --insecure -o /usr/src/objects/abc/$1 $0'