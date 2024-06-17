from view.estudiante import menu_estudiantes
from view.curso import menu_cursos

def menu():
    exit = False
    while not(exit):
        print()
        print("#" * 80)
        print("# Menu principal")
        print("#" * 80)
        print("1. Gestión de estudiantes")
        print("2. Gestión de cursos")
        print("0. Salir de la aplicación")

        option = int(input("Ingrese su opción: "))
        if option == 1:
            menu_estudiantes()
        elif option == 2:
            menu_cursos()
        elif option == 0:
            exit = True
        else:
            print("Opción no válida!\n Verifica la opción seleccionada.")