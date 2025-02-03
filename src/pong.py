import pygame as pg # type: ignore

#configurar ancho y alto de la pantalla 
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

#cambiar titulo de la pantalla 
pg.display.set_caption("PongYera")



#variables de inicalizacion 
ejecutando = True
mi_reloj = pg.time.Clock()


#Paleta de colores 
BLANCO = (255,255,255)
ROJO = (255, 0, 0)
AZUL = ( 0, 0, 255 )
COLOR_FONDO = (6,6,6)


#definir sonidos 
pg.mixer.init()
sonido_golpe_paleta = pg.mixer.Sound("golpe_paleta.mp3")
sonido_golpe_pared = pg.mixer.Sound("golpe_pared.mp3")
sonido_punto = pg.mixer.Sound('punto.mp3')
sonido_golpe_paleta.set_volume(.5)
sonido_golpe_pared.set_volume(.5)
sonido_punto.set_volume(.5)


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
pelota_diferencia_x = 3
pelota_diferencia_y = 3

#puntaje inicial 
puntos_j1 = 0
puntos_j2 = 0

#definir las fuentes 
pg.font.init()
calibri_bold_35 = pg.font.SysFont("calibri Bold", 35)



#crear elementos del juego
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA , ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)






def dibujar_pantalla():
    pantalla.fill(COLOR_FONDO)
    pg.draw.rect(pantalla, ROJO, paleta_j1)
    pg.draw.rect(pantalla, AZUL, paleta_j2)
    pg.draw.rect(pantalla, BLANCO, pelota)
    texto_puntos_j1 = calibri_bold_35.render('PUNTOS J1: ' + str(puntos_j1), True , ROJO)
    texto_puntos_j2 = calibri_bold_35.render('PUNTOS J2: ' + str(puntos_j2), True , AZUL)
    pantalla.blit(texto_puntos_j1, (130, 20))
    pantalla.blit(texto_puntos_j2, (620, 20))



def resetear_pelotas_y_pelotas():
    global pelota_x, pelota_y, pelota_diferencia_x, pelota_diferencia_y, j1_y, j2_y
    pelota_x = 450
    pelota_y = 300
    pelota_diferencia_x = 3
    pelota_diferencia_y = 3
    j1_y = 250
    j2_y = 250




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
    pelota.x = pelota_x
    pelota.y = pelota_y



    #redifinir coordenadas de las paletas
    if teclas[pg.K_w] and j1_y > 0:
        j1_y -= 5
    elif teclas [pg.K_s] and j1_y + ALTO_PALETA < ALTO_PANTALLA:
        j1_y += 5

    
    if teclas[pg.K_UP] and j2_y > 0:
        j2_y -= 5
    elif teclas [pg.K_DOWN] and j2_y + ALTO_PALETA < ALTO_PANTALLA:
        j2_y += 5

    #redifinir las coordenadas de la pelota 
    pelota_x += pelota_diferencia_x
    pelota_y += pelota_diferencia_y

    #verificar colisiones en cada movimiento de la pelota
    if pelota.colliderect(paleta_j1):
        sonido_golpe_paleta.play()
        pelota_diferencia_x = abs(pelota_diferencia_x)
    elif pelota.colliderect(paleta_j2):
        sonido_golpe_paleta.play()
        pelota_diferencia_x = abs(pelota_diferencia_x)*-1
    elif pelota_y <= 0:
        sonido_golpe_pared.play()
        pelota_diferencia_y = abs(pelota_diferencia_y)
    elif pelota_y >= ALTO_PANTALLA:
        sonido_golpe_pared.play()
        pelota_diferencia_y = abs(pelota_diferencia_y)*-1
    elif pelota_x <= 0 or pelota_x >= ANCHO_PANTALLA:
        sonido_punto.play()
        if pelota_x >= ANCHO_PANTALLA:
            puntos_j1 += 1
        elif pelota_x <= 0:
            puntos_j2 += 1
        resetear_pelotas_y_pelotas()



    dibujar_pantalla()


    pg.display.flip()
    mi_reloj.tick(60)









pg.quit()
quit()