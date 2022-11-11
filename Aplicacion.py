# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 06:49:01 2022
https://anderfernandez.com/blog/como-crear-api-en-python/

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
from pandastable import Table

 

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


# Documento Base
archivo = 'abalone.csv'
datos = pd.read_csv(archivo)
 
 
#Funciones

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


def tool_bar(canvas,funcion):
    toolbar = NavigationToolbar2Tk(canvas, funcion)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    canvas.mpl_connect("key_press_event", on_key_press)

   
def Advertencia():
     
    advertencia = tk.Tk()
    advertencia.title('ERROR')
    señal = ttk.Label(advertencia, text="SELECCIONAR DOS VARIABLES")
    señal.place(x=20, y=20)
    
        
    advertencia.mainloop()
   

def Advertencia_2():
    advertencia = tk.Tk()
    advertencia.title('ERROR')
    señal = ttk.Label(advertencia, text="SELECCIONAR UNA VARIABLE")
    señal.place(x=20, y=20)

    advertencia.mainloop()
    

def Advertencia_3():
    advertencia = tk.Tk()
    advertencia.title('ERROR')
    señal = ttk.Label(advertencia, text="SELECCIONAR AL MENOS UNA VARIABLE")
    señal.place(x=20, y=20)
          
    advertencia.mainloop()
    
def correcto():
    correcto = tk.Tk()
    correcto.title('Transaccion Exitosa')
    señal = ttk.Label(correcto, text="SE ELIMINARON LOS DATOS ATIPICOS")
    señal.pack() 
          
    correcto.mainloop()
 

def histograma(valores):

    datos = valores[0]
    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(x=datos)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    ax.set_xlabel('Valor de los datos')
    ax.set_ylabel("Cantidad de los datos")
    
    tool_bar(canvas,funcion)
    
    
    funcion.mainloop()


def boxplot(valores):

    datos = valores[0]
    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.boxplot(x=datos)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    tool_bar(canvas,funcion)
    
    
    funcion.mainloop()

def normplot(valores):

    datos = valores[0]
    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    res = stats.probplot(datos,dist=stats.norm,sparams=(6,),plot=ax)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
       
    tool_bar(canvas,funcion)

    
    funcion.mainloop()

def scatter(valores):

    datosx = valores[0]
    datosy= valores[1]
    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(datosx,datosy)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    tool_bar(canvas,funcion)
    
    funcion.mainloop()    



def ObtenerVariables(x):
    lista = []
    cont = 0
    
    if(longitud.get()): 
        cont+=1 
        lista.append(datos["length"])
    if(diametro.get()): 
        cont+=1
        lista.append(datos["Diameter"])
    if(altura.get()): 
        cont+=1
        lista.append(datos["height"])
    if(whole.get()): 
        cont+=1
        lista.append(datos["Whole Weight"])
    if(shucked.get()): 
        cont+=1
        lista.append(datos["Shucked Weight"])
    if(viscera.get()): 
        cont+=1
        lista.append(datos["Viscera Weight"])
    if(shell.get()): 
        cont+=1
        lista.append(datos["Shell Weight"])
    if(rings.get()): 
        cont+=1
        lista.append(datos["Rings"])
    
    if(cont==0): 
        return Advertencia_3()
         
  
    if(x == 4 and cont >= 3): 
        return Advertencia()
    
    if(x == 4 and cont == 1): 
        return Advertencia()
    
    if(x != 4 and cont >= 2): 
        return Advertencia_2()
    
    
    return lista,cont
    
     
    


def graficar_normal():
    
    valor_grafica = grafico_valor.get()
    
    if(valor_grafica==0): Advertencia_3()
    
    valores,total = ObtenerVariables(valor_grafica)
   
    
    if(total == 2):
        if(valor_grafica==4): scatter(valores)
    else:
        if(valor_grafica==1): histograma(valores)
        if(valor_grafica==2): normplot(valores)
        if(valor_grafica==3): boxplot(valores)
    
    

