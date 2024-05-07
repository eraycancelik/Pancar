#!/bin/bash
echo "bash scripting has been started"

function pancar(){
	echo "echo Pancar v1.02 is launching"
	pipenv shell
}
function run(){
	python main.py
}	
pancar
run
