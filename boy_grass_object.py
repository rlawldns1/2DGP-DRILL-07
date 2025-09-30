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

def reset_world():
    pass

def update_world():
    pass

running = True

open_canvas()





reset_world()





while running:
    handle_events()
    update_world()
    pass

close_canvas()
