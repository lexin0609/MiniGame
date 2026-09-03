#imports
import pygame
import random

#initialize game engine
pygame.init()

#window
size = (1000, 1000)
tittle = ('My first game')
screen = pygame.display.set_mode(size)
pygame.display.set_caption(tittle)
image = pygame.image.load('домик.png')
pygame.display.set_icon(image)

#fps
clock = pygame.time.Clock()
fps = 60

#colors
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
dark_blue = (0, 0, 139)
dark_green = (0, 100, 0)
brown = (139, 69, 19)
light_brown = (160, 82, 45)
light_light_brown = (210, 105, 30)
window = (128, 128, 128)
light_window = (218, 165, 32)
black = (0, 0, 0)
grey = (128, 128, 128)
white = (255, 255, 255)
dark_grey = (105, 105, 105)
ck = (0, 0, 0)
silver = (220, 220, 220)
red = (255, 0, 0)



darkness = pygame.Surface(size)
darkness.set_alpha(150)
darkness.fill((0, 0, 0))
color_clouds = pygame.Surface((1000, 500))
color_clouds.set_alpha(150)
color_clouds.fill((124, 128, 135))

movement_sun = pygame.Surface((1000,500))
movement_sun.set_alpha(150)
movement_sun.fill((yellow))

#font
font = pygame.font.SysFont('arialblack', 32)

press_n = font.render('n - ночь', 1, black)
press_d = font.render('d - день', 1, black)
press_w = font.render('w - свет в окне', 1, black)

#drawing stages
def draw_sky():
    #sky
    pygame.draw.rect(screen, sky_color, [0, 0, 1000, 500])
    #sun
    pygame.draw.ellipse(screen, color_sun, [700, 200, 100, 100])


def draw_clouds(x, y):
    pygame.draw.ellipse(color_clouds, cloud_color, [x, y + 16, 20, 20])
    pygame.draw.ellipse(color_clouds, cloud_color, [x + 12, y + 8, 16, 16])
    pygame.draw.ellipse(color_clouds, cloud_color, [x + 20, y, 32, 32])
    pygame.draw.ellipse(color_clouds, cloud_color, [x + 40, y + 16, 20, 20])
    pygame.draw.rect(color_clouds, cloud_color, [x + 12, y + 16, 36, 20])


def draw_moon(x, y):
    pygame.draw.ellipse(screen, color_sun, [x, y, 100, 100])
    pygame.draw.ellipse(screen, sky_color, [x + 25, y + 15, 80, 80])


def draw_house(x, y, width, height):
    draw_wall(x, y, width, height)
    draw_roof(x)
    draw_window()
    draw_door()


def draw_wall(x, y, width, height):
    pygame.draw.rect(screen, wall_color, [x, y, width, height])


def draw_roof(x):
    pygame.draw.polygon(screen, brown, [(150, 600), (x + 150, 450), (550, 600)])


def draw_window():
    pygame.draw.ellipse(screen, window_color, [225, 700, 100, 100])
    pygame.draw.line(screen, brown, [275, 700], [275, 800], 5)
    pygame.draw.line(screen, brown, [225, 750], [325, 750], 5)


def draw_door():
    pygame.draw.rect(screen, door_color, [350, 800, 100, 150])


stars = []
for i in range(400):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 500)
    r = random.randrange(3, 4)
    stars.append([x, y, r, r])

clouds = []
for n in range(40):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 400)
    clouds.append([x, y])

#config
light_from_window = False
day = True
run = True

#game loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                day = not day
            elif event.key == pygame.K_d:
                day = True
            elif event.key == pygame.K_w:
                light_from_window = not light_from_window



    #game conditions
    if day:
        grass_color = green
        sky_color = blue
        cloud_color = silver
        color_sun = yellow
        if not light_from_window:
            window_color = window
            wall_color = light_brown
            door_color = dark_grey
            cloud_color = silver
        else:
            window_color = light_window
            wall_color = light_brown
            door_color = dark_grey
            cloud_color = silver
    else:

        sky_color = dark_blue
        grass_color = dark_green
        cloud_color = dark_grey
        color_sun = white
        if not light_from_window:
            window_color = window
            wall_color = light_brown
            door_color = dark_grey
            color_sun = white
        else:
            window_color = light_window
            wall_color = light_light_brown
            door_color = grey
            color_sun = white

    #Draw grass
    pygame.draw.rect(screen, grass_color, [0, 500, 1000, 500])

    #draw sky
    draw_sky()

    for c in clouds:
        c[0] -= 0.5
        if c[0] < -100:
            c[0] = random.randrange(1000, 1100)
            c[1] = random.randrange(0, 500)

    if not day:
        for s in stars:
            pygame.draw.ellipse(screen, white, s)
        pygame.draw.ellipse(screen, sky_color, [725, 210, 80, 80])

    for c in clouds:
        draw_clouds(c[0], c[1])
    screen.blit(color_clouds, (0, 0))

    color_clouds.fill(ck)
    color_clouds.set_colorkey(ck)



    draw_house(200, 600, 300, 350)

    if not day and not light_from_window:
        screen.blit(darkness, (0, 0))

    screen.blit(press_n, [700, 800])
    screen.blit(press_d, [700, 850])
    screen.blit(press_w, [700, 900])

    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)


pygame.quit()

