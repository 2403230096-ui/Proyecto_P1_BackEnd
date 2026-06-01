from p5 import * 
from classes.clases import *
from patron.Builders import Builder
import random


cuadrado = None
cuadrado2 = None
elipse = None
elipse2 = None
# Figuras
ventana = Ventana(window_width=800, window_height=800)
figuras = []

def colorAleatorio():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"#{r:02X}{g:02X}{b:02X}"

def setup():

    ventana.iniciar()
    global cuadrado
    global cuadrado2
    global elipse
    global elipse2


    cuadrado = Cuadrado(2, "#0045A0", 50, 50,
                        random.uniform(0, ventana.window_width  - 50),   # x aleatorio
                        random.uniform(0, ventana.window_height - 50),   # y aleatorio
                        3, 2,
                        colorAleatorio())                                 # color aleatorio
    
    cuadrado2 = Cuadrado(2, "#0045A0", 50, 50,
                        random.uniform(0, ventana.window_width  - 50),   # x aleatorio
                        random.uniform(0, ventana.window_height - 50),   # y aleatorio
                        3, 2,
                        colorAleatorio())   

    elipse = Elipse(2, "#7C3E3E", 50, 50,
                    random.uniform(0, ventana.window_width  - 50),       # x aleatorio
                    random.uniform(0, ventana.window_height - 50),       # y aleatorio
                    3, 2,
                    colorAleatorio())   
    
    elipse2 = Elipse(2, "#7C3E3E", 50, 50,
                    random.uniform(0, ventana.window_width  - 50),       # x aleatorio
                    random.uniform(0, ventana.window_height - 50),       # y aleatorio
                    5, 2,
                    colorAleatorio())  

    figuras.append(cuadrado)
    figuras.append(cuadrado2)
    figuras.append(elipse)
    figuras.append(elipse2)

def draw():
    background(220)

    for figura in figuras:
        interactuarOBJ(figura)

def interactuarOBJ(figura:Figura):
    figura.dibujar()
    figura.desplazar_rebotar(max_x=ventana.window_width, max_y=ventana.window_height)

def crearFigura(tipo:int, x:float, y:float):
    if tipo == 0:
        return Builder().configBorde(2,"#244056").configPosicion(x,y).configDimesion(50,50).configColor("#995874").configVelocidad(4,5).build()
    else:
        return Builder().configBorde(4, "#995874").configPosicion(x, y).configDimesion(50, 50).configColor("#350319").configVelocidad(2,6).esElipse().build()
    
run()
    

