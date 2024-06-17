from view.principal import menu
from gui.principal import Principal

def menu_consola():
    menu()

def menu_gui():
    window = Principal()
    window.mainloop()

if __name__ == "__main__":
    menu_gui()

# CRUD - Create Read Update Delete
# MySQL 