from tkinter import Tk, Menu
from tkinter.ttk import Frame, Label
from tkinter.messagebox import showinfo, askyesno

from gui.curso import CourseUI
from gui.estudiante import StudentUI

class Principal(Tk):

    def __init__(self):
        super().__init__()
        self.title("Gestión de universidad")

        self.__center_screen(800,600)
        self.__create_menu()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # Cargo las ventanas disponibles
        self.__register_windows(container)

        self.__open_window("default")

    def __create_menu(self):
        menubar = Menu()

        # Cambiando el comportamiento del boton cerrar
        self.protocol("WM_DELETE_WINDOW", lambda: self.__exit())

        # Menu archivo
        file = Menu(menubar, tearoff=False)
        file.add_command(label="Salir", 
                         accelerator="Ctrl+Q",
                         command= lambda: self.__exit())
        self.bind_all("<Control-q>", lambda event: self.__exit())
        menubar.add_cascade(menu=file, label="Archivo")

        # Menu gestion
        manager = Menu(menubar, tearoff=False)
        manager.add_command(label="Cursos", command=lambda: self.__open_window("cursos"))
        manager.add_command(label="Profesores", command=lambda: self.__open_window("profesores"))
        manager.add_command(label="Estudiantes", command=lambda: self.__open_window("estudiantes"))

        menubar.add_cascade(menu=manager, label="Gestión")

        self.config(menu=menubar)

    def __center_screen(self, width: int, height: int):
        center_x = int(self.winfo_screenwidth()/2 - width/2)
        center_y = int(self.winfo_screenheight()/2 - height/2)

        self.geometry(f"{width}x{height}+{center_x}+{center_y}")

    def __register_windows(self, container):
        self.frames = dict()
        self.frames['default'] = DefaultUI(container)
        self.frames['default'].grid(row=0, column=0, sticky="nsew")
        self.frames['estudiantes'] = StudentUI(container)
        self.frames['estudiantes'].grid(row=0, column=0, sticky="nsew")
        self.frames['cursos'] = CourseUI(container)
        self.frames['cursos'].grid(row=0, column=0, sticky="nsew")

    def __open_window(self, option):

        if not(option in self.frames):
            showinfo(title="Abrir ventana", 
                     message=f"Esta intentando abrir la ventana '{option}' y esta no existe")
            option = "default"

        frame = self.frames[option]
        frame.reset()
        frame.tkraise()

    def __exit(self):
        answer = askyesno(title="Salir", 
                 message="¿Está seguro que quiere salir de la aplicación?")
        if answer:
            self.quit()

class DefaultUI(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        Label(self, 
              text="Bienvenido a la aplicación de gestión de universidad",
              anchor="center",
              font=("Helvetica", 15)).pack(fill="x", expand=True)
        
    def reset(self):
        pass
