import pygame
import sys
from pygame.locals import *

class Zelda():

    def __init__(self):

        """ Iniciamos todas nuestras variables y definimos nuestros sprite """

        # icono corazon
        self.corazon = pygame.image.load("imagenes/hud_heartFull.png")
        self.corazon_vacio = pygame.image.load("imagenes/hud_heartEmpty.png")
        # Creamos nuestro sprite de zelda
        self.zelda_sprite_map = pygame.image.load("imagenes/zelda.png")
        # Obtenemos el color del fondo de la imagen
        fondo_sprite = self.zelda_sprite_map.get_at((0,0))
        # Quitamos el fondo de la imagen
        self.zelda_sprite_map.set_colorkey(fondo_sprite, RLEACCEL)

        """
        El sprite de zelda esta compuesto por un rectangulos con 45px de ancho y 56px de alto
        las coordenas de cada sprite en la imagen que los contiene son las siguientes.
        De pie
        8,28
        Corriendo
        6,106 - 56,106 - 100,106 - 147,106 - 194,106 - 241,106
        """

        # Creamos una lista donde se almacenaran las ubicaciones de los sprite
        # Zelda de pie
        self.zelda_sprite_n = {}
        # self.zelda_sprite_n[0] = (301,268,44,50)
        self.zelda_sprite_n[0] = (14,26,24,50)
        # Zelda caminando
        self.zelda_sprite_n[1] = (6,106,45,50)
        self.zelda_sprite_n[2] = (56,106,45,50)
        self.zelda_sprite_n[3] = (100,106,45,50)
        self.zelda_sprite_n[4] = (147,106,45,50)
        self.zelda_sprite_n[5] = (194,106,45,50)
        self.zelda_sprite_n[6] = (241,106,45,50)
        # Zelda saltando
        self.zelda_sprite_n[7] = (12,199,28,44)
        self.zelda_sprite_n[8] = (44,185,23,56)
        self.zelda_sprite_n[9] = (72,183,34,44)
        self.zelda_sprite_n[10] = (112,182,39,52)
        self.zelda_sprite_n[11] = (155,199,33,44)
        # Zelda herida
        self.zelda_sprite_n[12] = (16,278,30,50)
        self.zelda_sprite_n[13] = (50,278,30,50)
        self.zelda_sprite_n[14] = (84,278,37,50)
        self.zelda_sprite_n[15] = (126,275,55,50)
        self.zelda_sprite_n[16] = (187,275,50,50)
        self.zelda_sprite_n[17] = (243,267,52,50)
        self.zelda_sprite_n[18] = (301,268,44,50)



        """ Variables para el movimiento del personaje"""
        # Contador que nos ayudara a movernos por los diferentes sprite
        self.contador = 7
        # controlara la velocidad con la que cambian los sprite
        self.v_s = 5
        self.i = 0 # indica el sprite inicial de zelda

        # Posicion de zelda en ejez X y Y
        self.zX = 50
        self.zY = 450
        self.zY_c = self.zY

        # Variables para el movimiento del nivel
        self.zX_M = 650  # Distancia maxima que alcanzara dentro de la pantalla
        self.zX_m = 200  # Distancia minima que alcanzara en el eje x

        # Direccion en la que zelda mira
        self.dir_der = True  # True indica que Zelda mira en la direccion derecha
        # Velocidad a la que camina zelda en pixeles
        self.zelda_v = 6

        # Variable que indica zelda esta saltando o esta en el suelo
        self.salto = False  # Indica que zelda esta saltando
        self.t_s = 0        # Indica en que etapa del salto se encuentra
        self.parabolico = False # Indica si esta en un salto parabolico o no
        self.bajano = False # Indica si esta bajando

        # Variables de colicion

        # Indica si zelda esta haciendo contacto con el suelo u otra superficie
        self.en_suelo = False
        # Indica si esta colicionando con algun objeto a la derecha o izquierda
        self.col_derecha = False
        self.col_izquierda = False

        """Variables de danio"""
        self.con_danio = 8
        self.z_herida = False

        """Variables de salud puntos y hub"""
        self.salud_zelda = 3

    def derecha(self, superficie):

        """Actualiza los sprite que generan el movimiento de zelda
        cuando camine hacia la derecha"""

        if self.contador == self.v_s * 1:
            self.i = 1
        if self.contador == self.v_s * 2:
            self.i = 2
        if self.contador == self.v_s * 3:
            self.i = 3
        if self.contador == self.v_s * 4:
            self.i = 4
        if self.contador == self.v_s * 5:
            self.i = 5
        if self.contador == self.v_s * 6:
            self.i = 6
            self.contador = 0

        self.contador += 1

        # Escalamos nuestro sprite a un tamanio 2 X ahora es 90x112px
        self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
        # Generamos nuestro rectangulo para la colicion
        self.colicion_zelda(self.zelda_sprite, superficie)
        # Dibujamos el sprite en pantalla
        superficie.blit(self.zelda_sprite, (self.zX, self.zY))

    def izquierda(self, superficie):

        """Actualiza los sprite que generan el movimiento de zelda cuando camine hacia la izquierda"""

        if self.contador == self.v_s * 1:
            self.i = 1
        if self.contador == self.v_s * 2:
            self.i = 2
        if self.contador == self.v_s * 3:
            self.i = 3
        if self.contador == self.v_s * 4:
            self.i = 4
        if self.contador == self.v_s * 5:
            self.i = 5
        if self.contador == self.v_s * 6:
            self.i = 6
            self.contador = 0

        self.contador += 1

        # Escalamos nuestro sprite a un tamanio 2 X ahora es 90x112px
        self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
        # Invertimos horizontalmente la imagen
        self.zelda_sprite_izq = pygame.transform.flip(self.zelda_sprite,True,False)
        # Generamos nuestro rectangulo para la colicion
        self.colicion_zelda(self.zelda_sprite_izq, superficie)
        # Dibujamos el sprite en pantalla
        superficie.blit(self.zelda_sprite_izq, (self.zX, self.zY))

    def arriba(self, superficie):

        """Actualiza los sprite que generan el movimiento de zelda cuando camine hacia la izquierda"""

        if self.contador == self.v_s * 1:
            self.i = 7
            self.zY += 12
        if self.contador == self.v_s * 2:
            self.i = 8
            self.zY -= 9
        if self.contador == self.v_s * 3:
            self.i = 9
            self.zY += 10
        if self.contador == self.v_s * 4:
            self.i = 10
        if self.contador == self.v_s * 5:
            self.i = 11
            self.zY += 10
        if self.contador == self.v_s * 6:
            self.i = 7
            self.zY += 12
            self.contador = 0

        self.contador += 1

        if self.dir_der == True:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
            obtener_rec = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            self.colicion_zelda(obtener_rec, superficie)
            superficie.blit(self.zelda_sprite, (self.zX, self.zY))
        else:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
            obtener_rec = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            self.zelda_sprite_izq = pygame.transform.flip(self.zelda_sprite,True,False)
            self.colicion_zelda(obtener_rec, superficie)
            superficie.blit(self.zelda_sprite_izq, (self.zX, self.zY))

    def normal(self, superficie):

        """ Dibujamos a zelda por defecto"""
        # Dibujamos a zelda cuando no se esta moviendo
        if self.dir_der == True and self.salto == False:
            # Escalamos nuestro sprite a un tamanio 2 X ahora es 90x112px
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            # Generamos nuestro rectangulo para la colicion
            self.colicion_zelda(self.zelda_sprite, superficie)
            superficie.blit(self.zelda_sprite, (self.zX, self.zY))

        elif self.dir_der == False and self.salto == False:
            # Escalamos nuestro sprite a un tamanio 2 X ahora es 90x112px
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            # Invertimos la direccion en que mira zelda
            self.zelda_sprite_izq = pygame.transform.flip(self.zelda_sprite,True,False)
            # Generamos nuestro rectangulo para la colicion
            self.colicion_zelda(self.zelda_sprite_izq, superficie)
            superficie.blit(self.zelda_sprite_izq, (self.zX, self.zY))

    def abajo(self, superficie):

        """ Dibujamos a zelda bajano"""
        if self.dir_der == True:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[9]))
            obtener_rec = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            self.colicion_zelda(obtener_rec, superficie)
            superficie.blit(self.zelda_sprite, (self.zX, self.zY))
        else:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[9]))
            obtener_rec = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[0]))
            self.zelda_sprite_izq = pygame.transform.flip(self.zelda_sprite,True,False)
            self.colicion_zelda(obtener_rec, superficie)
            superficie.blit(self.zelda_sprite_izq, (self.zX, self.zY))

    def herida(self, superficie):

        """Actualiza los sprite que generan el movimiento de zelda
        cuando camine hacia la derecha"""

        if self.con_danio == 8 * 1:
            self.i = 12
        if self.con_danio == 8 * 2:
            self.i = 13
        if self.con_danio == 8 * 3:
            self.i = 14
        if self.con_danio == 8 * 4:
            self.i = 15
        if self.con_danio == 8 * 5:
            self.i = 16
        if self.con_danio == 8 * 6:
            self.i = 17
        if self.con_danio == 8 * 7:
            self.i = 18
            self.con_danio = 0

        self.con_danio += 1

        if self.dir_der == True:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
            obtener_rec = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
            self.colicion_zelda(obtener_rec, superficie)
            superficie.blit(self.zelda_sprite, (self.zX, self.zY))
        else:
            self.zelda_sprite = pygame.transform.scale2x(self.zelda_sprite_map.subsurface(self.zelda_sprite_n[self.i]))
            self.zelda_sprite_izq = pygame.transform.flip(self.zelda_sprite,True,False)
            self.colicion_zelda(self.zelda_sprite_izq, superficie)
            superficie.blit(self.zelda_sprite_izq, (self.zX, self.zY))

    def teclado_zelda(self, superficie , evento):

        """  Estos son los eventos que se activan por teclado. """
        self.teclado = pygame.key.get_pressed() # Capturamos las teclas precionadas

        # Movimiento a la derecha
        if self.teclado[K_RIGHT]:
            if self.parabolico == False:
                self.derecha(superficie)
            elif self.salto == False:
                self.abajo(superficie)
            if self.zX < self.zX_M:
                self.zX+= self.zelda_v
            self.dir_der = True # Indica que Zelda va hacia la derecha

        # Movimiento a la izquierda
        elif self.teclado[K_LEFT]:
            if self.parabolico == False:
                self.izquierda(superficie)
            elif self.salto == False:
                self.abajo(superficie)
            if self.zX > self.zX_m:
                self.zX -= self.zelda_v
            self.dir_der = False # Indica que Zelda va hacia la izquierda

        # Salto
        elif self.teclado[K_UP] and (self.en_suelo == True or self.salto == True):
            if self.en_suelo == True:
                self.salto = True
            # Salto ascendente
            if self.salto == True:
                if self.t_s >= 0 and self.t_s <= 10:
                    self.zY -= 8
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 11 and self.t_s <= 20:
                    self.zY -=  6
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 21 and self.t_s <= 25:
                    self.zY -= 4
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s > 25:
                    self.salto = False
                    self.t_s = 0
            else:
                # Salto descendente
                if self.t_s >= 0 and self.t_s <= 10:
                    self.zY += 4
                    self.t_s+=1
                    self.abajo(superficie)
                if self.t_s >= 11 and self.t_s <= 20:
                    self.zY +=  6
                    self.t_s+=1
                    self.abajo(superficie)
                if self.t_s >= 21 and self.t_s <= 25:
                    self.zY += 8
                    self.t_s+=1
                    self.abajo(superficie)
                if self.t_s > 25:
                    self.salto = False
                    self.t_s = 0

        # Dibujamos a zelda por defecto
        elif self.en_suelo == True:

            self.normal(superficie)

        if self.teclado[K_b]:
            self.herida(superficie)
        """ Estos son los eventos que se activan al levantar una tecla"""
        if evento.type == KEYUP:

            if evento.key == K_UP:
                self.salto = False
                self.t_s = 0

            if evento.key == K_RIGHT:
                self.col_derecha = False

            if evento.key == K_LEFT:
                self.col_izquierda = False

        if self.en_suelo == True:
            self.parabolico = False


        """ Estas acciones se activan sin necesidad de precionar una tecla. """

        # Si no hace contacto con el suelo bajamos
        if self.en_suelo == False and self.salto == False:
            if not self.teclado[K_RIGHT] and not self.teclado[K_LEFT]:
                self.abajo(superficie)
            self.zY += 6

        """ Salto parabolico"""
        # Salto parabolico derecha ------>>>
        if self.teclado[K_RIGHT] and self.teclado[K_UP] and (self.en_suelo == True or self.salto==True):
            self.parabolico = True
            if self.en_suelo == True:
                self.salto = True

            if self.salto == True:
                if self.t_s >= 0 and self.t_s <= 10:
                    self.zY -= 8
                    self.zX += 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 11 and self.t_s <= 20:
                    self.zY -=  6
                    self.zX += 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 21 and self.t_s <= 25:
                    self.zY -= 4
                    self.zX += 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s > 25:
                    self.salto = False
                    self.t_s = 0

        # Salto parabolico izquiera  <<<------
        if self.teclado[K_LEFT] and self.teclado[K_UP] and (self.en_suelo == True or self.salto==True):

            self.parabolico = True

            if self.en_suelo == True:
                self.salto = True

            if self.salto == True:
                if self.t_s >= 0 and self.t_s <= 10:
                    self.zY -= 8
                    self.zX -= 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 11 and self.t_s <= 20:
                    self.zY -=  6
                    self.zX -= 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s >= 21 and self.t_s <= 25:
                    self.zY -= 4
                    self.zX -= 1
                    self.t_s+=1
                    self.arriba(superficie)
                if self.t_s > 25:
                    self.salto = False
                    self.t_s = 0

    def colicion_zelda(self, sprite, superficie):

        """ Obtenemos el rectangulo de zelda que se encargara de interceptar las coliciones """

        # Obtenemos el rectangulo del sprite que pasamos como parametro
        # Este rectangulo nos ayudara a detectar coliciones
        self.zelda_rect = sprite.get_rect()
        self.zelda_rect.left = self.zX
        self.zelda_rect.top = self.zY

        # pygame.draw.rect(superficie, (180, 115, 29), self.zelda_rect)

    # Funcion principal de zelda
    def zelda(self, superficie, evento):

        if self.z_herida == True:
            self.herida(superficie)
            if self.dir_der == True:
                self.zX -= 2
            elif self.dir_der == False:
                self.zX += 2
            if self.en_suelo == False:
                self.zY += 2
            # Salimos del estado de danio
            if self.con_danio == 7:
                self.salud_zelda -= 1
                self.z_herida = False


        if self.z_herida == False:
            self.teclado_zelda(superficie, evento)

        self.dibujar_hub(superficie)

    def dibujar_hub(self, superficie):
        corazonX = 25
        for i in range(0,self.salud_zelda):
            superficie.blit(self.corazon, (corazonX, 25))
            corazonX += 25

        for i in range(self.salud_zelda,3):
            superficie.blit(self.corazon_vacio, (corazonX, 25))
            corazonX += 25