#------------------------------------

def histograma_a(datos):

    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(x=datos)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    ax.set_xlabel('Valor de los datos')
    ax.set_ylabel("Cantidad de los datos")
    
    tool_bar(canvas,funcion)
    
    
    funcion.mainloop()


def boxplot_a(datos):

    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.boxplot(x=datos)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    tool_bar(canvas,funcion)
    
    
    funcion.mainloop()

def normplot_a(datos):

    
    funcion = tk.Tk()
    
    #Figure(figsize=(5, 4), dpi=100) 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    res = stats.probplot(datos,dist=stats.norm,sparams=(6,),plot=ax)
    

    canvas = FigureCanvasTkAgg(fig, funcion)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
       
    tool_bar(canvas,funcion)

    
    funcion.mainloop()
    

def graficar_atipico(valores,valor):
     
    print(valores)
    print(valor)
    
    valor_grafica = valor
    
    if(valor_grafica==1): histograma(valores)
    if(valor_grafica==2): normplot(valores)
    if(valor_grafica==3): boxplot(valores)

def atipicos_delete(variable_referente,datos_copia):
    
    landa_q1 = float(variable_q1.get())
    landa_q2 = float(variable_q2.get())
    
    print(landa_q1)
    print(landa_q2)
     
    
    Q1 = np.percentile(datos_copia[variable_referente], 25,
               method = 'midpoint')

    Q3 = np.percentile(datos_copia[variable_referente], 75,
               method = 'midpoint')
    IQR = Q3 - Q1
    
    print(datos_copia.shape )
    print("IQR", IQR)
    
    # Upper bound
    upper = np.where(datos_copia[variable_referente] >= (Q3+landa_q2*IQR))
    # Lower bound
    lower = np.where(datos_copia[variable_referente] <= (Q1-landa_q1*IQR))
    
    datos_copia.drop(upper[0], inplace = True)
    datos_copia.drop(lower[0], inplace = True)
    
    print(datos_copia.shape )
    
    return datos_copia
    

def eliminar_atipicos():
    
    datos_copia =  datos.copy() 
    
    variable_referente = combo.get()
    datos_copia = atipicos_delete(variable_referente,datos_copia)   

    #-------------------------------------------------------------------     
  
    root = tk.Tk()
    root.geometry('200x200')
    
    def grafica_atipico():
        
         
        print(combo_g.get())
        
        if(combo_g.get() == "NormPlot"): normplot_a(datos_copia[variable_referente])
        if(combo_g.get() =="Cajas y bigotes"): boxplot_a(datos_copia[variable_referente])
        if(combo_g.get() =="Histograma"): histograma_a(datos_copia[variable_referente])
       
         
    l = ttk.Label(root, text="Seleccione Grafica:")
    l.place(x=20, y=20)
    
    
    combo_g = ttk.Combobox(root,values = ["Histograma",
                                        "Cajas y bigotes",
                                        "NormPlot"
                                        ],state="readonly")
    combo_g.place(x=20, y=40)
 
    
    button_gra = tk.Button(root,text = 'Graficar', command = grafica_atipico)
    button_gra.place(x=20, y=66)  
    
    root.mainloop()



    
     


#--------------------------------------------------------------------------

def media(data):
    return sum(data)/len(data)

def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2
    
    # If the dataset is odd  
    if len(dataset) % 2 != 0:
        return data[index]
    
    # If the dataset is even
    return (data[index - 1] + data[index]) / 2
    
def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items()
                      if value == most_frequent]

    return modes


def lista_valores(data):
    lista_1 = []
    
    lista_1.append(media(data)) #Media
    lista_1.append(median(data)) #Mediana
    lista_1.append(mode(data)) #Moda
    lista_1.append(data.skew()) #Asimetria
    lista_1.append(data.kurt()) #Curtosis
    
    return lista_1

