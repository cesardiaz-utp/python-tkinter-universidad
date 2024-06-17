
from controller.curso import CursoController


def menu_cursos():
    exit = False

    while not(exit):
        print()
        print("#" * 80)
        print("# Gestion de Cursos")
        print("#" * 80)
        print("1. Listar todos los cursos")
        print("2. Consultar un curso")
        print("3. Agregar un curso")
        print("4. Modificar un curso")
        print("5. Eliminar un curso")
        print("0. Volver al menu principal")

        option = int(input("Ingrese su opción: "))
        if option == 1:
            listar()
        elif option == 2:
            consultar()
        elif option == 3:
            agregar()
        elif option == 4:
            modificar()
        elif option == 5:
            eliminar()
        elif option == 0:
            exit = True
        else:
            print("Opción no válida!\n Verifica la opción seleccionada.")

def listar():
    cursos = CursoController.get_all()
    print()
    print(" ID | Nombre | Creditos")
    for curso in cursos:
        print(f" {curso.id} | {curso.nombre} | {curso.creditos}")
    input("Presione <Enter> para continuar.")

def consultar():
    print()
    id = int(input("Ingrese el id del curso a consultar: "))
    curso = CursoController.get_by_id(id)

    if curso == None:
        print(f"El curso con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return
    
    print(f"""
          ID = {curso.id}
          NOMBRE = {curso.nombre}
          DESCRIPCION = {curso.descripcion}
          CREDITOS = {curso.creditos}
          DEPARTAMENTO_ID = {curso.departamento_id}
          DEPARTAMENTO = {curso.nombre_departamento}
          """)
    input("Presione <Enter> para continuar.")

def agregar():
    print()
    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripción del curso: ")
    creditos = int(input("Ingrese los créditos: "))
    departamento = int(input("Ingrese el ID del departamento al que pertenece: "))

    CursoController.new(nombre, descripcion, creditos, departamento)
    print("Curso agregado exitosamente!")
    input("Presione <Enter> para continuar.")

def modificar():
    print()
    id = int(input("Ingrese el id del curso a eliminar: "))
    curso = CursoController.get_by_id(id)

    if curso == None:
        print(f"El curso con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return
    
    nombre = input(f"Ingrese el nombre del curso ({curso.nombre}): ")
    if nombre == '':
        nombre = curso.nombre

    descripcion = input(f"Ingrese la descripción del curso ({curso.descripcion}): ")
    if descripcion == '':
        descripcion = curso.descripcion

    creditos = input(f"Ingrese los créditos ({curso.creditos}): ")
    if creditos == '':
        creditos = curso.creditos
    else:
        creditos = int(creditos)
    
    departamento = input(f"Ingrese el ID del departamento al que pertenece ({curso.departamento_id}): ")
    if departamento == '':
        departamento = curso.departamento_id
    else:
        departamento = int(departamento)

    CursoController.modify(id, nombre, descripcion, creditos, departamento)
    print("Curso modificado exitosamente!")
    input("Presione <Enter> para continuar.")

def eliminar():
    print()
    id = int(input("Ingrese el id del curso a eliminar: "))
    curso = CursoController.get_by_id(id)

    if curso == None:
        print(f"El curso con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return
    
    CursoController.delete(id)
    print("Curso eliminado exitosamente!")
    input("Presione <Enter> para continuar.")

