import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
import dumbmenu as dm
import time
import inputbox
import random

pygame.init();

FRAMELIMIT = 200;
CLOCK = pygame.time.Clock();

SURFWIDTH = 600;
SURFHEIGHT = 400;

DISPLAYSURFACE = pygame.display.set_mode((SURFWIDTH,SURFHEIGHT),0,32);
icon = pygame.image.load("icon.png");
pygame.display.set_caption('Foosball');
pygame.display.set_icon(icon);

pi = 3.14159265359;

BLACK = (0,0,0);
WHITE = (255,255,255);
DARKGREEN = (30,120,30);
GREY = (50,50,50);
BLUE = (40,40,250);
RED = (250,20,20);

TEAMRED1Y = 210;
TEAMRED2Y = 173;
TEAMRED3Y = 136;
TEAMRED4Y = 155;
ROW3VARIANT = 36;
ROW4VARIANT = 55;

TEAMBLUE1Y = 210;
TEAMBLUE2Y = 173;
TEAMBLUE3Y = 136;
TEAMBLUE4Y = 155;

ROW1XRED = 105;
ROW2XRED = 161;
ROW3XRED = 275;
ROW4XRED = 381;
ROW1XBLUE = 494;
ROW2XBLUE = 438;
ROW3XBLUE = 324;
ROW4XBLUE = 218;


godmode = False;

ball = pygame.Rect(295,210,7,7);
BALLX = ball.left;
BALLY = ball.top;

ballxvector = -1;
ballyvector = random.randrange(-1,1,1);

balizaleft = pygame.image.load("balizaleft.png");
balizaright = pygame.image.load("balizaright.png");

teamred1 = pygame.Rect(ROW1XRED-4,TEAMRED1Y,10,10);
teamred2a = pygame.Rect(ROW2XRED-4,TEAMRED2Y,10,10);
teamred2b = pygame.Rect(ROW2XRED-4,TEAMRED2Y + 73,10,10);
teamred3a = pygame.Rect(ROW3XRED-4,TEAMRED3Y,10,10);
teamred3b = pygame.Rect(ROW3XRED-4,TEAMRED3Y + ROW3VARIANT,10,10);
teamred3c = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 2*ROW3VARIANT,10,10);
teamred3d = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 3*ROW3VARIANT,10,10);
teamred3e = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 4*ROW3VARIANT,10,10);
teamred4a = pygame.Rect(ROW4XRED-4,TEAMRED4Y,10,10);
teamred4b = pygame.Rect(ROW4XRED-4,TEAMRED4Y + ROW4VARIANT,10,10);
teamred4c = pygame.Rect(ROW4XRED-4,TEAMRED4Y + 2*ROW4VARIANT,10,10);

teamblue1 = pygame.Rect(ROW1XBLUE-4,TEAMRED1Y,10,10);
teamblue2a = pygame.Rect(ROW2XBLUE-4,TEAMRED2Y,10,10);
teamblue2b = pygame.Rect(ROW2XBLUE-4,TEAMRED2Y + 73,10,10);
teamblue3a = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y,10,10);
teamblue3b = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + ROW3VARIANT,10,10);
teamblue3c = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 2*ROW3VARIANT,10,10);
teamblue3d = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 3*ROW3VARIANT,10,10);
teamblue3e = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 4*ROW3VARIANT,10,10);
teamblue4a = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y,10,10);
teamblue4b = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y + ROW4VARIANT,10,10);
teamblue4c = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y + 2*ROW4VARIANT,10,10);

selection1 = 0;
selection2 = 0;

gametime = time.time();

