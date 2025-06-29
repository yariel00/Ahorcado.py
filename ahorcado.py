import random

def obtener_palabra_aleatoria():
    palabras = [
        "avion", "gato", "programacion", "codigo",
        "banana", "robotica", "universo", "ecuador",
        "inteligencia", "yuca"
    ]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

# Dibujo del ahorcado

def mostrar_dibujo(intentos):
    dibujos = [
        """
          -----
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]
    print(dibujos[5 - intentos])

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("\nPalabra: ", tablero.strip())

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 5
    puntaje = 0

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")
    print(f"Tienes {intentos_restantes} intentos.\n")

    while intentos_restantes > 0:
        mostrar_dibujo(intentos_restantes)
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Introduce una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa solo UNA letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Prueba otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Correcto!")
            puntaje += 10
        else:
            intentos_restantes -= 1
            puntaje -= 5
            print("Incorrecto. Te quedan", intentos_restantes, "intentos.")

        palabra_actual = "".join([l if l in letras_adivinadas else "_" for l in palabra_secreta])
        if palabra_actual == palabra_secreta:
            print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            mostrar_tablero(palabra_secreta, letras_adivinadas)
            break

    if intentos_restantes == 0:
        print("\nSe acabaron los intentos. La palabra era:", palabra_secreta)

    print("Tu puntaje final fue:", max(puntaje, 0))

# Ejecutar el juego
jugar_ahorcado()

