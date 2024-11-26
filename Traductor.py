import json
diccionario = {
    "hola": "hello",
    "mundo": "world",
    "python": "python",
    "programa": "program",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "si": "if",
    "amor": "love",
    "jugar": "play",
    "ir": "go",
    "yo puedo": "i can"
    }

def guardar_diccionario(diccionario, archivo="diccionario.json"):
    with open(archivo, "w") as file:
        json.dump(diccionario, file, indent=4)
    print("Diccionario guardado con éxito.")

def cargar_diccionario(archivo="diccionario.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No se encontro un diccionario guardado.")
        return diccionario
    
def diccinario_traducciones():
    global diccionario
    diccionario = cargar_diccionario()

    while True:
        print("\n*** Menú del diccionario de traducciones ***")
        print("1. Buscar traduccion")
        print("2. Agregar nueva palabra")
        print("3. Eliminar una palabra")
        print("4. Mostrar todas las palabras")
        print("5. Guardar y salir")

        opcion = int(input("Eleige una opcion del 1 al 5: "))

        if opcion == 1:
            palabra = input("Escribe una palabra para traducir: ").lower()
            if palabra in diccionario:
                print(f"La traduccion de '{palabra}' es '{diccionario[palabra]}' ")
            elif palabra in diccionario.values():
                #busca la clave que coincida
                traduccion_inversa = [key for key, value in diccionario.items() if value == palabra]
                print(f"La traduccion de '{palabra}' es '{traduccion_inversa[0]}'")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario. Ingresa a la opcion 2 y agregala.")
        elif opcion == 2:
            palabra_es = input("Escribe la palabra en espeañol: ").lower()
            palabra_in = input("Escribe la traduccion en inglés: ").lower()
            if palabra_es in diccionario:
                print(f"La palabra '{palabra_es}' ya esta en el diccionario")
            else:
                diccionario[palabra_es] = palabra_in
                print(f"Se agrego la palabra '{palabra_es}' con la traduccion '{palabra_in}' al diccionario")
        elif opcion == 3:
            palabra = input("Escribe la palabra que deseas eliminar: ").lower()
            if palabra in diccionario: 
                del diccionario[palabra]
                print(f"La palabra '{palabra}' ha sido eliminada.")
            elif palabra in diccionario.values():
                clave_a_eliminar = [key for key, value in diccionario.items() if value == palabra][0]
                del diccionario[clave_a_eliminar]
                print(f"La traduccion '{palabra}' ha sido eliminada.")
            else: 
                print(f"La palabra '{palabra}' no está en el diccionario.")
        elif opcion == 4:
            print("\nPalabras en el diccionario:")
            for palabra_es, palabra_in in diccionario.items():
                print(f" {palabra_es} -> {palabra_in} ")
        elif opcion == 5:
            guardar_diccionario(diccionario)
            print("¡Hasta luego. Vuela pronto!")
            break
        else:
            print("Opción no válida. Por favor elige entre 1 y 5.")
            
diccinario_traducciones()