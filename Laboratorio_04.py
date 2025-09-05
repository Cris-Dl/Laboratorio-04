class Participante:
    def __init__(self, nombre, institucion):
        super().__init__()
        self.nombre = nombre
        self.institucion = institucion

class Banda(Participante):
    def __init__(self, nombre, institucion, categoria, puntaje, id):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = puntaje
        self.id = id

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria in ["primaria", "basico", "diversificado"]:
            self._categoria = categoria
        else:
            print("Categoria invalida, vuelva a intentar")

    @property
    def puntajes(self):
        return self._puntajes

    @puntajes.setter
    def puntajes(self, puntajes):
        if puntajes:
            self._puntajes = puntajes
        else:
            print("No hay puntajes registrados")

    def ver_info(self):
        return f"Nombre:{self.nombre} -- Institución:{self.institucion} -- Categoría:{self.categoria} -- Puntaje:{self.puntajes}"

class Concurso:
    def __init__(self):
        self.diccionario = {}

    def inscribir_banda(self):
        nombre = input("Ingrese el nombre de la banda: ")
        institucion = input("Ingrese el nombre de la institución que pertenece la banda: ")
        categoria = input("Ingrese el nombre de la categoria que pertenecera la banda: ")
        id = input("Ingrese el ID de la banda: ")
        self.diccionario[id] = Banda(nombre, institucion, categoria, 0, id)

    def registrar_evaluacion(self):
        id = input("Ingrese el ID de la banda a registrar sus notas: ")
        if id in self.diccionario:
            nombre = self.diccionario[id].nombre
            institucion = self.diccionario[id].institucion
            categoria = self.diccionario[id].categoria
            ritmo = float(input("Ingrese la nota del ritmo: "))
            uniformidad = float(input("Ingrese la nota de uniformidad: "))
            coreografia = float(input("Ingrese la nota de la coreografia: "))
            alineacion = float(input("Ingrese la nota de alineación: "))
            puntualidad = float(input("Ingrese la nota de puntualidad: "))
            puntaje = (ritmo + uniformidad + coreografia + alineacion + puntualidad)
            banda = Banda(nombre, institucion, categoria, puntaje, id)
            self.diccionario[id] = banda

    def listar_bandas(self):
        if not self.diccionario:
            print("No hay bandas incritas")
        else:
            for bandas in self.diccionario.values():
                print(bandas.ver_info())

import tkinter as tk

def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")

def registrar_evaluacion():
    print("Se abrió la ventana: Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x300")

def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
