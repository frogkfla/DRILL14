from pico2d import load_image

import game_framework


class Bird:
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAMES_PER_SECOND = 8
    FRAME_COUNT = 14

    def __init__(self, x, y):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0

    def update(self):
        self.frame = (self.frame + self.FRAMES_PER_SECOND *
                      game_framework.frame_time) % self.FRAME_COUNT

    def draw(self):
        frame_index = int(self.frame)
        column = frame_index % 5
        row = frame_index // 5
        source_x = column * self.FRAME_WIDTH
        source_y = 506 - (row + 1) * self.FRAME_HEIGHT
        self.image.clip_draw(
            source_x, source_y, self.FRAME_WIDTH, self.FRAME_HEIGHT,
            self.x, self.y, 110, 100
        )