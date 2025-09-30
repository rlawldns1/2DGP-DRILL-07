from pico2d import *
import random


# Game object class here


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True

open_canvas()

while running:
    pass

close_canvas()