def variableassignment():
    
    global TEAMRED1Y;
    global TEAMRED2Y;
    global TEAMRED3Y;
    global TEAMRED4Y;
    global ROW3VARIANT;
    global ROW4VARIANT;
    global TEAMBLUE1Y;
    global TEAMBLUE2Y;
    global TEAMBLUE3Y;
    global TEAMBLUE4Y;
    global ROW1XRED;
    global ROW2XRED;
    global ROW3XRED;
    global ROW4XRED;
    global ROW1XBLUE;
    global ROW2XBLUE;
    global ROW3XBLUE;
    global ROW4XBLUE;
    global teamred1;
    global teamred2a;
    global teamred3a;
    global teamred3b;
    global teamred3c;
    global teamred3d;
    global teamred3e;
    global teamred4a;
    global teamred4b;
    global teamred4c;
    global teamblue1;
    global teamblue2a;
    global teamblue2b;
    global teamblue3a;
    global teamblue3b;
    global teamblue3c;
    global teamblue3d;
    global teamblue3e;
    global teamblue4a;
    global teamblue4b;
    global teamblue4c;
    global selection1;
    global selection2;
    global BALLX;
    global BALLY;
    global ball;
    global ballmovement;
    global goalscored;
    global ballxvector;
    global ballyvector;
    global balizaleft;
    global gametime;
    global redscore;
    global bluescore;    
    global godmode;
    
    
    TEAMRED1Y = 210;
    TEAMRED2Y = 173;
    TEAMRED3Y = 136;
    TEAMRED4Y = 155;
    ROW3VARIANT = 36;
    ROW4VARIANT = 55;

    TEAMBLUE1Y = 210;
    TEAMBLUE2Y = 173;
    TEAMBLUE3Y = 136;
    TEAMBLUE4Y = 155;
    
    ROW1XRED = 105;
    ROW2XRED = 161;
    ROW3XRED = 275;
    ROW4XRED = 381;
    ROW1XBLUE = 494;
    ROW2XBLUE = 438;
    ROW3XBLUE = 324;
    ROW4XBLUE = 218;
    godmode = False;

    teamred1 = pygame.Rect(ROW1XRED-4,TEAMRED1Y,10,10);
    teamred2a = pygame.Rect(ROW2XRED-4,TEAMRED2Y,10,10);
    teamred2b = pygame.Rect(ROW2XRED-4,TEAMRED2Y + 73,10,10);
    teamred3a = pygame.Rect(ROW3XRED-4,TEAMRED3Y,10,10);
    teamred3b = pygame.Rect(ROW3XRED-4,TEAMRED3Y + ROW3VARIANT,10,10);
    teamred3c = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 2*ROW3VARIANT,10,10);
    teamred3d = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 3*ROW3VARIANT,10,10);
    teamred3e = pygame.Rect(ROW3XRED-4,TEAMRED3Y + 4*ROW3VARIANT,10,10);
    teamred4a = pygame.Rect(ROW4XRED-4,TEAMRED4Y,10,10);
    teamred4b = pygame.Rect(ROW4XRED-4,TEAMRED4Y + ROW4VARIANT,10,10);
    teamred4c = pygame.Rect(ROW4XRED-4,TEAMRED4Y + 2*ROW4VARIANT,10,10);

    teamblue1 = pygame.Rect(ROW1XBLUE-4,TEAMRED1Y,10,10);
    teamblue2a = pygame.Rect(ROW2XBLUE-4,TEAMRED2Y,10,10);
    teamblue2b = pygame.Rect(ROW2XBLUE-4,TEAMRED2Y + 73,10,10);
    teamblue3a = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y,10,10);
    teamblue3b = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + ROW3VARIANT,10,10);
    teamblue3c = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 2*ROW3VARIANT,10,10);
    teamblue3d = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 3*ROW3VARIANT,10,10);
    teamblue3e = pygame.Rect(ROW3XBLUE-4,TEAMRED3Y + 4*ROW3VARIANT,10,10);
    teamblue4a = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y,10,10);
    teamblue4b = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y + ROW4VARIANT,10,10);
    teamblue4c = pygame.Rect(ROW4XBLUE-4,TEAMRED4Y + 2*ROW4VARIANT,10,10);

    selection1 = 0;
    selection2 = 0;
    

    
    ball = pygame.Rect(295,210,7,7);

    BALLX = ball.left;
    BALLY = ball.top;
    
    ballmovement = False;
    goalscored = False;
    
    ballxvector = 1;
    ballyvector = random.randint(-7,7);
    redscore = 0;
    bluescore = 0;
    gametime = time.time();

def render_game_text():
    lucida = pygame.font.SysFont("lucidasans",12,True);
    player1 = lucida.render("PLAYER 1",True,WHITE);
    DISPLAYSURFACE.blit(player1,(10,10));
    player2 = lucida.render("PLAYER 2",True,WHITE);
    DISPLAYSURFACE.blit(player2,(520,10));
    lucidabig = pygame.font.SysFont("lucidasans",16,True);
    score = lucidabig.render("SCORE",True,WHITE);
    DISPLAYSURFACE.blit(score,(270,5));
    pygame.draw.rect(DISPLAYSURFACE,WHITE,(274,30,50,20),2);
    pygame.draw.line(DISPLAYSURFACE,WHITE,(300,30),(300,50),2);
    score1 = lucidabig.render(str(redscore),True,WHITE);
    DISPLAYSURFACE.blit(score1,(280,30));
    score2 = lucidabig.render(str(bluescore),True,WHITE);
    DISPLAYSURFACE.blit(score2,(310,30));
    spacetrigger = lucidabig.render("PRESS SPACE TO START",True,WHITE);
    DISPLAYSURFACE.blit(spacetrigger,(200,360));