def grafica_valores():
    
    lista = []
    #Media, Moda, Media , Kurtosis, Simetria
   

    #"length"
    
    data = datos["length"]
    lista.append(lista_valores(data))
    

    #"Diameter"
    data = datos["Diameter"]
    lista.append(lista_valores(data))
    
    #"height"
    data = datos["height"]
    lista.append(lista_valores(data))
    
    #"Whole Weight"
    data = datos["Whole Weight"]
    lista.append(lista_valores(data))
    
    #"Shucked Weight"
    data = datos["Shucked Weight"]
    lista.append(lista_valores(data))
    
    #"Viscera Weight"
    data = datos["Viscera Weight"]
    lista.append(lista_valores(data))
    
    #"Shell Weight"
    data = datos["Shell Weight"]
    lista.append(lista_valores(data))
    
    #"Rings"
    data = datos["Rings"]
    lista.append(lista_valores(data))
    
    
    return lista

    
def tabla():
    
    nueva_lista = grafica_valores

    df = pd.DataFrame(nueva_lista())
    df.columns = ["Media", "Mediana","Moda","Asimetria","Kurtosis"]
    
    variables = ["length",
                "Diameter",
                "height",
                "Whole Weight",
                "Shucked Weight",
                "Viscera Weight",
                "Shell Weight",
                "Rings"]
    
    df['Identificador'] = variables
   

    tabla = tk.Tk()
    tabla.geometry('700x500')

    
    frame = tk.Frame(tabla)
    frame.pack(fill='both', expand=True)
    
    pt = Table(frame, dataframe=df, editable=False)
    pt.show()
    
    texto = ttk.Label(tabla, text="INFORMACIÓN DE INTERPRETACIÓN:")
    texto.place(x=55, y=215)
    
    #-----------------------------------
    texto_1 = ttk.Label(tabla, text="Si kurtosis<3 la distribución es Platicúrtica")
    texto_1.place(x=55, y=237)
    
    texto_2 = ttk.Label(tabla, text="Si kurtosis=3 la distribución es Mesocúrtica")
    texto_2.place(x=55, y=260)
    
    texto_3 = ttk.Label(tabla, text="Si kurtosis>3 la distribución es Leptocúrtica")
    texto_3.place(x=55, y=285)
    
    #-----------------------------------
    texto_4 = ttk.Label(tabla, text="asimetría=0 : Distribución simétrica")
    texto_4.place(x=300, y=237)
    
    texto_5 = ttk.Label(tabla, text="asimetría>0: Distribución asimétrica a la derecha")
    texto_5.place(x=300, y=260)
    
    texto_6 = ttk.Label(tabla, text="asimetría<0: Distribución asimétrica a la izquierda")
    texto_6.place(x=300, y=285)
    
    tabla.mainloop()
    
"""
Si kurtosis<3 la distribución es Platicúrtica
Si kurtosis=3 la distribución es Mesocúrtica
Si kurtosis>3 la distribución es Leptocúrtica

asimetría=0 : Distribución simétrica
asimetría>0: Distribución asimétrica a la derecha
asimetría<0: Distribución asimétrica a la izquierda

"""     

#----------------------------------------------------------------------------------------

#PESTAÑA SIN ATIPICOS

#aplicacion Estructura

master = tk.Tk()
master.geometry('500x400')
master.title('Aplicacion')

Graficacion_normal = ttk.Label(master, text="Seleccione Grafica:")
Graficacion_normal.place(x=20, y=20)

#Graficas a Seleccionar

grafico_valor = tk.IntVar() 

primer_grafico = tk.Radiobutton(master, text="Histograma", variable = grafico_valor, value=1)
segundo_grafico = tk.Radiobutton(master, text="Normplot", variable = grafico_valor, value=2)
tercero_grafico = tk.Radiobutton(master, text="Cajas y Bigotes", variable = grafico_valor, value=3)
cuarto_grafico = tk.Radiobutton(master, text="Dispersión", variable = grafico_valor, value=4)

