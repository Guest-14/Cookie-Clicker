import pygame
import sys

pygame.init()

# -------- WINDOW --------

WIDTH, HEIGHT = 1100, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker Ultimate")

font = pygame.font.SysFont("arial", 24)
big = pygame.font.SysFont("arial", 48)

# -------- GAME DATA --------

cookies = 0

buildings = [

{"name":"Auto Clicker","count":0,"cps":1,"cost":50,"rect":None},

{"name":"Grandma","count":0,"cps":5,"cost":200,"rect":None},

{"name":"Farm","count":0,"cps":20,"cost":1000,"rect":None},

{"name":"Mine","count":0,"cps":50,"cost":3000,"rect":None},

{"name":"Factory","count":0,"cps":120,"cost":8000,"rect":None},

{"name":"Bank","count":0,"cps":300,"cost":20000,"rect":None},

{"name":"Laboratory","count":0,"cps":800,"cost":50000,"rect":None},

{"name":"Portal","count":0,"cps":2000,"cost":120000,"rect":None},

{"name":"Time Machine","count":0,"cps":5000,"cost":300000,"rect":None},

{"name":"Mega Factory","count":0,"cps":12000,"cost":800000,"rect":None}

]

# -------- COOKIE --------

cookie_rect = pygame.Rect(100,180,250,250)

# -------- TIMER --------

ADD = pygame.USEREVENT
pygame.time.set_timer(ADD,1000)

# -------- FUNCTIONS --------

def total_cps():

    total = 0

    for b in buildings:

        total += b["count"] * b["cps"]

    return total


def draw_cookie():

    pygame.draw.circle(screen,(181,101,29),(225,305),125)

    chips = [(180,250),(260,230),(290,330),(200,360),(240,300)]

    for c in chips:

        pygame.draw.circle(screen,(60,30,10),c,10)


def draw_shop():

    y = 100

    for b in buildings:

        rect = pygame.Rect(420,y,600,45)

        b["rect"] = rect

        pygame.draw.rect(screen,(50,50,50),rect)

        text = f"{b['name']}   Owned:{b['count']}   Cost:{b['cost']}   CPS:{b['cps']}"

        screen.blit(font.render(text,True,(0,255,0)),(430,y+10))

        y += 55


def draw():

    screen.fill((30,30,30))

    draw_cookie()

    draw_shop()

    screen.blit(big.render("COOKIE",True,(255,255,255)),(110,90))

    screen.blit(font.render(f"Cookies: {int(cookies)}",True,(255,255,255)),(20,20))

    screen.blit(font.render(f"Per Second: {total_cps()}",True,(255,255,0)),(20,60))

    pygame.display.update()

# -------- GAME LOOP --------

while True:

    draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:

            # click cookie
            if cookie_rect.collidepoint(event.pos):

                cookies += 1


            # click buildings
            for b in buildings:

                if b["rect"].collidepoint(event.pos):

                    if cookies >= b["cost"]:

                        cookies -= b["cost"]

                        b["count"] += 1

                        b["cost"] = int(b["cost"] * 1.5)


        if event.type == ADD:

            cookies += total_cps()