import random

from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from bird import Bird

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    speeds = random.sample(range(100, 191), 10)
    for row in range(2):
        for column in range(5):
            bird_index = row * 5 + column
            x = 160 + column * 320 + random.uniform(-80, 80)
            y = 190 + row * 220 + random.uniform(-20, 20)
            direction = 1 if bird_index % 2 == 0 else -1
            bird = Bird(x, y, speeds[bird_index], direction)
            game_world.add_oject(bird)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









