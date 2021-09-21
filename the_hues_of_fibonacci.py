import pygame as p, sys

p.init()

font = p.font.SysFont('arial', 42)

pd = p.display
win = pd.set_mode((1280, 720))
pd.set_caption("The Hues of Fibonacci by @Abracadabrazen")

One = abs(-1)
Midnight = (One, 0, 1)
Night = (1, 2, 3)
Dusk = (5, 8, 13)
Dawn = (21, 34, 55)
Noon = (89, 144, 233)
bg = [Midnight, Night, Dusk, Dawn, Noon]
times = ['Midnight', 'Night', 'Dusk', 'Dawn', 'Noon']

x = 0
while True:
    text = font.render(times[x], True, (255, 255, 255))

    win.fill(bg[x])
    win.blit(text, (550, 660))

    for event in p.event.get():
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE: sys.exit()
            if event.key == p.K_RIGHT: x += 1
            if event.key == p.K_LEFT: x -= 1

        if x < 0: x = len(bg) - 1
        if x >= len(bg): x = 0

    pd.update()