def draw_field():
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,(80,100,440,220));
    pygame.draw.lines(DISPLAYSURFACE,WHITE,False,((80,180),(100,180),(100,240),(80,240)),2);
    pygame.draw.lines(DISPLAYSURFACE,WHITE,False,((519,180),(499,180),(499,240),(519,240)),2);
    pygame.draw.lines(DISPLAYSURFACE,WHITE,False,((80,140),(133,140),(133,280),(80,280)),2);
    pygame.draw.lines(DISPLAYSURFACE,WHITE,False,((519,140),(466,140),(466,280),(519,280)),2);
    pygame.draw.line(DISPLAYSURFACE,WHITE,(299,100),(299,319),2);
    pygame.gfxdraw.filled_circle(DISPLAYSURFACE,300,210,4,WHITE);
    pygame.gfxdraw.circle(DISPLAYSURFACE, 300, 210, 35, WHITE);
    pygame.gfxdraw.circle(DISPLAYSURFACE, 300, 210, 34, WHITE);
    pygame.gfxdraw.circle(DISPLAYSURFACE, 300, 210, 36, WHITE);

    #desenhar o resto das linhas de campo
    
def save():
    highscore = int(time.time() - gametime);
    f = open("highscore.txt", "a+");
    index = 0;
    filelines = f.readlines();
    f.close();
    name = inputbox.ask(DISPLAYSURFACE, "Name:");
    linewrite = "%s - %s\n" % (int(highscore), name.upper());
    for line in filelines:
        score = int(filter(str.isdigit, line));
        if highscore < score:
            break;
        index = index + 1;
    filelines.insert(index, linewrite);
    f = open("highscore.txt", "w");
    for string in filelines:
        f.write("%s" % string);
    f.close();
    
def draw_bars():
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW1XRED,100),(ROW1XRED,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW2XRED,100),(ROW2XRED,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW4XBLUE,100),(ROW4XBLUE,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW3XRED,100),(ROW3XRED,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW3XBLUE,100),(ROW3XBLUE,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW4XRED,100),(ROW4XRED,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW2XBLUE,100),(ROW2XBLUE,319),3);
    pygame.draw.line(DISPLAYSURFACE,GREY,(ROW1XBLUE,100),(ROW1XBLUE,319),3);

def draw_triangle1():
    if selection1 == 0:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW1XRED,325,ROW1XRED+5,335,ROW1XRED-5,335,WHITE);
    if selection1 == 1:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW2XRED,325,ROW2XRED+5,335,ROW2XRED-5,335,WHITE);
    if selection1 == 2:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW3XRED,325,ROW3XRED+5,335,ROW3XRED-5,335,WHITE);
    if selection1 == 3:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW4XRED,325,ROW4XRED+5,335,ROW4XRED-5,335,WHITE);
    #teste para experimentar os triangulos bonitos; a escolha do triangulo parece funcionar bem, basta aplicar as barras que definirmos; teremos um triangulo inferior e outro superior; o inferior estara a esquerda e sera do player 1, o superior estara a direita e sera do player 2
    
def draw_triangle2():
    if selection2 == 0:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW4XBLUE,94,ROW4XBLUE+5,85,ROW4XBLUE-5,85,WHITE);
    if selection2 == 1:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW3XBLUE,94,ROW3XBLUE+5,85,ROW3XBLUE-5,85,WHITE);
    if selection2 == 2:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW2XBLUE,94,ROW2XBLUE+5,85,ROW2XBLUE-5,85,WHITE);
    if selection2 == 3:
        pygame.gfxdraw.filled_trigon(DISPLAYSURFACE,ROW1XBLUE,94,ROW1XBLUE+5,85,ROW1XBLUE-5,85,WHITE);

def erase_row3red():
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred3a);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred3b);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred3c);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred3d);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred3e);

def erase_row4red():
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred4a);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred4b);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred4c);

