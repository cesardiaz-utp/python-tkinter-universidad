from tkinter import StringVar, IntVar
from tkinter.ttk import Label, Frame, Button, Treeview, Entry, LabelFrame, Combobox, Scrollbar, Spinbox
from tkinter.messagebox import showinfo, showwarning, askyesno
from tkinter.scrolledtext import ScrolledText

from controller.curso import CursoController
from controller.departamento import DepartamentoController

class CourseUI(Frame):

    def __init__(self, parent) -> None:
        super().__init__(parent)

        Label(self, text="Gestión de cursos",
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

    def __create_table(self):
        frame = Frame(self)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        columns = ('id', 'name', 'credits', 'department')
        self.__table = Treeview(frame, columns=columns, show='headings')
        self.__table.heading('id', text="ID")
        self.__table.heading('name', text="Nombre")
        self.__table.heading('credits', text="Creditos")
        self.__table.heading('department', text="Departamento")

        self.__table.column('id', width=40, anchor="e",stretch=False)
        self.__table.column('credits', width=100, anchor="e",stretch=False)

        self.__table.bind("<<TreeviewSelect>>", self.__select_item)

        self.__table.grid(row=0, column=0, sticky="nsew")

        scroll = Scrollbar(frame, orient="vertical", command=self.__table.yview)
        self.__table.configure(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky="ns",)

        frame.pack(padx=5, pady=5, fill="both", expand=True)
            
    def __create_form(self):
        frame = LabelFrame(self, text="Datos del curso")

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=2)

        # Nombre
        Label(frame, 
              text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.__name = StringVar()
        
        self.__ent_name= Entry(frame, textvariable=self.__name)
        self.__ent_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # creditos
        Label(frame, 
              text="Creditos").grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.__credits = IntVar()
        Spinbox(frame, 
                from_=1, to=9, wrap=True,
                textvariable=self.__credits).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        
        # descripcion
        Label(frame, 
              text="Descripcion").grid(row=1, column=0, padx=5, pady=5, sticky="new")
        self.__description = ScrolledText(frame, height=5)
        self.__description.grid(row=1, column=1, columnspan=3, padx=5, sticky="ew")

        # Departamento
        Label(frame, 
              text="Departamento").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.__department = StringVar()

        # Consulto la informacion de los departamentos disponibles
        values = []
        departments = DepartamentoController.get_all()
        if departments != None:
            values = [department.nombre for department in departments]

        cmb = Combobox(frame, textvariable=self.__department, 
                       state="readonly",
                       values=values)
        cmb.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        # Guardar
        Button(frame, text="Guardar", command=self.save).grid(row=3, column=3, padx=5, pady=5, sticky="e")

        frame.pack(padx=5, pady=5, fill="x", expand=False)

    def __load_data(self):
        courses = CursoController.get_all()

        # Borrar los datos actuales
        for item in self.__table.get_children():
            self.__table.delete(item)

        # Agregar los nuevos elementos
        for course in courses:
            # ('id', 'name', 'credits', 'department')
            values = (course.id, course.nombre, course.creditos, course.nombre_departamento)
            self.__table.insert("", "end", values=values)

    def new(self):
        # Limpiar la seleccion tabla
        for selected in self.__table.selection():
            self.__table.selection_remove(selected)

        # Limpiar los campos del formulario
        self.__name.set("")
        self.__credits.set(1)
        self.__description.delete("1.0", "end")
        self.__department.set("")

        # Asignar foco al texto de nombre
        self.__ent_name.focus()

    def delete(self):
        # Si no hay seleccion, mostrar advertencia
        if len(self.__table.selection()) == 0:
            showwarning(title="Eliminar curso",
                        message="Debe seleccionar el curso a borrar")
            return
        
        # Confirmar si realmente desea eliminar el curso
        answer = askyesno(title="Eliminar curso",
                          message="¿Está seguro en eliminar a este curso?")
        if not(answer):
            return

        # de lo contrario, eliminar curso
        selected = self.__table.selection()[0]
        item = self.__table.item(selected)
        item = item["values"]
        id = int(item[0])

        CursoController.delete(id)

        # mostrar informacion de confirmación
        showinfo(title="Eliminar curso",
                 message="Curso eliminado exitosamente")
        
        # Cargar de nuevo la lista de cursos
        self.__load_data()
        self.new()

    def save(self):
        # TODO: Validar que los campos estén llenos


        # Obtener la información del departamento
        department = DepartamentoController.get_by_name(self.__department.get())

        # Si la tabla está seleccionada, se va a actualizar
        if len(self.__table.selection()) > 0:
            selected = self.__table.selection()[0]
            item = self.__table.item(selected)
            item = item["values"]
            id = int(item[0])

            CursoController.modify(id=id,
                                   nombre=self.__name.get(),
                                   descripcion=self.__description.get("1.0", "end"),
                                   creditos=self.__credits.get(),
                                   departamento_id=department.id)

            showinfo(title="Modificar curso",
                     message="Curso guardado exitósamente")

        # de lo contrariom es un curso nuevo
        else:
            CursoController.new(nombre=self.__name.get(),
                                descripcion=self.__description.get("1.0", "end"),
                                creditos=self.__credits.get(),
                                departamento_id=department.id)
            
            showinfo(title="Nuevo curso",
                     message="Curso guardado exitósamente")
            
        # Cargar de nuevo la lista de cursos
        self.__load_data()

    def __select_item(self, event = None):
        for selected_item in self.__table.selection():
            item = self.__table.item(selected_item)
            item = item["values"]
            id = item[0]

            course = CursoController.get_by_id(int(id))

            self.__name.set(course.nombre)
            self.__credits.set(course.creditos)
            self.__description.delete("1.0", "end")
            self.__description.insert("1.0", course.descripcion)
            self.__department.set(course.nombre_departamento)
            
            self.__ent_name.focus()
