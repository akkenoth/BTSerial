#!/usr/bin/bash
# Generate .py files from Qt Designer's .ui files.
# -w for Windows mode.

if [[ $# < 2 ]]; then
	echo "No arguments provided."
	exit 1
fi

PYUIC='pyuic5'
WIN=false
if [[ $1 == '-w' ]]; then
	PYUIC='/c/Python34/Lib/site-packages/PyQt5/pyuic5.bat'
	WIN=true
	shift
fi

while [[ $# > 0 ]]; do
	echo -n "Parsing ${1}... "
	$PYUIC -i 0 -x "${1}" -o "${1%%.ui}.py"
	if [[ "$WIN" == true ]]; then
		echo -n "Converting... "
		dos2unix -q "${1%%.ui}.py"
	fi
	echo "Done!"
	shift
done
