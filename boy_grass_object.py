from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = 400
        self.y = 90
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    pass

class Balls:
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False





def reset_world():
    global running
    global grass
    global boy
    running = True

    grass = Grass()
    boy = Boy()
    balls = Balls()
    pass

def update_world():

    pass

def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass


open_canvas()


reset_world()


while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
