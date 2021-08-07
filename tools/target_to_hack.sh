#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ $target ]; then
	echo "%{F#e51d0b} %{F#ffffff}$target%{u-}"
else
	echo "%{F#e51d0b}%{u-}%{F#ffffff} No target"
fi
