from p5 import *
from classes.clases import *
from patron import *

class Ventana(Figura):
    def __init__(self):
        self.cuadrado_base = Cuadrado(
            borde_grosor=2,
            borde_color="#333333",
            width= 50,
            height= 60,
            x= 0,
            y= 0,
            vel_x= 0,
            vel_y= 0,
            relleno= "#544940AD"
        )

        self.ventana1 = Cuadrado(
            borde_grosor=2,
            borde_color="#555266",
            width= 15,
            height= 15,
            x= 5,
            y= 5,
            vel_x= 8,
            vel_y= 5,
            relleno= "#012335"
        )
        self.ventana2 = Cuadrado(
            borde_grosor=2,
            borde_color="#555266",
            width= 15,
            height= 15,
            x= 30,
            y= 5,
            vel_x= 8,
            vel_y= 5,
            relleno= "#012335"
        )
        self.ventana3 = Cuadrado(
            borde_grosor=2,
            borde_color="#555266",
            width= 15,
            height= 15,
            x= 5,
            y= 30,
            vel_x= 8,
            vel_y= 5,
            relleno= "#012335"
        )
        self.ventana4 = Cuadrado(
            borde_grosor=2,
            borde_color="#555266",
            width= 15,
            height= 15,
            x= 30,
            y= 30,
            vel_x= 8,
            vel_y= 5,
            relleno= "#012335"
        )

        self.base = Cuadrado(
            borde_grosor=2,
            borde_color="#555266",
            width= 50,
            height= 10,
            x= 0,
            y= 50,
            vel_x= 8,
            vel_y= 5,
            relleno= "#ECEFF1"
        )
        
        
    def dibujar(self):
        self.cuadrado_base.dibujar()
        self.ventana1.dibujar()
        self.ventana2.dibujar()
        self.ventana3.dibujar()
        self.ventana4.dibujar()
        self.base.dibujar()