from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(0,600)
        self.y = 90
        self.frame = random.randint(0,7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

class SBalls:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(100, 700)
        self.y = 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 40:
            self.y -= random.randint(1, 10)


class BBalls:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(100, 700)
        self.y = 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 40:
            self.y -= random.randint(1, 10)


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
    global world
    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(10)]
    world += team

    SSballs = [SBalls() for _ in range(10)]
    world += SSballs

    BBballs = [BBalls() for _ in range(10)]
    world += BBballs


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()


reset_world()


while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
