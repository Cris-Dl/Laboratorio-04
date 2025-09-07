import tkinter as tk
from tkinter import messagebox


class Participante:
    def __init__(self, nombre, institucion):
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
        if puntajes >= 0:
            self._puntajes = puntajes
        else:
            print("No hay puntajes registrados")

    def ver_info(self):
        return f"Nombre:{self.nombre} -- Institución:{self.institucion} -- Categoría:{self.categoria} -- Puntaje:{self.puntajes}"


class Concurso:
    def __init__(self):
        self.diccionario = {}

    def inscribir_banda(self, nombre, institucion, categoria, id):
        if id in self.diccionario:
            return "ID ya existe."
        self.diccionario[id] = Banda(nombre, institucion, categoria, 0, id)
        return "Banda inscrita correctamente."

    def registrar_evaluacion(self, id, ritmo, uniformidad, coreografia, alineacion, puntualidad):
        if id not in self.diccionario:
            return "ID no encontrado."

        banda = self.diccionario[id]
        try:
            ritmo = float(ritmo)
            uniformidad = float(uniformidad)
            coreografia = float(coreografia)
            alineacion = float(alineacion)
            puntualidad = float(puntualidad)
        except ValueError:
            return "Los puntajes deben ser números."

        puntaje_total = ritmo + uniformidad + coreografia + alineacion + puntualidad
        banda.puntajes = puntaje_total
        return "Evaluación registrada correctamente."

    def listar_bandas(self):
        if not self.diccionario:
            return "No hay bandas inscritas."
        return "\n".join([banda.ver_info() for banda in self.diccionario.values()])

    def ranking(self):
        if not self.diccionario:
            return "No hay bandas inscritas para crear un ranking."

        bandas = list(self.diccionario.values())
        info = "Ranking de Bandas:\n"
        posicion = 1

        while bandas:
            mejor = bandas[0]
            for b in bandas:
                if b.puntajes > mejor.puntajes:
                    mejor = b
            info += f"{posicion}. {mejor.nombre} - Puntaje: {mejor.puntajes}\n"
            bandas.remove(mejor)
            posicion += 1

        return info


class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.concurso = Concurso()
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
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda_gui)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion_gui)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas_gui)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking_gui)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda_gui(self):
        ventana_inscripcion = tk.Toplevel(self.ventana)
        ventana_inscripcion.title("Inscribir Banda")
        ventana_inscripcion.geometry("300x300")

        tk.Label(ventana_inscripcion, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(ventana_inscripcion)
        nombre_entry.pack(pady=5)

        tk.Label(ventana_inscripcion, text="Institución:").pack(pady=5)
        institucion_entry = tk.Entry(ventana_inscripcion)
        institucion_entry.pack(pady=5)

        tk.Label(ventana_inscripcion, text="Categoría (primaria/basico/diversificado):").pack(pady=5)
        categoria_entry = tk.Entry(ventana_inscripcion)
        categoria_entry.pack(pady=5)

        tk.Label(ventana_inscripcion, text="ID:").pack(pady=5)
        id_entry = tk.Entry(ventana_inscripcion)
        id_entry.pack(pady=5)

        def guardar():
            nombre = nombre_entry.get()
            institucion = institucion_entry.get()
            categoria = categoria_entry.get()
            id_banda = id_entry.get()

            if not all([nombre, institucion, categoria, id_banda]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            mensaje = self.concurso.inscribir_banda(nombre, institucion, categoria, id_banda)
            if "correctamente" in mensaje:
                messagebox.showinfo("Éxito", mensaje)
                ventana_inscripcion.destroy()
            else:
                messagebox.showerror("Error", mensaje)

        tk.Button(ventana_inscripcion, text="Inscribir", command=guardar).pack(pady=10)

    def registrar_evaluacion_gui(self):
        ventana_evaluacion = tk.Toplevel(self.ventana)
        ventana_evaluacion.title("Registrar Evaluación")
        ventana_evaluacion.geometry("300x450")

        tk.Label(ventana_evaluacion, text="ID de la Banda:").pack(pady=5)
        id_entry = tk.Entry(ventana_evaluacion)
        id_entry.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntaje de Ritmo:").pack(pady=5)
        ritmo_entry = tk.Entry(ventana_evaluacion)
        ritmo_entry.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntaje de Uniformidad:").pack(pady=5)
        uniformidad_entry = tk.Entry(ventana_evaluacion)
        uniformidad_entry.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntaje de Coreografía:").pack(pady=5)
        coreografia_entry = tk.Entry(ventana_evaluacion)
        coreografia_entry.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntaje de Alineación:").pack(pady=5)
        alineacion_entry = tk.Entry(ventana_evaluacion)
        alineacion_entry.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntaje de Puntualidad:").pack(pady=5)
        puntualidad_entry = tk.Entry(ventana_evaluacion)
        puntualidad_entry.pack(pady=5)

        def guardar_evaluacion():
            id_banda = id_entry.get()
            ritmo = ritmo_entry.get()
            uniformidad = uniformidad_entry.get()
            coreografia = coreografia_entry.get()
            alineacion = alineacion_entry.get()
            puntualidad = puntualidad_entry.get()

            if not all([id_banda, ritmo, uniformidad, coreografia, alineacion, puntualidad]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            mensaje = self.concurso.registrar_evaluacion(id_banda, ritmo, uniformidad, coreografia, alineacion, puntualidad)
            if "correctamente" in mensaje:
                messagebox.showinfo("Éxito", mensaje)
                ventana_evaluacion.destroy()
            else:
                messagebox.showerror("Error", mensaje)

        tk.Button(ventana_evaluacion, text="Registrar", command=guardar_evaluacion).pack(pady=10)

    def listar_bandas_gui(self):
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("600x400")

        info = self.concurso.listar_bandas()

        texto_info = tk.Text(ventana_listado, height=20, width=70)
        texto_info.pack(padx=10, pady=10)

        texto_info.insert(tk.END, info)
        texto_info.config(state=tk.DISABLED)

    def ver_ranking_gui(self):
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("400x300")

        info = self.concurso.ranking()

        texto_ranking = tk.Text(ventana_ranking, height=15, width=50)
        texto_ranking.pack(padx=10, pady=10)

        texto_ranking.insert(tk.END, info)
        texto_ranking.config(state=tk.DISABLED)


if __name__ == "__main__":
    ConcursoBandasApp()