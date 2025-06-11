import random

def obtener_palabra_aleatoria():
    palabras=["avion","gato","programacion","codigo"]
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)

def jugar_ahorcado():
        palabra_secreta=obtener_palabra_aleatoria()
        letras_adivinadas=[]
        intentos_restantes=5

        while intentos_restantes>0:
            mostrar_tablero(palabra_secreta, letras_adivinadas)
            letra=input("Introduce una letra: ").lower()

            if letra in letras_adivinadas:
                print("Ya has introducido esa letra. Prueba otra.")
                continue

            if letra in palabra_secreta:
                letras_adivinadas.append(letra)
                if set(letras_adivinadas)==set(palabra_secreta):
                    print("Felicidades, has acertado la palabra")
                    break
            else:
                    intentos_restantes-=1
                    print(f"Letra incorrecta. Te quedan {intentos_restantes}")
        if intentos_restantes==0:
                        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")
jugar_ahorcado()
