#!/bin/bash

#
# Script de capture et d'éclairage dans la cabane à mésanges.
#
# light.py [DutyCycle] [Sleep]
#   DutyCycle : intensité de l'éclairage de 0 à 100.
#   Sleep : temps d'éclairage.
#

echo "+------------------------------------------------+"
echo "| Capture et éclairage dans la cabane à mésanges |"
echo "+------------------------------------------------+"
echo ""

read -p "Eclairage (o/n): " light

if [[ $light == [o] ]]; then

	read -p "Duty cycle: " dc
	read -p "Sleep: " sleep

	python3 light.py $dc $sleep

fi

read -p "Capture [image]/[film] (i/f/n): " capture

if [[ $capture == [i] ]]; then

	python3 picture.py

elif [[ $capture == [f] ]]; then

	read -p "Sleep: " duration

	python3 record.py $duration

fi
