import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustín Daniel
apellido: Monzón
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cantidad = 0
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0

        #Acumulador Numeros Positivos
        while True:
            numero = prompt("", "Ingresa un numero")
            if numero == None:
                break
            
            numero = int(numero)

            if numero > 0:
                acumulador_positivos = acumulador_positivos + numero
                contador_positivos = contador_positivos + 1
            elif numero < 0:
                acumulador_negativos = acumulador_negativos + numero
                contador_negativos = contador_negativos + 1
            else:
                contador_ceros = contador_ceros + 1

        diferencia_numeros = contador_positivos - contador_negativos

        mensaje = "Suma de negativos {0}, Suma de positivos {1}, Cantidad de negativos {2}, Cantidad de positivos {3}, Cantidad de ceros {4} y Diferencia de cantidades {5}".format(acumulador_negativos, acumulador_positivos, contador_negativos, contador_positivos, contador_ceros, diferencia_numeros)

        alert("", mensaje)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
