# Un menu de un reproductor de musica

# 12 opciones: reproducir cancion, parar cancion, alternar playilist aleatoria, eliminar cancion de la playilist,
# agregar canciones a la playlist ,cambiar de playilist, cambiar de cancion, ver las playilist, salir

# El objeto que se va cambiando entre las funciones esta formada por nombre del autor de la cancion y nombre de la cancion


# Listas para canciones dentro de playlist -1 playilist x canciones
# Variables simples para canciones individuales - Bien pensado para el estado actual



import menu

def main():

    print("Bienvenido al reproductor de música")
    menu.mostrar_menu()


if __name__ == "__main__":
    main()