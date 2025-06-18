def mostrar_menu_general():

        print("\nMenu:")
        print("1. Ver las playlists disponibles")

        # Cuando eliga la playilist de la lista le mostrara las canciones que tiene y el usuario podra elegir una 
        # cancion de la lista para reproducirla y le saldra mientras se reproduce la cancion el nombre del autor y el nombre de la cancion y las opciones 
        # para parar la cancion, cambiar de cancion, eliminar cancion de la playlist, agregar canciones a la playlist,
        # cambiar de playlist, alternar playlist aleatoria 
        # Hay que implementar recursion para que el usuario pueda volver al menu principal y elegir otra opcion
        

        # Resumen del reproductor de música:

        # Estructuras de datos: Diccionario para playlists donde clave=nombre playlist y valor=lista de canciones. Cada canción es una lista de dos elementos [autor, título]. Variables simples para flags de estado (reproduciendo True/False, playlist_actual, cancion_actual como índices).
        # Arquitectura de menús: Menú principal para navegación general, submenú específico durante reproducción. Usuario elige playlist → reproduce automáticamente primera canción → entra a submenú de reproducción. Sale del submenú solo cuando elige "volver", usando recursión para navegación entre menús.
        # Manejo de errores: Mensajes específicos incluidos en cada función. Cuando no hay más canciones o elementos inexistentes, para reproducción cambiando flag a False y mostrando mensaje correspondiente. Todas las opciones siempre visibles, pero con feedback claro cuando no aplican.
        # Simulación de reproducción: time.sleep() corto en bucle con verificación periódica de input usuario, descartando hilos por simplicidad. Función especializada que revisa estado del flag, llamada al inicio y final de operaciones críticas.
        
        #Input no-bloqueante: usar input() con timeout. Con 3 segundos sí se nota la "pausa",para hacer el enfoque de sleep corto + verificación funcionará bien.
        #Datos predefinidos: 
        #pythonplaylists = {
        #        "Rock": [["Metallica", "Enter Sandman"], ["AC/DC", "Thunderstruck"]],
        #        "Pop": [["Taylor Swift", "Shake It Off"]]
        #}
        # Validación en input:Try/except o verificar si es dígito.

        # 1. Estructuras de datos - Definir el diccionario de playlists con datos de prueba, variables para el estado actual (playlist_actual, cancion_actual, reproduciendo).
        # 2. Funciones básicas - Acceder a canción actual, cambiar canción, verificar si hay siguiente/anterior, la función que revisa estado y maneja flags.
        # 3. Funciones de manipulación - Agregar/eliminar canciones, cambiar playlist, modo aleatorio.
        # 4. Menús - Primero menú principal, después submenú de reproducción, por último la lógica de navegación/recursión.

        #1. Datos principales:
        #* Diccionario de playlists con canciones de ejemplo
        #* Variables de estado del reproductor
        #2. Estados del sistema:
        #* ¿Qué valores puede tener cada variable de estado? no se
        #* ¿Qué representa cada posible estado? las variables
        #3. Datos de configuración:
        # ¿Modo aleatorio on/off? modo aleatorio off
        # ¿Alguna configuración adicional? no
        #Pregunta de diseño: ¿Voy a tener variables globales o voy a pasar todo como parámetros entre funciones? parametros a funciones
        #Y otra: Ejemplo de variables de estado cuando arranca el sistema
        # playlist_actual = None (ninguna seleccionada)
         # cancion_actual = 0
         #reproduciendo = False

       
         #   playlist_actual puede ser: none (no hay playlist seleccionada),"Rock", "Pop", etc. (nombre de playlist activa)

         #cancion_actual:

         #0, 1, 2... (índice de la canción en la playlist)
         #-1 (si no hay canción válida)

         #reproduciendo puede ser:True (está sonando algo) False (parado/silencio)

         #modo_aleatorio puede ser:True (canciones en orden random) ,False (orden secuencial)

        # playlist_actual = None ✓ (ninguna seleccionada al inicio),  cancion_actual = -1 (no hay canción válida al inicio),reproduciendo = False ✓ (programa arranca en silencio),modo_aleatorio = False ✓ 

        # Resumen:Escribo las estructuras de datos,Empiezo con una función simple (ej: mostrar canción actual),y voy escribiendo las que necesitas otra función (ej: verificar si hay siguiente canción)

        # cancion_actual = 0 y después cancion_actual = -1. Decide cuál prefieres: 0 si quieres que apunte a la primera canción desde el inicio, -1 si quieres indicar "no hay canción válida"