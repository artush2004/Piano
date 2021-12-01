import pygame
from random import randrange

def display():
    pygame.init()
    dis = pygame.display.set_mode([600, 800])
    return dis

def game(dis):
    clock = pygame.time.Clock()
    fps = 50
    arg = []
    count = 0
    arg.append((randrange(0, 600, 150), -195, 150, 195))
    pygame.mixer.music.load("Patrick Trentini - Friday Rain.mp3")
    pygame.mixer.music.play()
    while True:
        dis.fill("pink")
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        for el in arg:
            pi = pygame.Rect(el)
            pygame.draw.rect(dis, pygame.Color("black"), pi, 0)

        if len(arg) == 0 or arg[-1][1] == 0:
            el = randrange(0, 600, 150), -200, 150, 195
            arg.append(el)
            if count > 10:
                pygame.mixer.music.pause()


        if len(arg) != 0 and arg[0][0]//150 == keys():
            pygame.mixer.music.unpause()
            count = 0
            arg.pop(0)
            fps += 20

        if len(arg) != 0 and arg[0][1]+195 == 800:
            end(dis)

        arg = move(arg)
        count += 1

        clock.tick(fps)
        pygame.display.flip()

def move(arg):
    sl = []
    for el in arg:
        el = el[0], el[1]+1, el[2], el[3]
        sl.append(el)
    return sl

def keys():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        return 0
    if key[pygame.K_s]:
        return 1
    if key[pygame.K_d]:
        return 2
    if key[pygame.K_f]:
        return 3

def end(dis):
    while True:
        f_end = pygame.font.SysFont("Arial", 66, bold=True)
        r_end = f_end.render("GAME OVER", 1, pygame.Color("black"))
        dis.blit(r_end, (130, 300))
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

def main():
    dis = display()
    game(dis)

if __name__ == '__main__':
    main()
