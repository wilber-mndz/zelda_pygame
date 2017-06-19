import pygame
import sys
from pygame.locals import *
import zelda
import nivel_1

class main(zelda.Zelda, nivel_1.nivel1):

    def __init__(self):
        zelda.Zelda.__init__(self)
        nivel_1.nivel1.__init__(self)
        ancho = 1024
        alto = 600


        pygame.init()
        ventana = pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("Animando Sprites")

        nivel = pygame.image.load("imagenes/nivel.png")
        fondo = pygame.image.load("imagenes/fondo.jpg")


        # creamos nuestro objeto reloj que nos ayudara a controlar el numero de fps
        reloj = pygame.time.Clock()

        nX = 0
        fX = 0

        muertes = 0

        # Bucle principal del juego
        while True:
            # Establecemos cuantos fotogramas por segundo queremos mostrar
            time = reloj.tick(60)
            ventana.fill((44, 176, 194))


            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()


            ventana.blit(fondo, (fX,0))
            ventana.blit(nivel, (nX,-30))

            self.zelda(ventana, evento)
            self.detectar_colision()

            self.dibujar_monedas(ventana)
            # self.dibujar_elementos(ventana)

            if self.teclado[K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if self.zX >= self.zX_M and self.teclado[K_RIGHT] and self.col_derecha == False and self.z_herida == False:
                nX -= self.zelda_v
                fX -= 1
                self.mover_elementos("derecha")
            if self.zX <= self.zX_m and self.teclado[K_LEFT] and fX != 0 and self.col_izquierda == False and self.z_herida == False:
                nX += self.zelda_v
                fX += 1
                self.mover_elementos("izquierda")
            pygame.display.update()

            if self.zelda_estado == False:
                zelda.Zelda.__init__(self)
                nivel_1.nivel1.__init__(self)
                nX = 0
                fX = 0
                muertes += 1
                self.zelda_vidas -= muertes

main()
