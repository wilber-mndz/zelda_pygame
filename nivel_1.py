import pygame
import sys
from pygame.locals import *
import zelda

class nivel1(zelda.Zelda):

    def __init__(self):
        zelda.Zelda.__init__(self)

        # Iniciamos el sonido de fondo
        pygame.mixer.init()
        pygame.mixer.music.load("sound/fondo.wav")
        pygame.mixer.music.play()

        # Este rectangulo es para la colicion con el suelo del nivel
        self.terrenos = []
        self.terrenos.append(pygame.Rect(0,530,1330,70))
        self.terrenos.append(pygame.Rect(1470,530,560,70))
        self.terrenos.append(pygame.Rect(2520,530,980,70))
        self.terrenos.append(pygame.Rect(2520,530,980,70))
        self.terrenos.append(pygame.Rect(3920,530,70,70))
        self.terrenos.append(pygame.Rect(4480,530,840,70))

        #Plataformas
        self.terrenos.append(pygame.Rect(210, 390, 210, 20))
        self.terrenos.append(pygame.Rect(420, 250, 210, 20))
        self.terrenos.append(pygame.Rect(770, 160, 140, 20))
        self.terrenos.append(pygame.Rect(1120, 160, 140, 20))
        self.terrenos.append(pygame.Rect(1540, 230, 350, 20))
        self.terrenos.append(pygame.Rect(1610, 390, 210, 20))
        self.terrenos.append(pygame.Rect(2100, 230, 490, 20))
        self.terrenos.append(pygame.Rect(3150, 320, 350, 20))
        self.terrenos.append(pygame.Rect(3570, 460, 350, 20))
        self.terrenos.append(pygame.Rect(2870, 90, 280, 20))
        self.terrenos.append(pygame.Rect(3500, 110, 420, 20))
        self.terrenos.append(pygame.Rect(4340, 320, 420, 20))
        self.terrenos.append(pygame.Rect(4830, 390, 210, 20))

        #Almacenara los rectangulos para colicion de las cajas

        # Aqui almacenaremos las coliciones de las cajas
        self.cajas = []
        self.cajas.append(pygame.Rect(490, 460, 70, 70))
        self.cajas.append(pygame.Rect(560, 460, 70, 70))
        self.cajas.append(pygame.Rect(630, 460, 70, 70))
        self.cajas.append(pygame.Rect(560, 390, 70, 70))
        self.cajas.append(pygame.Rect(1960, 460, 70, 70))
        self.cajas.append(pygame.Rect(2170, 390, 70, 70))
        # self.cajas.append(pygame.Rect(2240, 390, 70, 70))
        self.cajas.append(pygame.Rect(2380, 390, 70, 70))
        self.cajas.append(pygame.Rect(2450, 390, 70, 70))
        self.cajas.append(pygame.Rect(3150, 250, 70, 70))
        self.cajas.append(pygame.Rect(3150, 180, 70, 70))
        self.cajas.append(pygame.Rect(3850, 390, 70, 70))
        self.cajas.append(pygame.Rect(5250, 0, 70*5, 70*9))


        self.espinas = []
        self.espinas.append(pygame.Rect(985, 499 ,57 ,33))
        self.espinas.append(pygame.Rect(1685, 499 ,57 ,33))
        self.espinas.append(pygame.Rect(3230, 499 ,57 ,33))
        self.espinas.append(pygame.Rect(3430, 499 ,57 ,33))
        self.espinas.append(pygame.Rect(3655, 80 ,105 ,33))
        self.espinas.append(pygame.Rect(4330, 285 ,47 ,33))

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
        self.pos_monedas[8] = (2100,130)
        self.pos_monedas[9] = (2150,130)
        self.pos_monedas[10] = (2200,130)
        self.pos_monedas[11] = (2250,130)
        self.pos_monedas[12] = (2300,130)
        self.pos_monedas[13] = (2350,130)
        self.pos_monedas[14] = (2400,130)
        self.pos_monedas[15] = (2450,130)
        self.pos_monedas[16] = (2500,130)
        self.pos_monedas[17] = (2550,130)
        self.pos_monedas[18] = (1550,130)
        self.pos_monedas[19] = (1600,130)
        self.pos_monedas[20] = (1650,130)
        self.pos_monedas[21] = (1700,130)
        self.pos_monedas[22] = (1750,130)
        self.pos_monedas[23] = (1800,130)
        self.pos_monedas[24] = (1850,130)
        self.pos_monedas[25] = (2850,480)
        self.pos_monedas[26] = (2900,480)
        self.pos_monedas[27] = (2950,480)
        self.pos_monedas[28] = (3000,480)
        self.pos_monedas[29] = (3050,480)
        self.pos_monedas[30] = (2850,30)
        self.pos_monedas[31] = (2900,30)
        self.pos_monedas[32] = (2950,30)
        self.pos_monedas[33] = (3000,30)
        self.pos_monedas[34] = (3050,30)
        self.pos_monedas[35] = (3100,30)
        self.pos_monedas[36] = (3150,30)
        self.pos_monedas[37] = (3315,480)
        self.pos_monedas[38] = (3365,480)
        self.pos_monedas[39] = (3940,480)
        self.pos_monedas[40] = (4050, 2)
        self.pos_monedas[41] = (4150, 2)
        self.pos_monedas[42] = (4250, 50)
        self.pos_monedas[43] = (3650, 360)
        self.pos_monedas[44] = (3750, 360)
        self.pos_monedas[45] = (4500, 280)
        self.pos_monedas[46] = (4600, 280)
        self.pos_monedas[47] = (4500, 480)
        self.pos_monedas[48] = (820, 100)
        self.pos_monedas[49] = (1150, 100)


        # controlara la velocidad de animacion de las monedas


        self.estado_monedas = []
        self.monedas_rec = []

        for k in self.pos_monedas:
            self.estado_monedas.append(True)
            x = self.pos_monedas[k][0]
            y = self.pos_monedas[k][1]
            self.monedas_rec.append(pygame.Rect(x,y,32,32))

        self.v_m = len(self.monedas_rec)

    def dibujar_elementos(self, superficie):
        for caja in self.cajas:
            pygame.draw.rect(superficie, (255,255,255), caja)

        for terreno in self.terrenos:
            pygame.draw.rect(superficie, (4, 242, 56), terreno)

        for espina in self.espinas:
            pygame.draw.rect(superficie, (244, 40, 40), espina)

        for moneda in self.monedas_rec:
            pygame.draw.rect(superficie, (217, 227, 30), moneda)

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
            for moneda in self.monedas_rec:
                moneda.left -= self.zelda_v

        if direccion == "izquierda":

            # Movemos las monedas
            self.mX += self.zelda_v

            for caja in self.cajas:
                caja.left += self.zelda_v
            for terreno in self.terrenos:
                terreno.left += self.zelda_v
            for espina in self.espinas:
                espina.left += self.zelda_v
            for moneda in self.monedas_rec:
                moneda.left += self.zelda_v

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

        i = 0 # indice de la moneda
        for moneda in self.monedas_rec:
            if self.zelda_rect.colliderect(moneda) and self.estado_monedas[i] == True:
                self.estado_monedas[i] = False # Al colicionar la moneda se inactiva
                self.zelda_monedas +=1
                sonido = pygame.mixer.Sound("sound/Coin01.wav")
                sonido.play()
            i +=1


    def monedas (self,superficie, m_x_y, i):

        """Actualiza los sprite que generan el movimiento de zelda
        cuando camine hacia la derecha"""

        if self.con_mon == (self.v_m *10) * 1:
            self.j = 0
        if self.con_mon == (self.v_m *10) * 2:
            self.j = 1
        if self.con_mon == (self.v_m *10) * 3:
            self.j = 2
        if self.con_mon >= (self.v_m *10) * 4:
            self.j = 3
            self.con_mon = 0

        self.con_mon += 1

        if self.estado_monedas[i] == True: # Dibujamos la moneda solo si esta activa
            self.moneda = pygame.transform.scale2x(self.monedas_sheet.subsurface(self.monedas_n[self.j]))
            superficie.blit(self.moneda, (m_x_y[0] + self.mX ,m_x_y[1] + self.mY))

    def dibujar_monedas (self, superficie):
        for i in self.pos_monedas:
            self.monedas(superficie, self.pos_monedas[i], i)
                # self.con_mon = 0
