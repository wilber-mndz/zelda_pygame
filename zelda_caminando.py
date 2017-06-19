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

        # Cargamos la imagen de game_over
        self.game_over = pygame.image.load("imagenes/game_over.jpg")
        self.winner = pygame.image.load("imagenes/winner.png")


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
        activar_sonido = 0 # Variable que nos ayuda a activar el sonido de game over

        # Bucle principal del juego
        while True:
            # Establecemos cuantos fotogramas por segundo queremos mostrar
            time = reloj.tick(60)
            ventana.fill((44, 176, 194))


            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            """"Dibujamos elementos en pantalla"""
            # Dibujamos el fondo del nievel
            ventana.blit(fondo, (fX,0))
            # Dibujamos el nivel
            ventana.blit(nivel, (nX,-30))

            """Acciones y eventos del juego"""

            if self.zelda_game_over == False:
                # Activamos el control y estados de zelda
                self.zelda(ventana, evento)
                # Detectamos coliciones
                self.detectar_colision()
                # Dibujamos monedas
                self.dibujar_monedas(ventana)
                # Muestra los rectangulos de coliciones
                # self.dibujar_elementos(ventana)


            """Capturamos eventos de teclado"""
            # Pulsamos escape para salir
            if self.teclado[K_ESCAPE]:
                pygame.quit()
                sys.exit()

            """Movimiento de la camara"""
            if self.zX >= self.zX_M and self.teclado[K_RIGHT] and self.col_derecha == False and self.z_herida == False:
                nX -= self.zelda_v
                fX -= 1
                self.mover_elementos("derecha")
            if self.zX <= self.zX_m and self.teclado[K_LEFT] and fX != 0 and self.col_izquierda == False and self.z_herida == False:
                nX += self.zelda_v
                fX += 1
                self.mover_elementos("izquierda")

            """ Muertes, game over y victoria"""
            # Si zelda muere reinixiamos el nivel y descontamos una vida
            if self.zelda_estado == False:
                zelda.Zelda.__init__(self)
                nivel_1.nivel1.__init__(self)
                nX = 0
                fX = 0
                muertes += 1
                self.zelda_vidas -= muertes

            # Si pierde las 3 vidas activamos game over
            if self.zelda_vidas == 0:
                self.zelda_game_over = True

            # Mostrando game over

            if self.zelda_game_over == True:
                ventana.blit(self.game_over, (0,0))
                # Cargamos la fuente por defecto
                fuente = pygame.font.Font(None, 50)
                # Generamos nuestro texto
                texto = fuente.render("FIN DEL JUEGO", 0 ,(232, 77, 77))
                # Mostramos texto en pantalla
                ventana.blit(texto, (200,200))

                # Activamos el sonido una sola ves
                if activar_sonido == 0:
                    activar_sonido =1
                if activar_sonido == 1:
                    pygame.mixer.music.load("sound/lose_music_2.wav")
                    pygame.mixer.music.play()
                    activar_sonido = 2

            # Mostrmos pantalla de victoria
            if self.en_suelo == True and self.zelda_monedas == 50 and nX <= -4470:
                ventana.blit(self.winner, (0,0))
                # Cargamos la fuente por defecto
                fuente = pygame.font.Font(None, 50)
                # Generamos nuestro texto
                texto = fuente.render("HAS GANADO GRACIAS POR JUGAR", 0 , (115, 29, 200) )
                # Mostramos texto en pantalla
                ventana.blit(texto, (100,200))

                # Activamos el sonido una sola ves
                if activar_sonido == 0:
                    activar_sonido =1
                if activar_sonido == 1:
                    pygame.mixer.music.load("sound/winner.mp3")
                    pygame.mixer.music.play()
                    activar_sonido = 2


            pygame.display.update()
main()
