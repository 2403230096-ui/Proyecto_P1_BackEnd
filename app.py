from p5 import *
from classes.clases import *
from patron.Builders import Builder
from models.models import *

# Configuración de la ventana del lienzo
MAX_width = 600
Max_height = 600
ventana = None
def setup():

    size(MAX_width, Max_height)
    global ventana
    ventana = Ventana()


def draw():
    background(220)
    ventana.dibujar()



run()