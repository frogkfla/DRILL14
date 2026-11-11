from pico2d import get_canvas_width, load_image


## 설명 커밋 위한 수정
import game_framework


class Bird:
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAMES_PER_SECOND = 8
    FRAME_COUNT = 14
    DRAW_WIDTH = 110
    DRAW_HEIGHT = 100

    def __init__(self, x, y, speed=140, direction=1):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.speed = speed
        self.direction = direction
        self.frame = 0

    def update(self):
        self.frame = (self.frame + self.FRAMES_PER_SECOND *
                      game_framework.frame_time) % self.FRAME_COUNT
        self.x += self.direction * self.speed * game_framework.frame_time

        left_bound = self.DRAW_WIDTH / 2
        right_bound = get_canvas_width() - self.DRAW_WIDTH / 2
        if self.x < left_bound:
            self.x = left_bound
            self.direction = 1
        elif self.x > right_bound:
            self.x = right_bound
            self.direction = -1

    def draw(self):
        frame_index = int(self.frame)
        column = frame_index % 5
        row = frame_index // 5
        source_x = column * self.FRAME_WIDTH
        source_y = 506 - (row + 1) * self.FRAME_HEIGHT
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            source_x, source_y, self.FRAME_WIDTH, self.FRAME_HEIGHT,
            0, flip, self.x, self.y, self.DRAW_WIDTH, self.DRAW_HEIGHT
        )
