#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ $target ]; then
    echo "%{F#e51d0b}什%{F#ffffff} $target%{u-}"
else
    echo "%{F#e51d0b}ﲅ %{u-}%{F#ffffff} No target"
fi
