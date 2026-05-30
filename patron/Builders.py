# Builders
from classes.clases import *

# Construccion de objeto
class Builder: 


    def __init__(self):
        self._es_elipse = False

    # Configuracion de Borde
    def configBorde(self, borde_grosor:int, borde_color:int):
        self._borde_color = borde_color
        self._borde_grosor = borde_grosor
        return self
    
    # Configuracion de Color
    def configColor(self, color:str):
        self._color_relleno = color
        return self
    
    # Configuracion de Posicion
    def configPosicion(self, x:float, y:float):
        self._coor_x = x
        self._coor_y = y
        return self
    
    # Configuracion de Dimension
    def configDimesion(self, width:int = 50, height:int = 50):
        self._width = width
        self._height = height
        return self
    
    # Configuracion de Velocidad
    def configVelocidad(self, vel_x:float = 3, vel_y:float = 3):
        self._vel_x = vel_x
        self._vel_y = vel_y
        return self
    
    # Definimos el circulo
    def esElipse(self):
        self._es_elipse = True
        return self
    
    # Almacenamiento de elementos
    def build(self):
        variable = {
            'width':self._width,
            'height': self._height,
            'borde_grosor': self._borde_grosor,
            'borde_color':self._borde_color,
            'x': self._coor_x,
            'y': self._coor_y,
            'vel_x': self._vel_x,
            'vel_y': self._vel_y,
            'relleno':self._color_relleno            
        }

        # Definimos la seleccion entre cuadrado y circulo
        if self._es_elipse == False:
            return Cuadrado(**variable)
        else:
            return Elipse(**variable)