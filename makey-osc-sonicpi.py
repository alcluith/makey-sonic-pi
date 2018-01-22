###########################################################################
# Pygame Zero program allowing MaKey MaKey to trigger sounds in Sonic Pi
# Claire Quigley, January 2018
###########################################################################

from random import randint
from pythonosc import osc_message_builder
from pythonosc import udp_client


# set size of Pygame Zero window
WIDTH = 800
HEIGHT = 600
middle_x = WIDTH / 2
middle_y = HEIGHT / 2

# where to send the OSC messages (assuming Sonic Pi is
# running on the same machine as Pygame Zero).  Sonic Pi
# listens for OSC messages on Port 4559
sender = udp_client.SimpleUDPClient("127.0.0.1", 4559)

# screen colors
screen_r = 0
screen_g = 0
screen_b = 0


def draw():
    screen.fill((screen_r, screen_g, screen_b))

# for LEFT, RIGHT, UP, DOWN and SPACE symbols on MaKey MaKey.
# Add extra key connections from jumper wires on back of the
# MaKey MaKey here (e.g. w,s,a,d)
def on_key_up(key):
    global screen_r, screen_g, screen_b, sender
    if key == keys.UP:
        screen_r = 0
        screen_g = 255
        screen_b = 255
        sender.send_message('/play', 0 )
    elif key == keys.RIGHT:
        screen_r = 0
        screen_g = 0
        screen_b = 255
        sender.send_message('/play', 1 )
    elif key == keys.DOWN:
        screen_r = 0
        screen_g = 255
        screen_b = 0
        sender.send_message('/play', 2 )
    elif key == keys.LEFT:
        screen_r = 255
        screen_g = 255
        screen_b = 0
        sender.send_message('/play', 3 )
    elif key == keys.SPACE:
        screen_r = 0
        screen_g = 255
        screen_b = 0
        sender.send_message('/play', 4 )
    else:
        pass
    return

#for CLICK symbol on MaKey MaKey
def on_mouse_up():
    global screen_r, screen_g, screen_b, sender
    screen_r = 255
    screen_g = 0
    screen_b = 0
    sender.send_message('/play', 5 )
    return

