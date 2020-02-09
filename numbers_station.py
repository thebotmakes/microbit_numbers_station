from microbit import *
import random
import speech
import music

numbers = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']

group = ['one', 'three', 'seven', 'zero', 'zero']

breath = 300

def say_codes():
    code_list = []
    p = 0
    while p < 5:
        x = random.choice(numbers)
        code_list.append(x)
        p += 1
    r = 0
    while r < 2:
        z = 0
        while z < 4:
            speech.say(code_list[z])
            sleep(breath)
            z += 1
        speech.say(code_list[4], pitch=50, mouth=150, throat=150)
        sleep(breath)
        r += 1
        sleep(breath)

def say_group():
    for number in group:
        speech.say(number)
        sleep(breath)

def play_music():
    music.play(music.PYTHON, loop=False)
    music.stop

while True:
    play_music()
    say_group()
    sleep(breath)
    say_group()
    sleep(breath)
    say_codes()
    say_codes()
    say_codes()
    say_codes()
    say_codes()