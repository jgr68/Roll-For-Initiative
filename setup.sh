#!/bin/bash
while read line
do
	flask/bin/pip install "$line"
done < packages.txt
