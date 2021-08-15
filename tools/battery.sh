#!/bin/bash

if [ "$(acpi | awk '{print $3}' | tr -d ',')" != "Discharging" ]; then

	echo -e "%{F#27FF00} %{F#e2ee6a}$(acpi | awk '{print $4}' | tr -d ',')%{u-}"
else
	echo -e "%{F#FF0000} %{F#e2ee6a}$(acpi | awk '{print $4}' | tr -d ',')%{u-}"
fi
