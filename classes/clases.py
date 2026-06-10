# Clases 
from p5 import *

# Molde para el borde
class Borde: 
    def __init__(self, grosor, color):
        self.grosor = grosor
        self.color = color
    # Etiqueta para mostrar datos de Borde
    def __str__(self):
        return f"Grosor = {self.grosor}, Color = {self.color}"

# Molde para la dimension / tamaño de la figura
class Dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Etiqueta para mostrar datos de Dimension
    def __str__(self):
        return f"Ancho = {self.width}, Alto = {self.height}"
    
# Molde para la posicion del objeto dentro del lienzo
class Posicion:
    def __init__(self, coor_x, coor_y):
        self.coor_x = coor_x
        self.coor_y = coor_y

    # Etiqueta para mostrar las coordenadas inciales del objeto
    def __str__(self):
        return f"Coordenada X = {self.coor_x}, Coordenada Y = {self.coor_y}"

# Molde para la velocidad del objeto
class Velocidad:
    def __init__(self, vel_x, vel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
    # Etiqueta para mostrar la velocidad asignada
    def __str__(self):
        return f"Velocidad en X = {self.vel_x}, Velocidad en Y = {self.vel_y}"

# Molde para el tamaño de ventana
class Pantalla:
    def __init__(self, window_width:int = 600, window_height:int = 600):
        self.window_width = window_width
        self.window_height = window_height

    # Creamos la ventana
    def iniciar(self):
        size(self.window_width, self.window_height)
    
    def __str__(self):
        return f"Ancho de ventano = {self.window_width}, Alto de Ventana = {self.window_height}"
    
    
# Clase figura, engloba todos los parametros anteriores

class Figura: 
    def __init__(self,
                borde_grosor,
                borde_color,
                width,
                height,
                x,
                y,
                vel_x,
                vel_y,
                relleno, 
                borde:Borde=None
                ):

        # Esto utiliza los valores predeterminados en caso de no pasar nuevos parametros
        if borde is None:
            self.borde = Borde(borde_grosor, borde_color)
        else:
            self.borde = borde

        # Esto permite guardar los datos de las figuras dentro de los parametros adecuados
        self.dimension = Dimension(width, height)
        self.posicion = Posicion(x,y)
        self.color_relleno = relleno
        self.velocidad = Velocidad(vel_x, vel_y)

        # Etiqueta de los parametros
    def __str__ (self):
        return f"""
        Borde: {self.borde}
        Dimension: {self.dimension}
        Posicion: {self.posicion}
        Color relleno: {self.color_relleno}
        Velocidad: {self.velocidad}
        """
        
        # Esto utiliza los parametros dentro de figura para dibujar el objeto
    def dibujar(self):
        # Realiza el groseo del borde
        stroke_weight(self.borde.grosor)

        # Selecciona el color del borde
        stroke(self.borde.color)

        # Selecciona el color de relleno para la figura 
        fill(self.color_relleno)

        # Dibuja la figura dentro de las coordenadas y el tamaño presentado dentro de los parametros
        rect(self.posicion.coor_x, self.posicion.coor_y,
            self.dimension.width, self.dimension.height)

        # Movemos lo posicion del objeto y hacemos la colision con limites de la ventana
    def desplazar_rebotar(self, max_x: int = 600, max_y: int = 600):
        self.posicion.coor_x += self.velocidad.vel_x
        self.posicion.coor_y += self.velocidad.vel_y

        if self.posicion.coor_x <= 0 or self.posicion.coor_x + self.dimension.width >= max_x:
            self.velocidad.vel_x *= -1
        if self.posicion.coor_y <= 0 or self.posicion.coor_y + self.dimension.height >= max_y:
              self.velocidad.vel_y *= -1
        

class Cuadrado(Figura):
    ...

class Elipse(Figura):
    def dibujar(self):
        # Realiza el groseo del borde
        stroke_weight(self.borde.grosor)

        # Selecciona el color del borde
        stroke(self.borde.color)

        # Selecciona el color de relleno para la figura 
        fill(self.color_relleno)

        # Dibuja la figura dentro de las coordenadas y el tamaño presentado dentro de los parametros
        ellipse(self.posicion.coor_x, self.posicion.coor_y,
                self.dimension.width, self.dimension.height)