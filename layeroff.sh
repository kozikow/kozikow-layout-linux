#!/bin/bash
xmodmap -e "keycode 24 = q Q q Q"
xmodmap -e "keycode 25 = w W w W"
xmodmap -e "keycode 26 = e E e E"
xmodmap -e "keycode 27 = r R r R"
xmodmap -e "keycode 28 = t T t T"
xmodmap -e "keycode 29 = y Y y Y"
xmodmap -e "keycode 30 = u U u U"
xmodmap -e "keycode 31 = i I i I"
xmodmap -e "keycode 32 = o O o O"
xmodmap -e "keycode 33 = p P p P"

# Middle row remapping
xmodmap -e "keycode 38 = a A a A"
xmodmap -e "keycode 39 = s S s S"
xmodmap -e "keycode 40 = d D d D"
xmodmap -e "keycode 41 = f F f F"
xmodmap -e "keycode 42 = g G g G" # g
xmodmap -e "keycode 43 = h H h H" # k
xmodmap -e "keycode 44 = j J j J" # j
xmodmap -e "keycode 45 = k K k K" # h
xmodmap -e "keycode 46 = l L l L" # l
xmodmap -e "keycode 47 = semicolon colon semicolon colon"
xmodmap -e "keycode 48 = apostrophe quotedbl apostrophe quotedbl"

# Bottom row remapping
xmodmap -e "keycode 52 = z Z z Z"
xmodmap -e "keycode 53 = x X x X"
xmodmap -e "keycode 54 = c C c C"
xmodmap -e "keycode 55 = v V v V"
xmodmap -e "keycode 58 = m M m M"
