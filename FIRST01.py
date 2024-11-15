print("Hola mundo")
#pgzero

import random

portada = Actor("portada_inicio")
boton_play = Actor("but_play", (275, 410))
bruja = Actor("bruja", (50, 410))
background = Actor("fondo_total")
pantalla_general = Actor("pantalla_general")
WIDTH = 900
HEIGHT = 506
TITLE = "Mundland" 
FPS = 30 

y1 = random.randint(0,900)
y2 = random.randint(0,900)
y3 = random.randint(0,900)

act1 =Actor("tomate2", (300,y1))
act2 =Actor("rastrillo2", (300,y2))
act3 = Actor("cebolla2", (300,y3))

enemies = []

mode = "menu"


enemigos_cantidad = 8
lista_enemigos = []
ogros = []
puntaje = 0




for i in range(enemigos_cantidad):
    x = random.randint(200,WIDTH-50)
    y = random.randint(300,HEIGHT-50) 
    
    lista_enemigos.append((x,y))

ogros = []

for i in range(5):  
    x = random.randint(300, 800)
    y = random.randint(390, 410)
    enemy1 = Actor("enemy1",(x, y))
    enemy1.speed = random.randint(0, 2)
    ogros.append(enemy1)



    
    


def fill():
    global enemies
        
    name = ["rastrillo2" , "tomate2" , "cebolla2"]
    
    for i in range(15):
        
        x = random.randint(0,900)
        y = random.randint(-600,-200)
        elegido = random.choice(name)
        
        verdura = Actor(elegido,(x,y))
        enemies.append(verdura)
    
    
  
        

fill()

def mover_verduras():
    for i in range(len(enemies)):
        if enemies[i].y < HEIGHT:
            enemies[i].y += 8

def draw():
    
    if mode == "menu":
        portada.draw()
        boton_play.draw()
    elif mode == "game":
        background.draw()
        screen.draw.text(str(puntaje) , pos = (20,20) , fontsize = 36)
        bruja.draw()
        
        for ogro in ogros:
            ogro.draw();
        
        for enemi in enemies:
            enemi.draw();
            
            
    elif mode == "end":
        pantalla_general.draw()
        screen.draw.text("END GAME", center = (WIDTH//2,HEIGHT//2) , fontsize = 36)
        
    elif mode == "win":
        pantalla_general.draw()
        screen.draw.text("WIN", center = (WIDTH//2,HEIGHT//2) , fontsize = 36)    
        
def on_mouse_down(button, pos):
    global mode
    if boton_play.collidepoint(pos):
        mode = "game"
        
        
def detector_colisiones():
    
    for i in range(len(enemies)):
        
            
        if enemies[i].colliderect(bruja):
            game_over = 1
        
def update(dt):

    detector_colisiones()
    mover_ogros()
    colisiones_vegetales()
    colisiones_ogros()
    mover_verduras()
        
def on_key_down(key):
    if keyboard.left or keyboard.a and bruja.x > 20:
        bruja.x = bruja.x - 50

    elif keyboard.right or keyboard.d and bruja.x < 580:
        bruja.x = bruja.x + 50

    elif keyboard.down or keyboard.s:
        bruja.y += 115
        
    elif keyboard.up or keyboard.s:
        bruja.y -= 50
        
        
def mover_ogros():
    
    for i in range(len(ogros)):
        
        if ogros[i].x < bruja.x and abs(bruja.x - ogros[i].x) < 90:
            ogros[i].x += 5
        
        elif ogros[i].x > bruja.x and abs(bruja.x - ogros[i].x) < 90:
            ogros[i].x -= 5
         


def colisiones_vegetales():
    global mode
    for i in range(len(enemies)):
        if bruja.colliderect(enemies[i]):
            mode = "end"
            
            
            
def colisiones_ogros():
    global puntaje
    global mode
    for i in range(len(ogros)):
        if bruja.colliderect(ogros[i]):
            puntaje = puntaje + 1
            ogros.pop(i) 
            break 
    if len(ogros) <= 0:
        mode = "win"
         
