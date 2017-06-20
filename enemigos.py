import pygame
import zelda

class enemigos(zelda.Zelda):

    def __init__(self):
        zelda.Zelda.__init__(self)

        self.roca = []

        self.roca.append(pygame.image.load("imagenes/blockerMad.png"))
        self.roca.append(pygame.image.load("imagenes/blockerSad.png"))

        # Lista de enemigos
        self.roca_pos = {}
        self.roca_pos[0] = (820,-50)
        self.roca_pos[1] = (1700, 25)
        self.roca_pos[2] = (2800, 330)
        self.roca_pos[3] = (3870, 185)
        self.roca_pos[4] = (3350, 115)
        self.roca_pos[5] = (4550, 328)
        self.roca_pos[6] = (4650, 328)

        self.rocas_rec = []

        for k in self.roca_pos:
            x = self.roca_pos[k][0]
            y = self.roca_pos[k][1]
            self.rocas_rec.append(pygame.Rect(x,y,40,40))

        self.posY = 0
        self.v_r = 0
        self.roca_subiendo = False

    def comportamiento_enemigo(self, superficie, x):

        # # Posiciond del enemigo en Y
        if self.posY <= 150 and self.roca_subiendo == False:
            if self.v_r == 1:
                self.posY += 5
                self.v_r = 0
        if self.posY > 150:
            self.roca_subiendo = True

        if self.roca_subiendo == True:
            if self.v_r == 2:
                self.posY -= 1
                self.v_r = 0
                self.roca_subiendo = True
                if self.posY == 0:
                    self.roca_subiendo = False


        self.v_r += 1

        # Dibujamos el sprite del enemigo
        for i in self.roca_pos:
            if self.roca_subiendo == True:
                superficie.blit(self.roca[1], (self.roca_pos[i][0] + x ,self.roca_pos[i][1] + self.posY))
                self.rocas_rec[i].left = self.roca_pos[i][0] + x + 5
                self.rocas_rec[i].top = self.roca_pos[i][1] + self.posY + 5
            else:
                superficie.blit(self.roca[0], (self.roca_pos[i][0] + x ,self.roca_pos[i][1] + self.posY))
                self.rocas_rec[i].left = self.roca_pos[i][0] + x + 5
                self.rocas_rec[i].top = self.roca_pos[i][1] + self.posY + 5

            # Dibujamos el rectangulo del enemigo
            # pygame.draw.rect(superficie, (237, 137, 49), self.rocas_rec[i] )

        # Detectamos la colicion con el enmeigo
        for roca in self.rocas_rec:
            if self.zelda_rect.colliderect(roca):
                self.z_herida = True
                if self.zelda_rect.left < roca.left:
                    self.dir_der = True
                else:
                    self.dir_der = False
