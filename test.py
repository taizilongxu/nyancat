#!/usr/bin/env python
# encoding: utf-8
from frame import frames
import subprocess
import time
def linesnum():
    '''测试屏幕显示行数,每行字符数'''
    num = subprocess.check_output('stty size', shell=True)
    tmp = num.split(' ')
    return int(tmp[0]), int(tmp[1])

# terminal_width = 80
# terminal_height = 24

using_automatic_width = 0
using_automatic_height = 0


terminal_height, terminal_width = linesnum()

FRAME_HEIGHT = FRAME_WIDTH = 64

min_col = (FRAME_WIDTH - terminal_width/2) / 2;
max_col = (FRAME_WIDTH + terminal_width/2) / 2;
min_row = (FRAME_HEIGHT - (terminal_height-1)) / 2;
max_row = (FRAME_HEIGHT + (terminal_height-1)) / 2;

last = 0
output = ' '

colors = {}
colors[',']  = "\033[48;5;17m";
colors['.']  = "\033[48;5;231m";
colors['\''] = "\033[48;5;16m";
colors['@']  = "\033[48;5;230m";
colors['$']  = "\033[48;5;175m";
colors['-']  = "\033[48;5;162m";
colors['>']  = "\033[48;5;196m";
colors['&']  = "\033[48;5;214m";
colors['+']  = "\033[48;5;226m";
colors['#']  = "\033[48;5;118m";
colors['=']  = "\033[48;5;33m";
colors[';']  = "\033[48;5;19m";
colors['*']  = "\033[48;5;240m";
colors['%']  = "\033[48;5;175m";

i = 0  # frame
# f = 0  # total frames passed
clear_screen = 1
# if clear_screen:
#     print '\033[H\033[2J\033[?25l',
# else:
#     print '\033[s',

always_escape = 0

while True:
    # if clear_screen:
    #     print '\033[H]',
    # else:
    #     print '\033[u]',
    for y in range(min_row, max_row):
        for x in range(min_col, max_col):
            if  23 < y < 43 and x < 0:
                mod_x = ((-x+2) % 16) / 8;
                if (i / 2) % 2:
                    mod_x = 1 - mod_x;
                rainbow = ",,>>&&&+++###==;;;,,"

                tmp = mod_x + y - 23
                if tmp in range(len(rainbow)):
                    color = rainbow[mod_x + y - 23]
                else:
                    color = ','
            elif x < 0 or y < 0 or y >= FRAME_HEIGHT or x >= FRAME_WIDTH:
                color = ','
            else:
                color = frames[i][y][x]

            if always_escape:
                print colors[color],
            else:
                if color != last and colors.has_key(color):
                    last = color;
                    print colors[color]+output,
                else:
                    print output,
        print
    i += 1
    if i == 11:
        i = 0
    last = 0
    time.sleep(0.1)


