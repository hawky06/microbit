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

jingle = [
 'e:2','e:2','e:4','e:2','e:2','e:4','e:2','g:2','c','d','e:8','f:2','f:2','f:3',
 'f:1','f:2','e:2','e:2','e:1','e:1','e:2','d:2','d:2','e:2','d:4','g:4',
 'e:2','e:2','e:4','e:2','e:2','e:4','e:2','g:2','c','d','e:8','f:2','f:2','f:2',
 'f:2','f:2','e:2','e:2','e:1','e:1','g:2','g:2','f:2','d:2', 'c:4'
]

while True:
    if button_a.is_pressed():
        music.play(jingle,wait=False,loop=False)
        display.scroll("jingle bells",wait=False,loop=False)
    elif button_b.is_pressed():
        music.play(wewishyou,wait=False,loop=False)
        display.scroll("we wish you a merry christmas",wait=False,loop=False)