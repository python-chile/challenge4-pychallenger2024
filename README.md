Desafío 4: Práctica de downhill de Óscar
========================================
## Contexto:
Óscar es un gran ciclista que le gusta practicar descenso en cerros. Hoy ha elegido descender por el cerro Barón y ha programado un dron para que lo grabe. El dron debe ser capaz de estimar la velocidad para el seguimiento.

Se ha muestreado la pendiente "s" (positiva si es en subida y negativa si es en bajada) cada 10 metros. Se asume que Óscar no pedaleará y por tanto la pendiente determinará la aceleración. La magnitud de las pendientes es menor a 1. Óscar llega hasta el final o hasta que se detiene. Una pendiente 0.5 es equivalente a 45° en subida. 

$$a = -9 \cdot s$$ (9 es el producto de la gravedad 9.81 por el coeficiente de roce dinámico)

Considerando la velocidad inicial $v_0$ en cada tramo de 10 metros (la velocidad inicial en primer tramo es 0)

El tiempo en los 10 metros se determina por si hay pendiente:
$$t=\frac{\sqrt{v_0^2 + 20 \cdot a } - v_0}{a}$$

Y la velocidad final $v_1$ del segmento si hay pendiente:
$$v_1 = \sqrt{v_0^2 + 20 \cdot a}$$
Si no hay pendiente no hay aceleración y por tanto:
$$t=\frac{10}{v_0}$$
$$v_1=v_0$$

Si la velocidad llega a 0 con pendiente positiva Óscar se detendrá.
Considera que ciclista inicia a una altura de 300 metros.

Ayuda a Óscar a programar el programa del dron (en caso de que utilice bibliotecas externas debe agregarlas en requirements.txt)
(Todos los números despleagos se redondean a 2 decimales.)

## Parte 1: Estimar velocidad
Implementar función get_sections en utils.py que recibe como parámetro una lista de pendientes y retorna una lista de diccionarios, donde cada diccionario contiente las siguientes claves:

* acceleration: Aceleración del tramo
* time: Tiempo que toma a la bicicleta recorrer el tramo de 10 metros
* final_height: Altura al final del tramo.
* final_x: Desplazamiento horizontal al final del tramo respecto al punto de partida
* final_velocity: Rapidez al final del tramo

## Parte 2: Estimar tiempo en cada tramo:
Implementa función get_frames en utils.py que indicará los disintos momentos en que se encuentra bicileta para los instantes que van incremetándose de acuerdo a fps. Se recibe 2 parámetros

* sections: Es la lista que retorna función get_sections (ver parte anterior)
* fps: Frames por segundo (entero)

Y retorna diccionario con claves:

* duration: Duración total del viaje en segundo
* frames: Lista de diccionarios, donde cada diccionario tiene:
    * section: Número de tramo en que se encuentra ciclista
    * distance: Número de metros dentro del tramo para aquel instante

## Parte 3: Hacer animación
En función make_gif de utils.py genera una animación a 20Hz de dimensiones 500 x 500, donde cada frame tiene fondo cyan #00FFFF con una bicicleta y suelo. Bicicleta es formada así (considera puntos ya definidos en make_gif):

    * Rueda delantera como círculo negro #000000 grosor 2px radio 4 px, centro (250, 250)
    * Rueda trasera mismas características de rueda delantera cuyo centro dista 20px de rueda delantera (hacia izquierda) siguiendo pendiente de donde se ubica rueda delantera
    * Línea roja #FF0000 grosor 2px que inicia en centro rueda delantera y termina en manubrio (punto driver)
    * Línea roja #FF0000 grosor 2px que inicia en centro rueda trasera y termina en P1 (mitad de eje entre ruedas)
    * Línea roja #FF0000 grosor 2px entre P1 y asiento (punto seat)
    * Línea roja #FF0000 grosor 2px entre P1 y asiento (punto seat)
    * Línea roja #FF0000 grosor 2px entre P3 y P4
    * Línea roja #FF0000 grosor 2px entre P1 y P4
    * Línea roja #FF0000 grosor 2px entre rueda trasera y P3
    
Y el suelo se forma siguiendo las pendientes así:

    * Línea verde #0000FF grosor
    * Relleno café #808000 por debajo de línea verde

La orientación de bicicleta corresponderá a la pendiente que soporta en tal tramo y su punto de apoyo será la rueda delantera
La duración del gift es la que señala función get_frames
BONUS: ¿Y si Óscar pedalea cuando va lento y frena para mantener el control de la bicicleta? Establece un rango de velocidad mínima y máxima para estimar que tanto esfuerzo debe hacer Óscar para mantener ese rango de velocidad.
Corre los tests con:
python downhill.py
