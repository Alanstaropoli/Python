import hangman
import reverse
import tictactoe

def menu_principal():
    """Imprime el menu principal del multijuego en pantalla"""

    print("""Bienvenido a Multijuegos.
Seleccione el juego que desea ejecutar.
    1. Ahorcado.
    2. Tateti.
    3. Otello.
    4. Salir.""")

def main():
    while True:
        menu_principal()
        opcion = input()
        if opcion == '1':
            print('Ahorcado.')
            hangman.main()
        elif opcion == '2':
            print('Tateti.')
            reverse.main()
        elif opcion == '3':
            print('Otello.')
            tictactoe.main()
        elif opcion == '4':
            break
        print()
    print('El programa ha finalizado.')

if __name__ == "__main__":
    main()

