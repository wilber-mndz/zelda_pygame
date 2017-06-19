import pygame
import sys
from pygame.locals import *
import zelda

class nivel1(zelda.Zelda):

    def __init__(self):
        zelda.Zelda.__init__(self)

        # Este rectangulo es para la colicion con el suelo del nivel
        self.terrenos = []
        self.terrenos.append(pygame.Rect(0,530,1330,70))
        self.terrenos.append(pygame.Rect(1470,530,560,70))
        self.terrenos.append(pygame.Rect(2520,530,910,70))

        #Almacenara los rectangulos para colicion de las cajas

        # Aqui almacenaremos las coliciones de las cajas
        self.cajas = []
        self.cajas.append(pygame.Rect(490, 460, 70, 70))
        self.cajas.append(pygame.Rect(560, 460, 70, 70))
        self.cajas.append(pygame.Rect(630, 460, 70, 70))
        self.cajas.append(pygame.Rect(560, 390, 70, 70))
        self.cajas.append(pygame.Rect(1960, 460, 70, 70))
        self.cajas.append(pygame.Rect(2170, 390, 70, 70))
        self.cajas.append(pygame.Rect(2240, 390, 70, 70))
        self.cajas.append(pygame.Rect(2380, 390, 70, 70))
        self.cajas.append(pygame.Rect(2450, 390, 70, 70))

        self.espinas = []
        self.espinas.append(pygame.Rect(985, 499 ,57 ,33))
        self.espinas.append(pygame.Rect(1685, 499 ,57 ,33))

        # Importamos el archivo para nuestras monedas
        self.monedas_sheet = pygame.image.load("imagenes/coins.png")
        fondo_sprite = self.monedas_sheet.get_at((0,0))
        self.monedas_sheet.set_colorkey(fondo_sprite, RLEACCEL)

        # Sprites de las monedas
        self.j = 0
        self.monedas_n =  {}
        self.monedas_n[0] = (0,0, 16, 16)
        self.monedas_n[1] = (16,0, 16, 16)
        self.monedas_n[2] = (32,0, 16, 16)
        self.monedas_n[3] = (51,0, 16, 16)
        self.con_mon = 3

        # variables para mover las monedas por el mapa
        self.mX = 0
        self.mY = 0

        # Posicion de las monedas
        self.pos_monedas = {}
        self.pos_monedas[0] = (770,480)
        self.pos_monedas[1] = (870,480)
        self.pos_monedas[2] = (1265,480)
        self.pos_monedas[3] = (1350,420)
        self.pos_monedas[4] = (1405,420)
        self.pos_monedas[5] = (1500,480)
        self.pos_monedas[6] = (1780,480)
        self.pos_monedas[7] = (1870,480)

    def dibujar_elementos(self, superficie):
        for caja in self.cajas:
            pygame.draw.rect(superficie, (255,255,255), caja)

        for terreno in self.terrenos:
            pygame.draw.rect(superficie, (4, 242, 56), terreno)

        for espina in self.espinas:
            pygame.draw.rect(superficie, (244, 40, 40), espina)

    def mover_elementos(self, direccion):
        if direccion == "derecha":
            # Movemos las monedas
            self.mX -= self.zelda_v
            # Movemos las cajas
            for caja in self.cajas:
                caja.left -= self.zelda_v
            # Movemos el terreno
            for terreno in self.terrenos:
                terreno.left -= self.zelda_v
            # Movemos las espinas
            for espina in self.espinas:
                espina.left -= self.zelda_v

        if direccion == "izquierda":

            # Movemos las monedas
            self.mX += self.zelda_v

            for caja in self.cajas:
                caja.left += self.zelda_v
            for terreno in self.terrenos:
                terreno.left += self.zelda_v
            for espina in self.espinas:
                espina.left += self.zelda_v

    def detectar_colision(self):
        # Detectamos la colicion con el terreno
        contador = 0
        for espina in self.espinas:
            if self.zelda_rect.colliderect(espina):
                self.z_herida = True
                if self.zelda_rect.left < espina.left:
                    self.dir_der = True
                else:
                    self.dir_der = False

        for terreno in self.terrenos:

            if self.zelda_rect.colliderect(terreno):

                if self.zelda_rect.top + 56 < terreno.top:
                    self.zY = terreno.top - 98
                    contador +=1
            if contador > 0:
                self.en_suelo = True
            else:
                self.en_suelo = False

        for caja in self.cajas:
            sobre_caja = False
            if self.zelda_rect.colliderect(caja):

                # Detectamos colision en la parte de abajo
                if self.zelda_rect.top + 56 < caja.top:
                    self.zY = caja.top - 99
                    self.en_suelo = True
                    sobre_caja = True

                # Detectamos colision por el lado derecho de Zelda
                if self.zelda_rect.left < caja.left :
                    if self.teclado[K_RIGHT] and sobre_caja == False:
                        self.zX = self.zelda_rect.left
                        if self.teclado[K_RIGHT]:
                            self.col_derecha = True
                    else:
                        self.col_derecha = False


                # Detectamos colision por el lado izquierda de Zelda
                if self.zelda_rect.right > caja.right :
                    if self.teclado[K_LEFT] and sobre_caja == False:
                        self.zX = self.zelda_rect.left
                        self.col_izquierda = True
                        if self.teclado[K_LEFT]:
                            self.col_izquierda = True
                    else:
                        self.col_izquierda = False
            else:
                sobre_caja = False
                # self.col_derecha = False
                # self.col_izquierda = False


    def monedas (self,superficie, m_x_y):

        """Actualiza los sprite que generan el movimiento de zelda
        cuando camine hacia la derecha"""

        if self.con_mon == (len(self.pos_monedas) *10) * 1:
            self.j = 0
        if self.con_mon == (len(self.pos_monedas) *10) * 2:
            self.j = 1
        if self.con_mon == (len(self.pos_monedas) *10) * 3:
            self.j = 2
        if self.con_mon == (len(self.pos_monedas) *10) * 4:
            self.j = 3
            self.con_mon = 0

        self.con_mon += 1

        self.moneda = pygame.transform.scale2x(self.monedas_sheet.subsurface(self.monedas_n[self.j]))
        superficie.blit(self.moneda, (m_x_y[0] + self.mX ,m_x_y[1] + self.mY))

    def dibujar_monedas (self, superficie):
        for i in self.pos_monedas:
            self.monedas(superficie, self.pos_monedas[i])
