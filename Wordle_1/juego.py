import random

class Wordle:
    def seleccionar_palabra(self) -> str:
        with open("lista_palabras.txt", "r") as archivo:
            lineas = archivo.readlines()
            lista = [linea.strip() for linea in lineas]
        num_pal = random.randint(0, len(lista) - 1)
        pal = lista[num_pal]
        return pal

class Color:
    def __init__(self):
        self.GRIS = "\033[90m"
        self.VERDE = "\033[92m"
        self.AMARILLO = "\033[93m"
        self.RESET = "\033[0m"

class Tablero:
    def __init__(self):
        self.num_intentos: int = 0
        self.matriz = []
        self.llenar_matriz()

    def llenar_matriz(self):
        for i in range(6):
            self.matriz.append(["_" for _ in range(5)])

    def imprimir_tablero(self):
        for fila in self.matriz:
            print(" ".join(fila))
        print(f"Intento {self.num_intentos + 1}/6")

    def ingresar_palabra(self):
        if self.num_intentos < 6:
            print("Ingresa una palabra de 5 letras en minúsculas:")
            palabra = input()
            if len(palabra) == 5 and palabra.isalpha() and palabra.islower():
                for i, letra in enumerate(palabra):
                    self.matriz[self.num_intentos][i] = letra
                self.num_intentos += 1
            else:
                print("Por favor, ingresa una palabra válida de 5 letras en minúsculas.")
        else:
            print("Ya has alcanzado el límite de intentos.")

    def colorear_matriz(self, palabra_correcta):
        for j in range(5):
            letra = self.matriz[self.num_intentos - 1][j]
            if letra == palabra_correcta[j]:
                self.matriz[self.num_intentos - 1][j] = f"{Color().VERDE}{letra}{Color().RESET}"
            elif letra in palabra_correcta:
                self.matriz[self.num_intentos - 1][j] = f"{Color().AMARILLO}{letra}{Color().RESET}"
            else:
                self.matriz[self.num_intentos - 1][j] = f"{Color().GRIS}{letra}{Color().RESET}"

# Función principal del juego
def jugar_wordle():
    wordle = Wordle()
    tablero = Tablero()
    palabra_correcta = wordle.seleccionar_palabra()
    while tablero.num_intentos < 6:
        tablero.imprimir_tablero()
        tablero.ingresar_palabra()
        tablero.colorear_matriz(palabra_correcta)
        if "".join(tablero.matriz[tablero.num_intentos - 1]) == palabra_correcta:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        tablero.imprimir_tablero()
        print(f"¡Agotaste tus intentos! La palabra correcta era: {palabra_correcta}")

if __name__ == "__main__":
    jugar_wordle()
