from controller.estudiante import EstudianteController

def menu_estudiantes():
    exit = False

    while not(exit):
        print()
        print("#" * 80)
        print("# Gestion de estudiantes")
        print("#" * 80)
        print("1. Listar todos los estudiantes")
        print("2. Consultar un estudiante")
        print("3. Agregar un estudiante")
        print("4. Modificar un estudiante")
        print("5. Eliminar un estudiante")
        print("0. Volver al menu principal")

        option = int(input("Ingrese su opción: "))
        if option == 1:
            listar_estudiantes()
        elif option == 2:
            consultar_estudiante()
        elif option == 3:
            agregar_estudiante()
        elif option == 4:
            modificar_estudiante()
        elif option == 5:
            eliminar_estudiante()
        elif option == 0:
            exit = True
        else:
            print("Opción no válida!\n Verifica la opción seleccionada.")

def listar_estudiantes():
    estudiantes = EstudianteController.get_all()
    print(" ID | Nombre completo            | Correo electrónico ")
    print("=" * 60)
    for est in estudiantes:
        print(f"{est.id} | {est.nombre} {est.apellido} | {est.email}")
    
    input("Presione <Enter> para continuar.")

def consultar_estudiante():
    print()
    id = int(input("Ingrese el id del estudiante: "))
    est = EstudianteController.get_by_id(id)

    if est == None:
        print(f"Estudiante con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return

    print(f"""
            Id = {est.id}
            Nombre = {est.nombre}
            Apellido = {est.apellido}
            Fecha de nacimiento = {est.fecha_nacimiento}
            Genero = {est.genero}
            Email = {est.email}
            Telefono = {est.telefono}
            Direccion = {est.direccion}                
          """)
    
    input("Presione <Enter> para continuar.")

def agregar_estudiante():
    print()
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (AAAA-MM-DD): ")
    genero = input("Ingrese el genero: ")
    email = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el número telefónico: ")
    direccion = input("Ingrese la dirección: ")

    EstudianteController.new(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)

    print("¡Estudiante creado exitosamente!")
    input("Presione <Enter> para continuar.")

def modificar_estudiante():
    print()
    id = int(input("Ingrese el id del estudiante a modificar: "))
    est = EstudianteController.get_by_id(id)
    
    if est == None:
        print(f"Estudiante con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return

    nombre = input(f"Ingrese el nombre del estudiante ({est.nombre}): ")
    if nombre == '':
        nombre = est.nombre

    apellido = input(f"Ingrese el apellido del estudiante ({est.apellido}): ")
    if apellido == '':
        apellido = est.apellido

    fecha_nacimiento = input(f"Ingrese la fecha de nacimiento ({est.fecha_nacimiento}): ")
    if fecha_nacimiento == '':
        fecha_nacimiento = est.fecha_nacimiento

    genero = input(f"Ingrese el genero ({est.genero}): ")
    if genero == '':
        genero = est.genero

    email = input(f"Ingrese el correo electrónico ({est.email}): ")
    if email == '':
        email = est.email

    telefono = input(f"Ingrese el número telefónico ({est.telefono}): ")
    if telefono == '':
        telefono = est.telefono

    direccion = input(f"Ingrese la dirección ({est.direccion}): ")
    if direccion == '':
        direccion = est.direccion

    EstudianteController.modify(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)

    print("¡Estudiante modificado exitosamente!")
    input("Presione <Enter> para continuar.")

def eliminar_estudiante():
    print()
    id = int(input("Ingrese el id del estudiante a modificar: "))
    est = EstudianteController.get_by_id(id)
    
    if est == None:
        print(f"Estudiante con el id {id} no existe!")
        input("Presione <Enter> para continuar.")
        return

    EstudianteController.delete(id)

    print("¡Estudiante eliminado exitosamente!")
    input("Presione <Enter> para continuar.")
