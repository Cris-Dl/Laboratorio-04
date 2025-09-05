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

    #def ranking(self):
        #if not self.diccionario:
            #print("No hay bandas incritas")
        #primero = 0
        #segundo = 0
        #tercero = 0
        #else:
            #for bandas in self.diccionario.values():
                #if bandas.puntajes > primero:
                    #primero = bandas.puntajes()

opciones = Concurso()
import tkinter as tk

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")
        opciones.inscribir_banda()

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()

