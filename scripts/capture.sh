#!/bin/bash

echo "+------------------------------------------------+"
echo "| Capture et éclairage dans la cabane à mésanges |"
echo "+------------------------------------------------+"
echo ""

read -p "Eclairage (O/n): " light

if [[ $light == [oO] || -z $light ]]; then

	read -p "Duty cycle(100): " dc
	if [[ -z $dc ]]; then dc=100; fi

	read -p "Sleep(30): " sleep
	if [[ -z $sleep ]]; then sleep=30; fi

	python3 light.py $dc $sleep &
fi

read -p "Capture [image]/[film] (i/f/N): " capture

if [[ $capture == [i] ]]; then

	python3 picture.py

elif [[ $capture == [f] ]]; then

	read -p "Sleep(30): " duration
	if [[ -z $duration ]]; then duration=30; fi

	python3 record.py $duration
fi