def update_row3red():
    teamred3a.top = TEAMRED3Y;
    teamred3b.top = TEAMRED3Y + ROW3VARIANT;
    teamred3c.top = TEAMRED3Y + 2*ROW3VARIANT;
    teamred3d.top = TEAMRED3Y + 3*ROW3VARIANT;
    teamred3e.top = TEAMRED3Y + 4*ROW3VARIANT;

def update_row4red():
    teamred4a.top = TEAMRED4Y;
    teamred4b.top = TEAMRED4Y + ROW4VARIANT;
    teamred4c.top = TEAMRED4Y + 2*ROW4VARIANT;
    
def draw_row3red():
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred3a);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred3b);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred3c);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred3d);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred3e);  

def draw_row4red():
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred4a);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred4b);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred4c);

def draw_row3blue():
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue3a);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue3b);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue3c);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue3d);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue3e);  

def draw_row4blue():
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue4a);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue4b);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue4c);

def erase_row3blue():
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue3a);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue3b);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue3c);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue3d);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue3e);

def erase_row4blue():
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue4a);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue4b);
    pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue4c);

def update_row3blue():
    teamblue3a.top = TEAMBLUE3Y;
    teamblue3b.top = TEAMBLUE3Y + ROW3VARIANT;
    teamblue3c.top = TEAMBLUE3Y + 2*ROW3VARIANT;
    teamblue3d.top = TEAMBLUE3Y + 3*ROW3VARIANT;
    teamblue3e.top = TEAMBLUE3Y + 4*ROW3VARIANT;

def update_row4blue():
    teamblue4a.top = TEAMBLUE4Y;
    teamblue4b.top = TEAMBLUE4Y + ROW4VARIANT;
    teamblue4c.top = TEAMBLUE4Y + 2*ROW4VARIANT;
    
def ball_collision_red(ycenter):
    global ballxvector;
    global ballyvector;
    ballxvector = 1;
    ballyvector = ycenter - ball.centery;

def ball_collision_blue(ycenter):
    global ballxvector;
    global ballyvector;
    ballxvector = -1;
    ballyvector = ycenter - ball.centery;
    
def check_collision_red():
    if teamred1.colliderect(ball):
        ball_collision_red(teamred1.centery);
    if teamred2a.colliderect(ball):
        ball_collision_red(teamred2a.centery);
    if teamred2b.colliderect(ball):
        ball_collision_red(teamred2b.centery);
    if teamred3a.colliderect(ball):
        ball_collision_red(teamred3a.centery);
    if teamred3b.colliderect(ball):
        ball_collision_red(teamred3b.centery);
    if teamred3c.colliderect(ball):
        ball_collision_red(teamred3c.centery);
    if teamred3c.colliderect(ball):
        ball_collision_red(teamred3c.centery);
    if teamred3d.colliderect(ball):
        ball_collision_red(teamred3d.centery);
    if teamred3e.colliderect(ball):
        ball_collision_red(teamred3e.centery);
    if teamred4a.colliderect(ball):
        ball_collision_red(teamred4a.centery);
    if teamred4b.colliderect(ball):
        ball_collision_red(teamred4b.centery);
    if teamred4c.colliderect(ball):
        ball_collision_red(teamred4c.centery);
    
def check_collision_blue():
    if teamblue1.colliderect(ball):
        ball_collision_blue(teamblue1.centery);
    if teamblue2a.colliderect(ball):
        ball_collision_blue(teamblue2a.centery);
    if teamblue2b.colliderect(ball):
        ball_collision_blue(teamblue2b.centery);
    if teamblue3a.colliderect(ball):
        ball_collision_blue(teamblue3a.centery);
    if teamblue3b.colliderect(ball):
        ball_collision_blue(teamblue3b.centery);
    if teamblue3c.colliderect(ball):
        ball_collision_blue(teamblue3c.centery);
    if teamblue3c.colliderect(ball):
        ball_collision_blue(teamblue3c.centery);
    if teamblue3d.colliderect(ball):
        ball_collision_blue(teamblue3d.centery);
    if teamblue3e.colliderect(ball):
        ball_collision_blue(teamblue3e.centery);
    if teamblue4a.colliderect(ball):
        ball_collision_blue(teamblue4a.centery);
    if teamblue4b.colliderect(ball):
        ball_collision_blue(teamblue4b.centery);
    if teamblue4c.colliderect(ball):
        ball_collision_blue(teamblue4c.centery);
        
