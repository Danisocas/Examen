from logica.logica import gestorPartida

def main():
    juego = gestorPartida()

    juego.anadir_jugador("Nacho", "lobo")
    juego.anadir_jugador("Elena", "vidente")
    juego.anadir_jugador("Carlos", "aldeano")

   
    print(juego.jugadores[0].accion_nocturna(juego.jugadores[2]))

    
    print(juego.votacion_dia("Carlos"))

    
    print(juego.comprobar_victoria())


if __name__ == "__main__":
    main()