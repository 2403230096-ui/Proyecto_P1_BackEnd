from p5 import * 
from classes.clases import *
from patron.Builders import Builder


cuadrado = None
elipse = None
# Figuras
ventana = Ventana(window_width=800, window_height=800)
figuras = []

def setup():
    ventana.iniciar()
    global cuadrado
    global elipse

    cuadrado = Cuadrado(2, "#0045A0", 50, 50, 10, 0, 3, 2, "#862F2F")
    elipse = Elipse(2, "#7C3E3E", 50, 50, 100, 100, 3, 2, "#CE22D4")

    figuras.append(cuadrado)
    figuras.append(elipse)



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
    