primer_grafico.place(x=20, y=40)
segundo_grafico.place(x=120, y=40)
tercero_grafico.place(x=220, y=40)
cuarto_grafico.place(x=330, y=40)


#Variables de Seleccionables 

#El diagrama de dispersion necesita dos variables
#Los demas diagramas necesitan una variable

variables_normal = ttk.Label(master, text="Seleccione Variables a Graficar:")
variables_normal.place(x=20, y=80)

longitud = tk.IntVar()
diametro = tk.IntVar()
altura = tk.IntVar()
whole = tk.IntVar()
shucked = tk.IntVar()
viscera = tk.IntVar()
shell = tk.IntVar()
rings = tk.IntVar()


objeto_uno = tk.Checkbutton(master, text = "Length ",variable = longitud, onvalue=1, offvalue=0)
objeto_uno.place(x=20, y=100)

objeto_tres = tk.Checkbutton(master, text = "Diameter",variable = diametro, onvalue=1, offvalue=0)
objeto_tres.place(x=20, y=130)

objeto_cuatro = tk.Checkbutton(master, text = "Height",variable = altura, onvalue=1, offvalue=0)
objeto_cuatro.place(x=100, y=100)

objeto_cinco = tk.Checkbutton(master, text = "Whole weight",variable = whole, onvalue=1, offvalue=0)
objeto_cinco.place(x=100, y=130)

objeto_seis = tk.Checkbutton(master, text = "Shucked Weight",variable = shucked, onvalue=1, offvalue=0)
objeto_seis.place(x=200, y=100)

objeto_siete = tk.Checkbutton(master, text = "Viscera Weight",variable = viscera, onvalue=1, offvalue=0)
objeto_siete.place(x=200, y=130)

objeto_ocho = tk.Checkbutton(master, text = "Shell Weight",variable = shell, onvalue=1, offvalue=0)
objeto_ocho.place(x=320, y=100)

objeto_nueve = tk.Checkbutton(master, text = "Rings",variable = rings, onvalue=1, offvalue=0)
objeto_nueve.place(x=320, y=130)
 


button = tk.Button(master,text = 'Graficar', command = graficar_normal)
button.place(x=420, y=140) 


#------------------------------------------------------------------------------------------------------------------------
#PESTAÑA CON ATIPICOS 

separacion = ttk.Label(master, text="--------------------------------------------------------------------------------------")
separacion.place(x=20, y=170)

graficacion_atipicos = ttk.Label(master, text="Graficación sin valores atipicos")
graficacion_atipicos.place(x=20, y=190)

variable_q1 = tk.StringVar()
variable_q2 = tk.StringVar()

q1 = ttk.Label(master, text="Landa Q1")
q1.place(x=30, y=220)
q2 = ttk.Label(master, text="Landa Q3")
q2.place(x=30, y=245)

entrada_1 = ttk.Entry(master,textvariable=variable_q1)
entrada_1.place(x=100, y=220)
entrada_2 = ttk.Entry(master,textvariable=variable_q2)
entrada_2.place(x=100, y=245)

button_atipico = tk.Button(master,text = 'Eliminar Valores Atipicos', command = eliminar_atipicos)
button_atipico.place(x=250, y=245) 

label_combo = ttk.Label(master, text="Seleccione la Variable")
label_combo.place(x=250, y=190)

combo = ttk.Combobox(master,values = ["length",
                                    "Diameter",
                                    "height",
                                    "Whole Weight",
                                    "Shucked Weight",
                                    "Viscera Weight",
                                    "Shell Weight",
                                    "Rings"],state="readonly")
combo.place(x=250, y=220) 

 

 


separacion = ttk.Label(master, text="--------------------------------------------------------------------------------------")
separacion.place(x=20, y=300)

#------------------------------------------------------------------------------------------------------------------------
#GRAFICO DE VALORES

button = tk.Button(master,text = "Generar Tabla de Media,Mediana,Moda,Asimetria,Kurtosis", command = tabla)
button.place(x=20, y=320) 



master.mainloop()

 