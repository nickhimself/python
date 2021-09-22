from pytube import YouTube as yt
import tkinter
import pygame

pygame.init()
clock = pygame.time.Clock()
f5 = pygame.display.update

black = (0, 0, 0)
grey = (128, 128, 128)
white = (255, 255, 255)

w, h = 256, 256
bg = (255, 255, 255)

pygame.display.set_caption('downloader')
window = pygame.display.set_mode((w, h))

window.fill(bg)

rectw, recth = 236, 236
pygame.draw.rect(window, grey, (10, 10, rectw, recth))
f5()

itag = [(137, 1080), (22, 720), (21, 480), (18, 360)]
rect_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 0), (64, 64, 64), (128, 128, 128)]

text_x = rectw / 2
text_y = recth / 2
text_size = 64
text_string = ''
font = pygame.font.SysFont(pygame.font.get_default_font(), text_size)
text_shadow = font.render(text_string, True, black)
text_surface = font.render(text_string, True, white)
text_rect = text_surface.get_rect(center=(w / 2, h / 2))
window.blit(text_shadow, (text_rect.x + 3, text_rect.y + 2))
window.blit(text_surface, (text_rect.x, text_rect.y))

x = 5
trying = False
tried = False
downloading = False
running = True
while running:
    #print(f'x: {x}, trying: {trying}, tried: {tried}, downloading: {downloading}')
    
    if not trying and not tried and not downloading:
        window.fill(bg)
        text_string = 'ready'
        x = 6

    if downloading:
        window.fill(bg)
        text_string = 'working'
        text_shadow = font.render(text_string, True, black)
        text_surface = font.render(text_string, True, white)
        text_rect = text_surface.get_rect(center=(w / 2, h / 2))
        window.blit(text_shadow, (text_rect.x + 3, text_rect.y + 2))
        window.blit(text_surface, (text_rect.x, text_rect.y))
        f5()
        try:
            item.download('C:/Users/Nick/Desktop', skip_existing=True)
        except:
            quit()

        tried = False
        trying = False
        downloading = False

    if trying and not tried:
        text = str(tkinter.Tk().clipboard_get())
        url = text.split('%')[0]
        streams = yt(url).streams.filter(progressive=True,file_extension='mp4')

        x = 0
        item = streams.get_by_itag(itag[x][0])

        if item != None: pygame.draw.rect(window, (255, 0, 0), (10, 10, 236, 236))

        if item == None:
            x += 1
            item = streams.get_by_itag(itag[x][0])

        if item == None:
            x += 1
            item = streams.get_by_itag(itag[x][0])

        if item == None:
            x += 1
            item = streams.get_by_itag(itag[x][0])

        if item == None:
            x += 1

        if itag[x][0] == 137: text_string = '1080p'
        elif itag[x][0] == 22: text_string = '720p'
        elif itag[x][0] == 21: text_string = '480p'
        else: text_string = '360p'

        print(itag[x][0])
        trying = True
        tried = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not tried: trying = True
            if tried: downloading = True

    pygame.draw.rect(window, rect_colors[x], (10, 10, 236, 236))

    text_shadow = font.render(text_string, True, black)
    text_surface = font.render(text_string, True, white)
    text_rect = text_surface.get_rect(center=(w / 2, h / 2))

    window.blit(text_shadow, (text_rect.x + 3, text_rect.y + 2))
    window.blit(text_surface, (text_rect.x, text_rect.y))

    f5()
    clock.tick(60)

quit()