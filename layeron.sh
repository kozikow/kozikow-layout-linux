#!/bin/bash
# Run xev to find keycodes on your keyboard
# Top row remapping
xmodmap -e "keycode 24 = 1 exclam 1 exclam"
xmodmap -e "keycode 25 = 2 at 2 at"
xmodmap -e "keycode 26 = 3 numbersign 3 numbersign"
xmodmap -e "keycode 27 = 4 dollar 4 dollar"
xmodmap -e "keycode 28 = 5 percent 5 percent"
xmodmap -e "keycode 29 = 6 asciicircum 6 asciicircum"
xmodmap -e "keycode 30 = 7 ampersand 7 ampersand"
xmodmap -e "keycode 31 = 8 asterisk 8 asterisk"
xmodmap -e "keycode 32 = 9 parenleft 9 parenleft"
xmodmap -e "keycode 33 = 0 parenright 0 parenright"

# Middle row remapping
xmodmap -e "keycode 38 = parenleft parenleft parenleft parenleft"
xmodmap -e "keycode 39 = parenright parenright parenright parenright"
xmodmap -e "keycode 40 = braceleft braceleft braceleft braceleft"
xmodmap -e "keycode 41 = braceright braceright braceright braceright"
xmodmap -e "keycode 42 = grave asciitilde grave asciitilde" # g
xmodmap -e "keycode 43 = Left Left Left Down Left " # k
xmodmap -e "keycode 44 = Down Down Down Down Down" # j
xmodmap -e "keycode 45 = Up Up Up Up Up" # h
xmodmap -e "keycode 46 = Right Right Right Down Right" # l
xmodmap -e "keycode 47 = equal plus equal plus"
xmodmap -e "keycode 48 = backslash bar backslash bar"

# Bottom row remapping
xmodmap -e "keycode 52 = bracketleft bracketleft bracketleft bracketleft"
xmodmap -e "keycode 53 = bracketright bracketright bracketright bracketright"
xmodmap -e "keycode 54 = minus minus minus minus"
xmodmap -e "keycode 55 = plus plus plus plus" # 55
xmodmap -e "keycode 58 = underscore underscore underscore underscore" # 58
