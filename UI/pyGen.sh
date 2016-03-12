#!/usr/bin/bash
# Generate .py files from Qt Designer's .ui files.
# -w for Windows mode.

if [[ $# < 2 ]]; then
	echo "No arguments provided."
	exit 1
fi

PYUIC='pyuic5'
if [[ $1 == '-w' ]]; then
	PYUIC='/c/Python34/Lib/site-packages/PyQt5/pyuic5.bat'
	shift
fi

while [[ $# > 0 ]]; do
	echo -n "Parsing ${1}... "
	$PYUIC -x "${1}" -o "${1%%.ui}.py"
	echo "Done!"
	shift
done