def define_ball_vectors():
    ball.top = 210;
    BALLY = ball.top;
    ball.left = 295;
    BALLX = ball.left;
    ballxvector = 1;
    ballyvector = random.randint(-7,7);
    
    
def gameplay():
    global BALLX;
    global BALLY;
    global ballxvector;
    global ballyvector;
    global selection1;
    global selection2;
    global TEAMRED1Y;
    global TEAMRED2Y;
    global TEAMRED3Y;
    global TEAMRED4Y;
    global TEAMBLUE1Y;
    global TEAMBLUE2Y;
    global TEAMBLUE3Y;
    global TEAMBLUE4Y;
    global firstboot;
    global choice;
    global ballmovement;
    global redscore;
    global bluescore;
    global goalscored;
    global godmode;
    pygame.draw.rect(DISPLAYSURFACE,BLACK,(40,180,40,60));
    pygame.draw.rect(DISPLAYSURFACE,BLACK,(520,180,40,60));
    draw_field();
    draw_bars();
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred1);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred2a);
    pygame.draw.rect(DISPLAYSURFACE,RED,teamred2b);
    draw_row3red();
    draw_row4red();
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue1);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2a);
    pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2b);
    draw_row3blue();
    draw_row4blue();
    pygame.draw.rect(DISPLAYSURFACE,WHITE,ball);
    keys = pygame.key.get_pressed();
    if keys[K_w]:
        if selection1 == 0:
            if teamred1.top>180:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred1);
                TEAMRED1Y = TEAMRED1Y - 1;
                teamred1.top = TEAMRED1Y;
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred1);
        if selection1 == 1:
            if teamred2a.top>100:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred2a);
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred2b);
                TEAMRED2Y = TEAMRED2Y - 1;
                teamred2a.top = TEAMRED2Y;
                teamred2b.top = TEAMRED2Y+73;
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred2a);
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred2b);
        if selection1 == 2:
            if teamred3a.top>100:
                erase_row3red();
                TEAMRED3Y = TEAMRED3Y - 1;
                update_row3red();
                draw_row3red();
        if selection1 == 3:
            if teamred4a.top>100:
                erase_row4red();
                TEAMRED4Y = TEAMRED4Y - 1;
                update_row4red();
                draw_row4red();
    if keys[K_s]:
        if selection1 == 0:
            if teamred1.bottom<240:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred1);
                TEAMRED1Y = TEAMRED1Y + 1;
                teamred1.top = TEAMRED1Y;
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred1);
        if selection1 == 1:
            if teamred2b.bottom<320:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred2a);
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamred2b);
                TEAMRED2Y = TEAMRED2Y + 1;
                teamred2a.top = TEAMRED2Y;
                teamred2b.top = TEAMRED2Y+73;
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred2a);
                pygame.draw.rect(DISPLAYSURFACE,RED,teamred2b);
        if selection1 == 2:
            if teamred3e.bottom<320:
                erase_row3red();
                TEAMRED3Y = TEAMRED3Y + 1;
                update_row3red();
                draw_row3red();
        if selection1 == 3:
            if teamred4c.bottom<320:
                erase_row4red();
                TEAMRED4Y = TEAMRED4Y + 1;
                update_row4red();
                draw_row4red();
    if keys[K_UP]:
        if selection2 == 3:
            if teamblue1.top>180:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue1);
                TEAMBLUE1Y = TEAMBLUE1Y - 1;
                teamblue1.top = TEAMBLUE1Y;
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue1);
        if selection2 == 2:
            if teamblue2a.top>100:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue2a);
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue2b);
                TEAMBLUE2Y = TEAMBLUE2Y - 1;
                teamblue2a.top = TEAMBLUE2Y;
                teamblue2b.top = TEAMBLUE2Y+73;
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2a);
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2b);
        if selection2 == 1:
            if teamblue3a.top>100:
                erase_row3blue();
                TEAMBLUE3Y = TEAMBLUE3Y - 1;
                update_row3blue();
                draw_row3blue();
        if selection2 == 0:
            if teamblue4a.top>100:
                erase_row4blue();
                TEAMBLUE4Y = TEAMBLUE4Y - 1;
                update_row4blue();
                draw_row4blue();
    if keys[K_DOWN]:
        if selection2 == 3:
            if teamblue1.bottom<240:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue1);
                TEAMBLUE1Y = TEAMBLUE1Y + 1;
                teamblue1.top = TEAMBLUE1Y;
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue1);
        if selection2 == 2:
            if teamblue2b.bottom<320:
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue2a);
                pygame.draw.rect(DISPLAYSURFACE,DARKGREEN,teamblue2b);
                TEAMBLUE2Y = TEAMBLUE2Y + 1;
                teamblue2a.top = TEAMBLUE2Y;
                teamblue2b.top = TEAMBLUE2Y+73;
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2a);
                pygame.draw.rect(DISPLAYSURFACE,BLUE,teamblue2b);
        if selection2 == 1:
            if teamblue3e.bottom<320:
                erase_row3blue();
                TEAMBLUE3Y = TEAMBLUE3Y + 1;
                update_row3blue();
                draw_row3blue();
        if selection2 == 0:
            if teamblue4c.bottom<320:
                erase_row4blue();
                TEAMBLUE4Y = TEAMBLUE4Y + 1;
                update_row4blue();
                draw_row4blue();

    check_collision_blue();
    check_collision_red();
    if (ballmovement):
        if godmode == False:
            ball.left = ball.left + ballxvector;
            
            if (ball.left<81 and (ball.top<181 or ball.bottom>239)):
                ballxvector = 1;
            if (ball.right>519 and (ball.top<181 or ball.bottom>239)):
                ballxvector = -1;
            if (ball.top<101):
                ballyvector = ballyvector*(-1);
                ball.top = ball.top + 1;
            if (ball.bottom>319):
                ballyvector = ballyvector*(-1);
                ball.top = ball.top - 1;
            if (ballyvector<0):
                if(ballyvector>-9):
                    if(ball.centerx%(9-abs(ballyvector)) == 0):
                        BALLY = BALLY + 1;
                        ball.top = BALLY;
                else:
                    if(ball.centerx%1 == 0):
                        BALLY = BALLY + 1;
                        ball.top = BALLY;
            if (ballyvector>0):
                if(ballyvector<9):
                    if(ball.centerx%(9-abs(ballyvector)) == 0):
                        BALLY = BALLY - 1;
                        ball.top = BALLY;
                else:
                    if((ball.centerx%1) == 0):
                        BALLY = BALLY - 1;
                        ball.top = BALLY;
        if godmode == True:
            ball.left = ball.left + ballxvector;
            
            if (ball.left<81):
                ballxvector = 1;
            if (ball.right>519):
                ballxvector = -1;
            if (ball.top<101):
                ballyvector = ballyvector*(-1);
                ball.top = ball.top + 1;
            if (ball.bottom>319):
                ballyvector = ballyvector*(-1);
                ball.top = ball.top - 1;
            if (ballyvector<0):
                if(ballyvector>-9):
                    if(ball.centerx%(9-abs(ballyvector)) == 0):
                        BALLY = BALLY + 1;
                        ball.top = BALLY;
                else:
                    if(ball.centerx%1 == 0):
                        BALLY = BALLY + 1;
                        ball.top = BALLY;
            if (ballyvector>0):
                if(ballyvector<9):
                    if(ball.centerx%(9-abs(ballyvector)) == 0):
                        BALLY = BALLY - 1;
                        ball.top = BALLY;
                else:
                    if((ball.centerx%1) == 0):
                        BALLY = BALLY - 1;
                        ball.top = BALLY;
    balizared = DISPLAYSURFACE.blit(balizaleft,(40,180));
    balizablue = DISPLAYSURFACE.blit(balizaright,(520,180));
    if godmode == False:
        if balizared.contains(ball):
            if goalscored == False:
                lucidabig = pygame.font.SysFont("lucidasans",16,True);
                bluescore += 1;
                lucida = pygame.font.SysFont("lucidasans",24,True);
                player2scores = lucida.render("PLAYER 2 SCORES",True,WHITE);
                DISPLAYSURFACE.blit(player2scores,(200,51));
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(274,30,50,20));
                pygame.draw.rect(DISPLAYSURFACE,WHITE,(274,30,50,20),2);
                pygame.draw.line(DISPLAYSURFACE,WHITE,(300,30),(300,50),2);
                score1 = lucidabig.render(str(redscore),True,WHITE);
                DISPLAYSURFACE.blit(score1,(280,30));
                score2 = lucidabig.render(str(bluescore),True,WHITE);
                DISPLAYSURFACE.blit(score2,(310,30));
                goalscored = True;
                ballmovement = False;
                if bluescore<5:
                    spacetrigger = lucidabig.render("PRESS SPACE TO CONTINUE",True,WHITE);
                    DISPLAYSURFACE.blit(spacetrigger,(200,360));
        
        if balizablue.contains(ball):
            if goalscored == False:
                lucidabig = pygame.font.SysFont("lucidasans",16,True);
                redscore += 1;
                lucida = pygame.font.SysFont("lucidasans",24,True);
                player2scores = lucida.render("PLAYER 1 SCORES",True,WHITE);
                DISPLAYSURFACE.blit(player2scores,(200,51));
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(274,30,50,20));
                pygame.draw.rect(DISPLAYSURFACE,WHITE,(274,30,50,20),2);
                pygame.draw.line(DISPLAYSURFACE,WHITE,(300,30),(300,50),2);
                score1 = lucidabig.render(str(redscore),True,WHITE);
                DISPLAYSURFACE.blit(score1,(280,30));
                score2 = lucidabig.render(str(bluescore),True,WHITE);
                DISPLAYSURFACE.blit(score2,(310,30));
                goalscored = True;
                ballmovement = False;
                if redscore<5:
                    spacetrigger = lucidabig.render("PRESS SPACE TO CONTINUE",True,WHITE);
                    DISPLAYSURFACE.blit(spacetrigger,(200,360));

        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                if ballmovement == True:
                    if godmode == True:
                        godmode = False;
                        pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,340,440,60));                    
                    elif godmode == False:
                        godmode = True;
                        lucidabig = pygame.font.SysFont("lucidasans",16,True);
                        godmodetext = lucidabig.render("GOD MODE ENABLED",True,WHITE);
                        DISPLAYSURFACE.blit(godmodetext,(220,360));
        
            if event.key == pygame.K_ESCAPE:
                firstboot = True;
                choice = -1;
                save();
                DISPLAYSURFACE.fill(BLACK);
            if event.key == pygame.K_d:
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,320,440,20));
                if selection1<3:
                    selection1 += 1;
                draw_triangle1();
            if event.key == pygame.K_a:
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,320,440,20));
                if selection1>0:
                    selection1 += -1;
                draw_triangle1();
            if event.key == pygame.K_RIGHT:
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,80,440,19));
                if selection2<3:
                    selection2 += 1;
                draw_triangle2();
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,80,440,19));
                if selection2>0:
                    selection2 += -1;
                draw_triangle2();
            if event.key == pygame.K_SPACE:
                if ballmovement == False:
                    define_ball_vectors();
                    ballmovement = True;
                    goalscored = False;
                    pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,340,440,60));
                    pygame.draw.rect(DISPLAYSURFACE,BLACK,(80,51,440,29));
    pygame.display.update();
    CLOCK.tick(FRAMELIMIT);
    
