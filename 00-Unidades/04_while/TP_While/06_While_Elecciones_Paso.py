import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustín Daniel
apellido: Monzón
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        votos_maximo = 1
        votos_minimo = -1
        nombre_maximo = "ninguno"
        nombre_minimo = "ninguno"
        edad_minimo = 0

        contador_edad = 0
        acumulador_edad = 0
        acumulador_votos = 0

        seguir = True

        while seguir == True:
            nombre = prompt("", "Ingrese Nombre")

            edad = prompt("", "Ingrese Edad")
            edad = int(edad)
            while edad < 25:
                edad = prompt("Error", "Ingrese Edad")
                edad = int(edad)
            
            votos = prompt("", "Ingrese Votos")
            votos = int(votos)
            while votos < 0:
                votos = prompt("Error", "Ingrese Votos")
                votos = int(votos)
            
            if votos > votos_maximo:
                votos_maximo = votos
                nombre_maximo = nombre
            elif votos < votos_minimo or votos_minimo == -1:
                votos_minimo = votos
                nombre_minimo = nombre
                edad_minimo = edad
            
            if edad >= 25:
                contador_edad = contador_edad + 1
                acumulador_edad = acumulador_edad + edad
            
            if votos > 0:
                acumulador_votos = acumulador_votos + votos
            
            seguir = question("seguir", "Ingresa otro empleado?")

        if contador_edad != 0:
            promedio = acumulador_edad / contador_edad
        else:
            promedio = 0

        mensaje = "La persona con más votos fue: {0}, la persona con menos votos fue {1} y su edad es de {2}. Promedio de edades {3}, Votos totales {4}".format(nombre_maximo, nombre_minimo, edad_minimo,promedio,acumulador_votos)
        alert("", mensaje)
    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
