from microbit import *
import music
music.set_tempo(ticks=4, bpm=120)

wewishyou = ['a5:2', 'd6:4', 'd6:2', 'e6:2',
'd6:2', 'c#6:2', 'b5:4', 'g5:4', 'b5:2',
'e6:4', 'e6:2', 'f#6:2', 'e6:2', 'd6:2',
'c#6:4', 'a5:4', 'c#6:2', 'f#6:4', 'f#6:2',
'g6:2', 'f#6:2', 'e6:2', 'd6:4', 'b5:4',
'a5:2', 'b5:2', 'e6:2', 'c#6:2', 'd6:2', 'R:4'
]

while True:
    if button_a.is_pressed():
        music.play(wewishyou,wait=False,loop=False)
    elif button_b.is_pressed():
        display.scroll("we wish you a merry christmas",wait=False,loop=False)