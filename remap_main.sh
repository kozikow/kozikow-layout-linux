# http://kozikow.wordpress.com/2013/11/15/the-only-alternative-keyboard-layout-youll-ever-need-as-a-programmer/

# Reverse all previous remappings.
# This is useful when I unplug and plug keyboard and want to re-run remap.sh
setxkbmap -layout us

# caps lock to ctrl (later xcape will add escape)
# 66 - keycode of caps lock
xmodmap -e "clear lock"
xmodmap -e "keycode 66 = Control_L"
xmodmap -e "add control = Control_L"

# Initial work of remapping enter to ctrl_l/enter
# 36 - keycode of return
spare_modifier="Hyper_L"
xmodmap -e "keycode 36 = $spare_modifier"
xmodmap -e "remove mod4 = $spare_modifier" # hyper_l is mod4 by default
xmodmap -e "add Control = $spare_modifier"
# Map return to an unused keycode (to keep it around for xcape to use).
xmodmap -e "keycode any = Return"

# Right cmd to blue layer button
# 134 - keycode of right cmd
xmodmap -e "clear mod4"
# xmodmap -e "keycode 133 = Meta_R" # mode_switch, third and fourth column of keysym
xmodmap -e "keycode 134 = " # This key will be handled by layer_daemon.py
xmodmap -e "add mod4 = Super_L" # readd back left_cmd as super

# Run blue layer daemon
./run_daemon.sh

# enter, escape and backspace remapping
# Install from https://github.com/alols/xcape
./xcape -d -e "$spare_modifier=Return;Control_L=Escape;Shift_R=BackSpace"
