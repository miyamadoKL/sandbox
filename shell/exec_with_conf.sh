#!/bin/sh

#Input conf.txt as the 1st argument
if [ "$1" = "" ]; then
  COUNTRY="World"
else
  . $1
fi

echo "Hello ${COUNTRY}!"
