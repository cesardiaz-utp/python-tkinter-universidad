from tkinter import StringVar
from tkinter.ttk import Label, Frame, Button, Treeview, Entry, LabelFrame, Combobox, Scrollbar
from tkinter.messagebox import showinfo, showwarning, askyesno

from controller.estudiante import EstudianteController

class StudentUI(Frame):

    def __init__(self, parent) -> None:
        super().__init__(parent)

        Label(self, text="Gestión de estudiantes",
              anchor="center",
              font=("Helvetica", 14)).pack(padx=5, pady=10, fill="x", expand=False)
        
        frame = Frame(self)
        Button(frame, text="Nuevo", command=self.new).pack(anchor="e")
        frame.pack(padx=5, fill="x", expand=False)

        self.__create_table()
        
        frame = Frame(self)
        Button(frame, text="Eliminar", command=self.delete).pack(anchor="e")
        frame.pack(padx=5, fill="x", expand=False)

        # Formulario para llenar datos
        self.__create_form()

    def reset(self):
        self.new()
        self.__load_data()

    def __load_data(self):
        students = EstudianteController.get_all()

        # Borrar los datos actuales
        for item in self.__table.get_children():
            self.__table.delete(item)

        # Agregar los nuevos elementos
        for student in students:
            # ('id', 'name', 'email', 'phone')
            values = (student.id, f"{student.nombre} {student.apellido}", student.email, student.telefono)
            self.__table.insert("", "end", values=values)

    def new(self):
        # Limpiar la seleccion tabla
        for selected in self.__table.selection():
            self.__table.selection_remove(selected)

        # Limpiar los campos del formulario
        self.__firstname.set("")
        self.__lastname.set("")
        self.__email.set("")
        self.__birthdate.set("")
        self.__gender.set("")
        self.__phone.set("")
        self.__address.set("")

        # Asignar foco al texto de nombre
        self.__ent_firstname.focus()

    def delete(self):
        # Si no hay seleccion, mostrar advertencia
        if len(self.__table.selection()) == 0:
            showwarning(title="Eliminar estudiante",
                        message="Debe seleccionar el estudiante a borrar")
            return
        
        # Confirmar si realmente desea eliminar el estudiante
        answer = askyesno(title="Eliminar estudiante",
                          message="¿Está seguro en eliminar a este estudiante?")
        if not(answer):
            return

        # de lo contrario, eliminar estudiante
        selected = self.__table.selection()[0]
        item = self.__table.item(selected)
        item = item["values"]
        id = int(item[0])

        EstudianteController.delete(id)

        # mostrar informacion de confirmación
        showinfo(title="Eliminar estudiante",
                 message="Estudiante eliminado exitosamente")
        
        # Cargar de nuevo la lista de estudiantes
        self.__load_data()
        self.new()

    def save(self):
        # TODO: Validar que los campos estén llenos

        # Si la tabla está seleccionada, se va a actualizar
        if len(self.__table.selection()) > 0:
            selected = self.__table.selection()[0]
            item = self.__table.item(selected)
            item = item["values"]
            id = int(item[0])

            EstudianteController.modify(id=id,
                                        nombre=self.__firstname.get(),
                                        apellido=self.__lastname.get(),
                                        fecha_nacimiento=self.__birthdate.get(),
                                        genero=self.__gender.get(),
                                        email=self.__email.get(),
                                        telefono=self.__phone.get(),
                                        direccion=self.__address.get())

            showinfo(title="Modificar estudiante",
                     message="Estudiante guardado exitósamente")

        # de lo contrariom es un estudiante nuevo
        else:
            EstudianteController.new(nombre=self.__firstname.get(),
                                     apellido=self.__lastname.get(),
                                     fecha_nacimiento=self.__birthdate.get(),
                                     genero=self.__gender.get(),
                                     email=self.__email.get(),
                                     telefono=self.__phone.get(),
                                     direccion=self.__address.get())
            
            showinfo(title="Nuevo estudiante",
                     message="Estudiante guardado exitósamente")
            
        # Cargar de nuevo la lista de estudiantes
        self.__load_data()

    def __select_item(self, event = None):
        for selected_item in self.__table.selection():
            item = self.__table.item(selected_item)
            item = item["values"]
            id = item[0]

            student = EstudianteController.get_by_id(int(id))

            self.__firstname.set(student.nombre)
            self.__lastname.set(student.apellido)
            self.__email.set(student.email)
            self.__birthdate.set(student.fecha_nacimiento)
            self.__gender.set(student.genero)
            self.__address.set(student.direccion)
            self.__phone.set(student.telefono)

            self.__ent_firstname.focus()

    def __create_table(self):
        frame = Frame(self)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        columns = ('id', 'name', 'email', 'phone')
        self.__table = Treeview(frame, columns=columns, show='headings')
        self.__table.heading('id', text="ID")
        self.__table.heading('name', text="Nombre completo")
        self.__table.heading('email', text="Correo electrónico")
        self.__table.heading('phone', text="Teléfono")
        self.__table.bind("<<TreeviewSelect>>", self.__select_item)

        self.__table.grid(row=0, column=0, sticky="nsew")

        scroll = Scrollbar(frame, orient="vertical", command=self.__table.yview)
        self.__table.configure(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns",)

        frame.pack(padx=5, pady=5, fill="both", expand=True)
            
    def __create_form(self):
        frame = LabelFrame(self, text="Datos del estudiante")

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=2)

        # self.nombre = nombre
        Label(frame, 
              text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        self.__firstname = StringVar()
        
        self.__ent_firstname= Entry(frame, textvariable=self.__firstname)
        self.__ent_firstname.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # self.apellido = apellido
        Label(frame, 
              text="Apellido").grid(row=0, column=2, padx=5, pady=5)
        self.__lastname = StringVar()
        Entry(frame, 
              textvariable=self.__lastname).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        
        # self.fecha_nacimiento = fecha_nacimiento
        Label(frame, 
              text="Fecha de nacimiento").grid(row=1, column=0, padx=5, pady=5)
        self.__birthdate = StringVar()
        Entry(frame, 
              textvariable=self.__birthdate).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # self.genero = genero
        Label(frame, 
              text="Genero").grid(row=1, column=2, padx=5, pady=5)
        self.__gender = StringVar()
        cmb = Combobox(frame, textvariable=self.__gender, 
                       state="readonly",
                       values=("M", "F", "I"))
        cmb.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        # self.email = email
        Label(frame, 
              text="Correo electrónico").grid(row=2, column=0, padx=5, pady=5)
        self.__email = StringVar()
        Entry(frame, 
              textvariable=self.__email).grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        # self.telefono = telefono
        Label(frame, 
              text="Teléfono").grid(row=3, column=0, padx=5, pady=5)
        self.__phone = StringVar()
        Entry(frame, 
              textvariable=self.__phone).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # self.direccion = direccion
        Label(frame, 
              text="Dirección").grid(row=3, column=2, padx=5, pady=5)
        self.__address = StringVar()
        Entry(frame, 
              textvariable=self.__address).grid(row=3, column=3, padx=5, pady=5, sticky="ew")
        
        # Guardar
        Button(frame, text="Guardar", command=self.save).grid(row=4, column=3, padx=5, pady=5, sticky="e")

        frame.pack(padx=5, pady=5, fill="x", expand=False)