import pygame as pg

#configurar ancho y alto de la pantalla 
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

#cambiar titulo de la pantalla 
pg.display.set_caption("PongYera")
icono = pg.image.load("pong.png")
pg.display.set_icon(icono)


#variables de inicalizacion 
ejecutando = True
mi_reloj = pg.time.Clock()


#Paleta de colores 
BLANCO = (255,255,255)
ROJO = (215, 63, 42)
AZUL = (42, 113, 215)
COLOR_FONDO = (142, 187, 113)


#tamaño y coordenadas de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100

#COORDENADAS PELOTA 
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 13
ALTO_PELOTA = 13



#crear elementos del juego
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA , ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)






def dibujar_pantalla():
    pantalla.fill(COLOR_FONDO)
    pg.draw.rect(pantalla, ROJO, paleta_j1)
    pg.draw.rect(pantalla, AZUL, paleta_j2)
    pg.draw.ellipse(pantalla, BLANCO, pelota)




#Loop principal
while ejecutando:
    
    #verificar cierre del juego 
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutando = False
    #evento al presionar tecla
    teclas = pg.key.get_pressed()


    #actualizar posisicones de elementos 
    paleta_j1.y = j1_y
    paleta_j2.y = j2_y



    #redifinir coordenadas de las paletas
    if teclas[pg.K_w] and j1_y > 0:
        j1_y -= 5
    elif teclas [pg.K_s] and j1_y + ALTO_PALETA < ALTO_PANTALLA:
        j1_y += 5

    
    if teclas[pg.K_UP] and j2_y > 0:
        j2_y -= 5
    elif teclas [pg.K_DOWN] and j2_y + ALTO_PALETA < ALTO_PANTALLA:
        j2_y += 5




    dibujar_pantalla()


    pg.display.flip()
    mi_reloj.tick(60)









pg.quit()
quit()