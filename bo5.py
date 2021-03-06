from collections import namedtuple
import random

W = 800
H = 600
RED = 200, 0, 0
BLUE = 0, 0, 200
GREEN = 0, 200, 0

ball = Rect((W/2, H/2), (30, 30))
Direction = namedtuple('Direction', 'x y')
ball_dir = Direction(5, 5)

bat = Rect((W/2, 0.96 * H), (150, 15))
N_BLOCKS = 8
BLOCK_W = W / N_BLOCKS
BLOCK_H = BLOCK_W / 4

blocks = []
for n_block in range(N_BLOCKS):
    block = Rect((n_block * BLOCK_W, 0), (BLOCK_W, BLOCK_H))
    blocks.append((block, random.choice([RED, GREEN, BLUE])))

def draw_blocks():
    for block, colour in blocks:
        print(block)
        screen.draw.filled_rect(block, colour)

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, RED)
    screen.draw.filled_rect(bat, RED)
    draw_blocks()

def on_key_down():
    import sys
    sys.exit()

def on_mouse_move(pos):
    x, y = pos
    bat.center = (x, bat.center[1])

def move(ball):
    """returns a new ball at a new position
    """
    global ball_dir
    ball.move_ip(ball_dir)

def boubce():
    if ball.x > W or ball.x <= 0:
        ball_dir = Direction(-1 * ball_dir.x, ball_dir.y)

    if ball.y > H or ball.y <= 0:
        ball_dir = Direction(ball_dir.x, ball_dir.y * -1)



def update():
    move(ball)