def gameover(player):
    global choice;
    global firstboot;
    DISPLAYSURFACE.fill(BLACK);
    lucida = pygame.font.SysFont("lucidasans", 16, True);
    gameplayer = player + " wins!";
    gamewinner = lucida.render(gameplayer, True, WHITE);
    DISPLAYSURFACE.blit(gamewinner, (DISPLAYSURFACE.get_width() / 2, DISPLAYSURFACE.get_height() / 2));
    firstboot = True;
    choice = -1;
    save();
    DISPLAYSURFACE.fill(BLACK);

firstboot = True;
gamestart = True;
choice = -1;

while True:
    if firstboot == True:
        DISPLAYSURFACE.fill(BLACK);
        pygame.draw.line(DISPLAYSURFACE,GREY,(ROW1XBLUE,100),(ROW1XBLUE,319),3);
        choice = dm.dumbmenu(DISPLAYSURFACE, ['Start Game','Quit Game'],100,150,"lucidasans",42,0.7,WHITE, WHITE, True);
        firstboot = False;
        DISPLAYSURFACE.fill(BLACK);
        gamestart = True;
        variableassignment();
    if choice == 0:
        if gamestart == True:
            render_game_text();
            draw_field();
            draw_bars();
            draw_triangle1();
            draw_triangle2();
            gamestart = False;
        gameplay();
        if bluescore == 5:
            gameover("Blue");
            DISPLAYSURFACE.fill(BLACK);
        if redscore == 5:
            gameover("Red");
            DISPLAYSURFACE.fill(BLACK);
    if choice == 1:
        pygame.quit();
        sys.exit();
