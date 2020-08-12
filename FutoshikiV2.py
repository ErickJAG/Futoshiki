from tkinter import *
import tkinter as tk
import ast
import random
from tkinter import messagebox
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


inicio=Tk()
inicio.geometry("300x400")
inicio.resizable(0, 0)
inicio.title("Menu Principal")
inicio.iconbitmap("Metaverse.ico")
inicio.configure(bg="black")
#Definicion de variable principales
iniciar=False
seconds=0
mins=0
hours=0
s2=0
m2=0
h2=0
opcion=""
ini=False
cargada=False
jugadas=[]
borradas=[]
lvl=""
win=False
top=False
matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
matriz2=[["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
matriz3=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
#############
#Funcionalidad: terminar el programa
def salga():
    inicio.destroy()
#Funcionalidad: abrir el PDF con el manual
def helps():
    os.system("manual_de_usuario_futoshiki.PDF")
#Funcionalidad: abrir una ventana on la info del programa
def abouts():
    messagebox.showinfo("Acerca del programa", "Nombre de programa: FutoshikiV2\nVersion: 3.7.3\nAutor: Erick Astorga Gamboa")
ayuda=Button(inicio,text="Ayuda",background="orange",activebackground="orange",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda:helps())
ayuda.place(x=102, y=170)
about=Button(inicio,text="Acerca de",background="orange",activebackground="orange",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda:abouts())
about.place(x=82, y=230)
salir=Button(inicio,text="Salir",background="red",activebackground="red",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda:salga())
salir.place(x=112, y=290)
#############
#Definicion de variable secundarias
r=""
d=""
p=""
d2=""
nombre=""
#No posee entradas especificas
#Salida: una ventana con la configuracion
#Funcionalidad: desplegar una ventana con las opciones de la configuracion
def confi():
    #Funcionalidad: cerrar la ventana de configuracion al terminar de usarla
    def salirConfi():
        if r=="" or p=="" or d=="":
            configuracion.destroy()
        else:
            iniciar.configure(state="normal")
            configuracion.destroy()
            if r=="Timer":
                #Funcionalidad: definir las variables necesarias para tener
                #el tiempo del timer guardado en caso de querer reiniciar y para
                #crear el timer de una vez
                def opTimer():
                    global seconds
                    global mins
                    global hours
                    global s2
                    global m2
                    global h2
                    ho=horas.get()
                    mi=minutos.get()
                    se=segundos.get()
                    if ho=="" or se=="" or mi=="":
                        messagebox.showinfo("Configurando temporizador", "Porfavor digite un valor en cada\nespacio antes de continuar")
                    elif ho.isdigit()==False or mi.isdigit()==False or se.isdigit()==False:
                        messagebox.showinfo("Configurando temporizador", "Porfavor digite un valor numerico")
                    elif int(ho)<0 or int(ho)>2:
                        messagebox.showinfo("Error de horas", "Porfavor digite un valor del 0 al 59")
                    elif int(mi)<0 or int(mi)>59:
                        messagebox.showinfo("Error de minutos", "Porfavor digite un valor del 0 al 59")
                    elif int(se)<0 or int(se)>59:
                        messagebox.showinfo("Error de segundos", "Porfavor digite un valor del 0 al 59")
                    else:
                        hours=int(ho)
                        mins=int(mi)
                        seconds=int(se)
                        s2=seconds
                        h2=hours
                        m2=mins
                        temporizador.destroy()
                #Ventana en caso de que se elija usar timer
                temporizador=Tk()
                temporizador.geometry("300x400")
                temporizador.resizable(0, 0)
                temporizador.title("Timer")
                temporizador.iconbitmap("Metaverse.ico")
                temporizador.configure(bg="black")
                Label(temporizador,text="Horas (de 0 a 2)",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=62,y=35)
                Label(temporizador,text="Minutos (de 0 a 59)",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=62,y=135)
                Label(temporizador,text="Segundos (de 0 a 59)",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=62,y=235)
                segundos=Entry(temporizador,font=("Trebuchet MS", 12, "bold"))
                segundos.place(x=62,y=285)
                minutos=Entry(temporizador,font=("Trebuchet MS", 12, "bold"))
                minutos.place(x=62,y=185)
                horas=Entry(temporizador,font=("Trebuchet MS", 12, "bold"))
                horas.place(x=62,y=85)
                exits=Button(temporizador,text="Continuar",relief=RAISED,bg="grey",activebackground="grey",font=("Trebuchet MS", 12, "bold"),command=lambda:opTimer())
                exits.place(x=110,y=338)
                temporizador.mainloop()
    #Funcionalidad: definir la configuracion del reloj
    def opreloj(op):
        global r
        r=op
    #Funcionalidad: definir la configuracion de dificultad
    def opdificultad(op):
        global d
        global d2
        if op=="Multi Nivel":
            d="Facil"
            d2=op
        else:
            d=op
    #Funcionalidad: definir la configuracion del panel
    def oppanel(op):
        global p
        p=op
    global r
    global d
    global p
    configuracion=Tk()
    configuracion.iconbitmap("Metaverse.ico")
    configuracion.geometry("600x350")
    configuracion.configure(bg="black")
    configuracion.title("Configuracion")
    configuracion.resizable(0, 0)
    R=tk.IntVar()
    D=tk.IntVar()
    P=tk.IntVar()
    texto1=Label(configuracion,text="Reloj",fg="green",bg="black",font=("Trebuchet MS", 17, "bold"))
    texto1.place(x=50,y=20)
    texto2=Label(configuracion,text="Dificultad",fg="green",bg="black",font=("Trebuchet MS", 17, "bold"))
    texto2.place(x=185,y=20)
    texto3=Label(configuracion,text="Posicion de digitos",fg="green",bg="black",font=("Trebuchet MS", 17, "bold"))
    texto3.place(x=350,y=20)
    f=50
    c=70
    val=0
    reloj1=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Si",variable=R,value=1,font=("Trebuchet MS", 17, "bold"))
    reloj1.configure(command=lambda: opreloj(reloj1["text"]))
    reloj1.place(x=50,y=70)
    reloj2=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="No",variable=R,value=2,font=("Trebuchet MS", 17, "bold"))
    reloj2.configure(command=lambda: opreloj(reloj2["text"]))
    reloj2.place(x=50,y=120)
    reloj3=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Timer",variable=R,value=3,font=("Trebuchet MS", 17, "bold"))
    reloj3.configure(command=lambda: opreloj(reloj3["text"]))
    reloj3.place(x=50,y=170)
    dificultad1=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Facil",variable=D,value=1,font=("Trebuchet MS", 17, "bold"))
    dificultad1.configure(command=lambda: opdificultad(dificultad1["text"]))
    dificultad1.place(x=185,y=70)
    dificultad2=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Normal",variable=D,value=2,font=("Trebuchet MS", 17, "bold"))
    dificultad2.configure(command=lambda: opdificultad(dificultad2["text"]))
    dificultad2.place(x=185,y=120)
    dificultad3=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Dificil",variable=D,value=3,font=("Trebuchet MS", 17, "bold"))
    dificultad3.configure(command=lambda: opdificultad(dificultad3["text"]))
    dificultad3.place(x=185,y=170)
    dificultad4=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Multi Nivel",variable=D,value=4,font=("Trebuchet MS", 17, "bold"))
    dificultad4.configure(command=lambda: opdificultad(dificultad4["text"]))
    dificultad4.place(x=185,y=220)
    posicion1=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Izquierda",variable=P,value=1,font=("Trebuchet MS", 17, "bold"))
    posicion1.configure(command=lambda: oppanel(posicion1["text"]))
    posicion1.place(x=350,y=100)
    posicion2=Radiobutton(configuracion,selectcolor="black",activeforeground="green",activebackground="black",fg="green",bg="black",text="Derecha",variable=P,value=2,font=("Trebuchet MS", 17, "bold"))
    posicion2.configure(command=lambda: oppanel(posicion2["text"]))
    posicion2.place(x=350,y=150)
    confirmar=Button(configuracion,text="Confirmar",background="green",activebackground="green",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda: salirConfi())
    confirmar.place(x=235,y=280)
    configuracion.mainloop()
conf=Button(inicio,text="Configuracion",background="green",activebackground="green",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda: confi())
conf.place(x=60, y=110)
#No posee entradas especificas
#Salida: tablero de juego
#Funcionalidad: crear el tablero de juego
def juego():
    global ini
    global win
    global cargada
    global matriz
    global matriz2
    global matriz3
    win=False
    ini=False
    ###########################
    #Funcionalidad: definir la variable opcion dependiendo del panel elegido
    def elejirOp(op):
        global opcion
        global ini
        if ini==True:
            opcion=op
            if op==panel1["text"]:
                panel1.configure(bg="green")
                panel2.configure(bg="white")
                panel3.configure(bg="white")
                panel4.configure(bg="white")
                panel5.configure(bg="white")
            elif op==panel2["text"]:
                panel1.configure(bg="white")
                panel2.configure(bg="green")
                panel3.configure(bg="white")
                panel4.configure(bg="white")
                panel5.configure(bg="white")
            elif op==panel3["text"]:
                panel1.configure(bg="white")
                panel2.configure(bg="white")
                panel3.configure(bg="green")
                panel4.configure(bg="white")
                panel5.configure(bg="white")
            elif op==panel4["text"]:
                panel1.configure(bg="white")
                panel2.configure(bg="white")
                panel3.configure(bg="white")
                panel4.configure(bg="green")
                panel5.configure(bg="white")
            else:
                panel1.configure(bg="white")
                panel2.configure(bg="white")
                panel3.configure(bg="white")
                panel4.configure(bg="white")
                panel5.configure(bg="green")
    ###########################
    if cargada==False:
        matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
        matriz2=[["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
        matriz3=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    global r
    global p
    global d
    global d2
    global seconds
    global mins
    global hours
    global nombre
    global jugadas
    global borradas
    global lvl
    global s2
    global m2
    global h2
    difficulties=[]
    futo=Tk()
    futo.geometry("1000x800")
    futo.resizable(0, 0)
    futo.title("FutoshikiV2")
    futo.iconbitmap("Metaverse.ico")
    futo.configure(bg="black")
    level=[0,1,2]
    if lvl=="":
        lvl=random.choice(level)
    file=open("futoshiki2020partidas.dat","r")
    contenido=file.readlines()
    for i in range (0,len(contenido),1):
        dato=contenido[i].find(";")
        valor=(contenido[i][0:dato])
        difficulties+=[valor]
    file.close
    listaEasy=ast.literal_eval(difficulties[0])
    listaNormal=ast.literal_eval(difficulties[1])
    listaHard=ast.literal_eval(difficulties[2])
    ###########################
    #Creacion del reloj en caso de ser elegido
    if r=="Si":
        if cargada==False:
            jugadas=[]
            matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
            matriz2=[["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
            matriz3=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
            if d2=="Multi Nivel" and d!="Facil":
                pass
            else:
                nombre=""
                seconds=0
                mins=0
                hours=0
        strs=str(seconds)
        strm=str(mins)
        strh=str(hours)
        if seconds<10:
            strs="0"+str(seconds)
        if hours<10:
            strh="0"+str(hours)
        if mins<10:
            strm="0"+str(mins)
        tiempo=strh+":"+strm+":"+strs
        timer_display=Label(futo,text=tiempo,bg="light grey",font=("Trebuchet MS",30,"bold"))
        timer_display.place(x=30,y=702)
    elif r=="Timer":
        if cargada==False:
            jugadas=[]
            matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
            matriz2=[["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
            matriz3=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
            if d2=="Multi Nivel" and d!="Facil":
                pass
            else:
                nombre=""
                seconds=s2
                mins=m2
                hours=h2
        strs=str(seconds)
        strm=str(mins)
        strh=str(hours)
        if seconds<10:
            strs="0"+str(seconds)
        if hours<10:
            strh="0"+str(hours)
        if mins<10:
            strm="0"+str(mins)
        tiempo=strh+":"+strm+":"+strs
        timer_display=Label(futo,text=tiempo,bg="light grey",font=("Trebuchet MS",30,"bold"))
        timer_display.place(x=30,y=702)
    ###########################
    #Creacion de las matrizes que tienen los valores del
    #del tablero dependiendo de la dificultad
    if cargada==False:
        if d=="Facil":
            for i in listaEasy[lvl]:
                if i[0]=="<" or i[0]==">":
                    matriz2[int(i[1])][int(i[2])]=i[0]
                elif i[0]=="^" or i[0]=="v":
                    matriz3[int(i[1])][int(i[2])]=i[0]
                else:
                    matriz[int(i[1])][int(i[2])]=int(i[0])
        elif d=="Normal":
            for i in listaNormal[lvl]:
                if i[0]=="<" or i[0]==">":
                    matriz2[int(i[1])][int(i[2])]=i[0]
                elif i[0]=="^" or i[0]=="v":
                    matriz3[int(i[1])][int(i[2])]=i[0]
                else:
                    matriz[int(i[1])][int(i[2])]=int(i[0])
        else:
            for i in listaHard[lvl]:
                if i[0]=="<" or i[0]==">":
                    matriz2[int(i[1])][int(i[2])]=i[0]
                elif i[0]=="^" or i[0]=="v":
                    matriz3[int(i[1])][int(i[2])]=i[0]
                else:
                    matriz[int(i[1])][int(i[2])]=int(i[0])
    ###########################
    #Creacion del panel de digitos
    if p=="Izquierda":
        panel1=Button(futo,height=2,width=6,text="1",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel1.configure(command=lambda: elejirOp(panel1["text"]))
        panel1.place(x=100,y=100)
        panel2=Button(futo,height=2,width=6,text="2",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel2.configure(command=lambda: elejirOp(panel2["text"]))
        panel2.place(x=100,y=200)
        panel3=Button(futo,height=2,width=6,text="3",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel3.configure(command=lambda: elejirOp(panel3["text"]))
        panel3.place(x=100,y=300)
        panel4=Button(futo,height=2,width=6,text="4",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel4.configure(command=lambda: elejirOp(panel4["text"]))
        panel4.place(x=100,y=400)
        panel5=Button(futo,height=2,width=6,text="5",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel5.configure(command=lambda: elejirOp(panel5["text"]))
        panel5.place(x=100,y=500)
    else:
        panel1=Button(futo,height=2,width=6,text="1",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel1.configure(command=lambda: elejirOp(panel1["text"]))
        panel1.place(x=830,y=100)
        panel2=Button(futo,height=2,width=6,text="2",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel2.configure(command=lambda: elejirOp(panel2["text"]))
        panel2.place(x=830,y=200)
        panel3=Button(futo,height=2,width=6,text="3",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel3.configure(command=lambda: elejirOp(panel3["text"]))
        panel3.place(x=830,y=300)
        panel4=Button(futo,height=2,width=6,text="4",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel4.configure(command=lambda: elejirOp(panel4["text"]))
        panel4.place(x=830,y=400)
        panel5=Button(futo,height=2,width=6,text="5",activebackground="green",bg="white",relief=RAISED,font=("Trebuchet MS", 12, "bold"))
        panel5.configure(command=lambda: elejirOp(panel5["text"]))
        panel5.place(x=830,y=500)
    ###########################
    #Funcionalidad: registrar la partida en caso de que se complete
    #con exito
    def terminado():
        global seconds
        global mins
        global hours
        global s2
        global m2
        global h2
        global nombre
        global d
        global d2
        global r
        global top
        global opcion
        top=True
        if r=="Si":
            if seconds<10:
                strS="0"+str(seconds)
            else:
                strS=str(seconds)
            if mins<10:
                strM="0"+str(mins)
            else:
                strM=str(mins)
            if hours<10:
                strH="0"+str(hours)
            else:
                strH=str(hours)
            strTiempo=strH+":"+strM+":"+strS
            string=str(nombre)+";"+strTiempo+";"+str(d)
            file=open("futoshiki2020top10.dat","a")
            file.write(string)
            file.write("\n")
            file.close()
            file=open("futoshiki2020top10.dat","a")
            file.close()
        elif r=="Timer":
            seconds=int(s2)-int(seconds)
            mins=int(m2)-int(mins)
            hours=int(h2)-int(hours)
            if seconds<0:
                seconds=60+seconds
            if mins<0:
                mins=60+mins
                hours=int(hours)+1
            if seconds<10:
                strS="0"+str(seconds)
            else:
                strS=str(seconds)
            if mins<10:
                strM="0"+str(mins)
            else:
                strM=str(mins)
            strH="0"+str(hours)
            strTiempo=strH+":"+strM+":"+strS
            if d2=="Multi Nivel":
                string=str(nombre)+";"+strTiempo+";"+str(d2)
            else:
                string=str(nombre)+";"+strTiempo+";"+str(d)
            file=open("futoshiki2020top10.dat","a")
            file.write(string)
            file.write("\n")
            file.close()
            file=open("futoshiki2020top10.dat","a")
            file.close()
        borrar.configure(state="disabled")
        redo.configure(state="disabled")
        terminar.configure(state="disabled")
        erase.configure(state="disabled")
        topTen.configure(state="disabled")
        guardar.configure(state="disabled")
        panel1.configure(state="disabled",bg="white")
        panel2.configure(state="disabled",bg="white")
        panel3.configure(state="disabled",bg="white")
        panel4.configure(state="disabled",bg="white")
        panel5.configure(state="disabled",bg="white")
        opcion=""
        if d2=="Multi Nivel":
            messagebox.showinfo("Felicidades", "Ha terminado todas las dificultades")
        else:
            messagebox.showinfo("Felicidades", "Ha llenado el tablero completo")
        top=False
    ###########################
    #Funcionalidad: cargar la siguiente dificultad
    def nextLevel():
        global d
        string="Nivel "+d+" completado\nEmpezando siguiente nivel"
        if d=="Facil":
            d="Normal"
        else:
            d="Dificil"
        futo.destroy()
        messagebox.showinfo("Felicidades", string)
        juego()
    ###########################
    #Funcionalidad: manejar el reloj de fondo
    def reloj():
        global win
        global seconds
        global mins
        global hours
        global top
        if top==True:
            pass
        else:
            seconds=seconds+1
            mins=mins+seconds//60
            hours=hours+mins//60
            m=str(mins)
            h=str(hours)
            if hours<10:
                h="0"+str(hours)
            if mins<10:
                m="0"+str(mins)
            if seconds==60:
                seconds=0
            se=seconds
            s=str(se)
            if se<10:
                s="0"+str(se)
            if win==True:
                terminado()
            else:
                time=h+":"+m+":"+s
                timer_display.config(text=time)
                futo.after(1000,reloj)
    ###########################
    #Funcionalidad manejar el timer de fondo
    def timer():
        global win
        global seconds
        global mins
        global hours
        global top
        #Funcionalidad: continuar la partida en caso de que no quiera
        #terminarla cuando el tiempo se acaba
        def timerN():
            global seconds
            global hours
            global mins
            global m2
            global s2
            global h2
            hours=h2
            mins=m2
            seconds=s2
            timerT.destroy()
            reloj()
        #Funcionalidad: cerrar la partida en caso de que quiera
        #terminarla cuando el tiempo se acaba
        def timerS():
            global lvl
            if lvl==0:
                lvl=random.choice([1,2])
            elif lvl==1:
                lvl=random.choice([0,2])
            else:
                lvl=random.choice([0,1])
            timerT.destroy()
            futo.destroy()
        if top==True:
            pass
        else:
            seconds = seconds - 1
            if seconds==-1:
                seconds=59
                mins=mins-1
                if hours>0 and mins==-1:
                    mins=59
                    hours=hours-1
            s = str(seconds)
            m = str(mins)
            h = str(hours)
            if hours < 10:
                h = "0" + str(hours)
            if mins < 10:
                m = "0" + str(mins)
            if seconds < 10:
                s = "0" + str(seconds)
            time=h+":"+m+":"+s
            timer_display.config(text=time)
            if win==True:
                terminado()
            else:
                if hours==0 and mins==0 and seconds==0:
                    messagebox.showinfo("STOP", "El tiempo se ha acabado\nfin de la partida?")
                    timerT=Tk()
                    timerT.geometry("300x300")
                    timerT.resizable(0, 0)
                    timerT.title("Terminar Juego?")
                    timerT.iconbitmap("Metaverse.ico")
                    timerT.configure(bg="black")
                    Label(timerT,text="Terminar Juego",bg="black",fg="white",font=("Trebuchet MS", 18, "bold")).place(x=57,y=30)
                    Yes=Button(timerT,text="Si",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: timerS())
                    Yes.place(x=121,y=120)
                    No=Button(timerT,text="No",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: timerN())
                    No.place(x=121,y=200)
                else:
                    futo.after(1000, timer)
    ###########################
    #Funcionalidad: definir las matrizes del tablero de una partida guardada
    #cuando esta se desea cargar
    def cMatriz(matris):
        global matriz
        global matriz2
        global matriz3
        matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
        matriz2=[["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
        matriz3=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
        for i in matris:
            if i[0]=="<" or i[0]==">":
                matriz2[int(i[1])][int(i[2])]=i[0]
            elif i[0]=="^" or i[0]=="v":
                matriz3[int(i[1])][int(i[2])]=i[0]
            else:
                matriz[int(i[1])][int(i[2])]=int(i[0])
    ###########################
    #Funcionalidad: cargar la partida que se encuentre guardada
    def cargarP():
        global cargada
        global seconds
        global mins
        global hours
        global s2
        global m2
        global h2
        global nombre
        global d
        global r
        global p
        cargada=True
        file=open("futoshiki2020juegoactual.dat","r")
        contenido=file.readlines()
        for i in range (0,len(contenido),1):
            #Ciclo de lectura del archivo
            dato1=contenido[i].find(";")
            valor1=(contenido[i][0:dato1])
            if valor1=="NONE":
                print(valor1)
                messagebox.showinfo("STOP", "No hay partida para cargar")
                i=len(contenido)
            else:
                dato2=contenido[i].find(";",dato1+1)
                dato3=contenido[i].find(";",dato2+1)
                dato4=contenido[i].find(";",dato3+1)
                dato5=contenido[i].find(";",dato4+1)
                valor2=(contenido[i][dato1+1:dato2])
                valor3=(contenido[i][dato2+1:dato3])
                valor4=(contenido[i][dato3+1:dato4])
                valor5=(contenido[i][dato4+1:dato5])
                if valor1=="Timer":
                    dato6=contenido[i].find(";",dato5+1)
                    dato7=contenido[i].find(";",dato6+1)
                    dato8=contenido[i].find(";",dato7+1)
                    dato9=contenido[i].find(";",dato8+1)
                    valor6=(contenido[i][dato5+1:dato6])
                    valor7=(contenido[i][dato6+1:dato7])
                    valor8=(contenido[i][dato7+1:dato8])
                    valor9=(contenido[i][dato8+1:dato9])
                    h2=valor6
                    m2=valor7
                    s2=valor8
                    matri=ast.literal_eval(valor8)
                    nombre=valor9
                elif valor1=="Si":
                    dato6=contenido[i].find(";",dato5+1)
                    valor6=(contenido[i][dato5+1:dato6])
                    matri=ast.literal_eval(valor5)
                    nombre=valor6
                else:
                    matri=ast.literal_eval(valor4)
                    nombre=valor5
                r=valor1
                d=valor2
                p=valor3
                cMatriz(matri)
                if valor1=="Si" or valor1=="Timer":
                    t=list(valor4)
                    if t[0]=="0":
                        hours=int(t[1])
                    else:
                        hours=(int(t[0])*10)+int(t[1])
                    if t[3]=="0":
                        mins=int(t[4])
                    else:
                        mins=(int(t[3])*10)+int(t[4])
                    if t[6]=="0":
                        seconds=int(t[7])
                    else:
                        seconds=(int(t[6])*10)+int(t[7])
        if valor1=="NONE":
            pass
        else:
            futo.destroy()
            juego()
    ###########################
    #Funcionalidad: verificar que las condiciones esten corretas para
    #iniciar
    def comenzar():
        global nombre
        global r
        global ini
        global cargada
        if nombre=="":
            messagebox.showinfo("Antes de empezar...", "Porfavor digite un nombre\nantes de empezar la partida")
        else:
            if r=="Si":
                reloj()
            elif r=="Timer":
                timer()
            else:
                pass
            ini=True
            start.configure(state="disabled")
            borrar.configure(state="normal")
            redo.configure(state="normal")
            terminar.configure(state="normal")
            erase.configure(state="normal")
            topTen.configure(state="normal")
            guardar.configure(state="normal")
            cargar.configure(state="disabled")
    if cargada==False:
        if d2=="Multi Nivel":
            if d=="Facil":
                name=Entry(futo,font=("Trebuchet MS", 12, "bold"))
                name.place(x=488,y=90)
        else:
            name=Entry(futo,font=("Trebuchet MS", 12, "bold"))
            name.place(x=488,y=90)
    ###########################
    #Funcionalidad: definir el nombre y verificar que el nombre dado
    #cumpla con las restricciones
    #Restricciones: el nombre no puede ser mayor a 20 caracteres
    def definirN():
        global nombre
        if name.get()=="":
            messagebox.showinfo("Error", "No se aceptan espacios vacios")
        elif len(list(name.get()))>20:
            messagebox.showinfo("Error", "El nombre no puede ser\nmayor a 20 caracteres")
        else:
            nombre=name.get()
            aceptarN.destroy()
            name.destroy()
            nombres=Label(futo,text=nombre,bg="black",fg="white",font=("Trebuchet MS", 12, "bold"))
            nombres.place(x=480,y=90)
    ###########################
    #Funcionalidad: borrar la ultima jugada realizada
    def borrarJ():
        global matriz
        global jugadas
        global borradas
        if jugadas==[]:
            messagebox.showinfo("Alto", "No hay jugadas que borrar")
        else:
            fila=int(jugadas[0][0])
            columna=int(jugadas[0][1])
            jBorrada=(str(fila),str(columna),matriz[fila][columna])
            borradas=[jBorrada]+borradas
            matriz[fila][columna]=""
            for i in range(len(matriz)):
                for f in range(len(matriz)):
                    boton=listaB[i][f]
                    boton.configure(text=matriz[f][i])
            jugadas=jugadas[1:]
    ###########################
    #Funcionalidad: rehacer la ultima jugada realizada
    def rehacerJ():
        global matriz
        global jugadas
        global borradas
        if borradas==[]:
            messagebox.showinfo("Alto", "No hay jugadas que rehacer")
        else:
            fila=int(borradas[0][0])
            columna=int(borradas[0][1])
            jugadas=[(fila,columna)]+jugadas
            matriz[fila][columna]=borradas[0][2]
            for i in range(len(matriz)):
                for f in range(len(matriz)):
                    boton=listaB[i][f]
                    boton.configure(text=matriz[f][i])
            borradas=borradas[1:]
    ###########################
    #Funcionalidad: borrar el juego entero
    def borrarG():
        global matriz
        #Funcionalidad: cerrar la ventana de opcion y continuar con el juego actual
        def borrarGN():
            brrg.destroy()
        #Funcionalidad: cerrar la ventana de opcion y borrar el juego actual
        def borrarGS():
            global matriz
            global jugadas
            brrg.destroy()
            if jugadas==[]:
                messagebox.showinfo("Alto", "El tablero no tiene jugadas")
            else:
                while jugadas!=[]:
                    fila=int(jugadas[0][0])
                    columna=int(jugadas[0][1])
                    matriz[fila][columna]=""
                    for i in range(len(matriz)):
                        for f in range(len(matriz)):
                            boton=listaB[i][f]
                            boton.configure(text=matriz[f][i])
                    jugadas=jugadas[1:]
        brrg=Tk()
        brrg.geometry("300x300")
        brrg.resizable(0, 0)
        brrg.title("Borrar Juego?")
        brrg.iconbitmap("Metaverse.ico")
        brrg.configure(bg="black")
        Label(brrg,text="Borrar Juego",bg="black",fg="white",font=("Trebuchet MS", 18, "bold")).place(x=75,y=30)
        Yes=Button(brrg,text="Si",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: borrarGS())
        Yes.place(x=121,y=120)
        No=Button(brrg,text="No",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: borrarGN())
        No.place(x=121,y=200)
    ###########################
    #Funcionalidad: terminar la partida por completo
    def finishG():
        #Funcionalidad: cerrar la ventana de opcion y no terminar el juego actual
        def finishGN():
            finish.destroy()
        #Funcionalidad: cerrar la ventana de opcion y terminar el juego actual
        def finishGS():
            global lvl
            if lvl==0:
                lvl=random.choice([1,2])
            elif lvl==1:
                lvl=random.choice([0,2])
            else:
                lvl=random.choice([0,1])
            finish.destroy()
            futo.destroy()
            juego()
        finish=Tk()
        finish.geometry("300x300")
        finish.resizable(0, 0)
        finish.title("Terminar Juego?")
        finish.iconbitmap("Metaverse.ico")
        finish.configure(bg="black")
        Label(finish,text="Terminar Juego",bg="black",fg="white",font=("Trebuchet MS", 18, "bold")).place(x=57,y=30)
        Yes=Button(finish,text="Si",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: finishGS())
        Yes.place(x=121,y=120)
        No=Button(finish,text="No",width=5,font=("Trebuchet MS", 12, "bold"),command=lambda: finishGN())
        No.place(x=121,y=200)
    ###########################
    #Funcionalidad: calcular los tiempos par definir cuales fueron los
    #mas rapidos para el top 10
    def calc_tiempo(l):
        suma=0
        result=[]
        for i in range(len(l)):
            tiemp=list(l[i])
            if tiemp[0]=="0":
                suma=suma+((int(tiemp[1]))*100)
            else:
                suma=suma+((int(tiemp[0])*100)+(int(tiemp[1]))*100)
            if tiemp[3]=="0":
                suma=suma+(int(tiemp[4])*10)
            else:
                suma=suma+((int(tiemp[3])*10)+(int(tiemp[4]))*10)
            if tiemp[6]=="0":
                suma=suma+int(tiemp[7])
            else:
                suma=suma+(int(tiemp[6])+int(tiemp[7]))
            result=result+[suma]
            suma=0
        return result
    ###########################
    #Funcionalidad: guardar la partida actual
    def guardarP():
        global r
        global d
        global p
        global seconds
        global mins
        global hours
        global nombre
        global m2
        global s2
        global h3
        global matriz
        global matriz2
        global matriz3
        if seconds<10:
            strS="0"+str(seconds)
        else:
            strS=str(seconds)
        if mins<10:
            strM="0"+str(mins)
        else:
            strM=str(mins)
        if hours<10:
            strH="0"+str(hours)
        else:
            strH=str(hours)
        cuadricula=[]
        for i in range(len(matriz)):
            for f in range(len(matriz)):
                if matriz[i][f]!="":
                    cuadricula=cuadricula+[(matriz[i][f],int(i),int(f))]
                if matriz3[i][f]!="":
                    cuadricula=cuadricula+[(matriz3[i][f],int(i),int(f))]
        for i in range(len(matriz2)):
            for f in range(len(matriz2[0])):
                if matriz2[i][f]!="":
                    cuadricula=cuadricula+[(matriz2[i][f],int(i),int(f))]
                
        strTiempo=strH+":"+strM+":"+strS
        if r=="Si":
            string=str(r)+";"+str(d)+";"+str(p)+";"+strTiempo+";"+str(cuadricula)+";"+str(nombre)
        elif r=="No":
            string=str(r)+";"+str(d)+";"+str(p)+";"+str(cuadricula)+";"+str(nombre)
        else:
            string=str(r)+";"+str(d)+";"+str(p)+";"+strTiempo+";"+str(h2)+";"+str(m2)+";"+str(s2)+";"+str(cuadricula)+";"+str(nombre)
        file=open("futoshiki2020juegoactual.dat","w")
        file.write(string)
        file.close()
        file=open("futoshiki2020juegoactual.dat","a")
        file.close()
    ###########################
    #Funcionalidad: ordenar los top jugadores de cada lista pra pasar
    #a desplegarlos
    def ordenTop(nombres,tiempos,sumas):
        result=[]
        while sumas!=[]:
            s=""
            for i in range(len(sumas)):
                if sumas[i]==min(sumas):
                    s=i
            if len(result)<10:
                result=result+[(nombres[s],tiempos[s])]
            del nombres[s]
            del tiempos[s]
            del sumas[s]
        return result
    ###########################
    #Funcionalidad: crear el pdf del top 10
    def pdf(TOPF, TOPN, TOPD, TOPM):
        global nombre
        nombrepdf=nombre+" Top10.pdf"
        pdfmetrics.registerFont(TTFont('GOTHIC', 'GOTHIC.ttf'))
        pdfmetrics.registerFont(TTFont('GOTHICB', 'GOTHICB.ttf'))
        c=canvas.Canvas(nombrepdf,pagesize=(810, 500))
        c.setFont("GOTHICB", 40, leading=None)
        c.drawString(225, 450, "Top 10 FutoshikiV2")
        c.setFont("GOTHICB", 30, leading=None)
        c.drawString(70, 380, "Facil")
        c.drawString(250, 380, "Normal")
        c.drawString(465, 380, "Dificil")
        c.drawString(630, 380, "Multi Nivel")
        c.setFont("GOTHICB", 20, leading=None)
        c.drawString(20, 350, "Nombre")
        c.drawString(220, 350, "Nombre")
        c.drawString(420, 350, "Nombre")
        c.drawString(620, 350, "Nombre")
        c.drawString(120, 350, "Tiempo")
        c.drawString(320, 350, "Tiempo")
        c.drawString(520, 350, "Tiempo")
        c.drawString(720, 350, "Tiempo")
        c.setFont("GOTHIC", 12, leading=None)
        columna=320
        n=1
        for i in TOPF:
            string1=str(n)+". "+str(i[0])
            string2=i[1]
            c.drawString(20, columna, string1)
            c.drawString(120, columna, string2)
            columna=columna-20
            n=n+1
        columna=320
        n=1
        for i in TOPN:
            string1=str(n)+". "+str(i[0])
            string2=i[1]
            c.drawString(220, columna, string1)
            c.drawString(320, columna, string2)
            columna=columna-20
            n=n+1
        columna=320
        n=1
        for i in TOPD:
            string1=str(n)+". "+str(i[0])
            string2=i[1]
            c.drawString(420, columna, string1)
            c.drawString(520, columna, string2)
            columna=columna-20
            n=n+1
        columna=320
        n=1
        for i in TOPM:
            string1=str(n)+". "+str(i[0])
            string2=i[1]
            c.drawString(620, columna, string1)
            c.drawString(720, columna, string2)
            columna=columna-20
            n=n+1
        c.showPage()
        c.save()
        messagebox.showinfo("Listo", "Se ha creado una tabla\ncon el top 10 para visualizar\n \nEn caso de querer imprimirla\nun PDF ha sido creado con su\nnombre en la carpeta del programa")
    ###########################
    #Funcionalidad: crear la ventana de top 10 jugadores de
    #cada dificultad
    def top_ten():
        global top
        #Funcionalidad: cerrar la ventan del tiempo y resumir el reloj/timer
        def salirTop():
            global top
            global r
            top=False
            if r=="Si":
                reloj()
            elif r=="Timer":
                timer()
            topt.destroy()
        listaNF=[]
        listaTF=[]
        listaNN=[]
        listaTN=[]
        listaND=[]
        listaTD=[]
        listaNM=[]
        listaTM=[]
        file=open("futoshiki2020top10.dat","r")
        contenido=file.readlines()
        for z in range (0,len(contenido),1):
            dato1=contenido[z].find(";")
            dato2=contenido[z].find(";",dato1+1)
            dato3=contenido[z].find(";",dato2+1)
            valor1=(contenido[z][0:dato1])
            valor2=(contenido[z][dato1+1:dato2])
            valor3=(contenido[z][dato2+1:dato3])
            if valor3=="Facil":
                listaNF=listaNF+[valor1]
                listaTF=listaTF+[valor2]
            elif valor3=="Normal":
                listaNN=listaNN+[valor1]
                listaTN=listaTN+[valor2]
            elif valor3=="Dificil":
                listaND=listaND+[valor1]
                listaTD=listaTD+[valor2]
            else:
                listaNM=listaNM+[valor1]
                listaTM=listaTM+[valor2]
        file.close()
        top=True
        tiemposF=calc_tiempo(listaTF)
        tiemposN=calc_tiempo(listaTN)
        tiemposD=calc_tiempo(listaTD)
        tiemposM=calc_tiempo(listaTM)
        TOPF=ordenTop(listaNF,listaTF,tiemposF)
        TOPN=ordenTop(listaNN,listaTN,tiemposN)
        TOPD=ordenTop(listaND,listaTD,tiemposD)
        TOPM=ordenTop(listaNM,listaTM,tiemposM)
        topt=Tk()
        topt.geometry("820x500")
        topt.iconbitmap("Metaverse.ico")
        topt.configure(bg="black")
        topt.title("Top 10")
        topt.resizable(0, 0)
        botonSalir=Button(topt,text="Salir",bg="grey",activebackground="grey",relief=RAISED,font=("Trebuchet MS", 18, "bold"),command=lambda:salirTop())
        botonSalir.place(x=375,y=420)
        Label(topt,text="Top 10 Facil",fg="green",bg="black",font=("Trebuchet MS", 17, "bold")).place(x=50,y=20)
        Label(topt,text="Top 10 Normal",fg="green",bg="black",font=("Trebuchet MS", 17, "bold")).place(x=215,y=20)
        Label(topt,text="Top 10 Dificil",fg="green",bg="black",font=("Trebuchet MS", 17, "bold")).place(x=400,y=20)
        Label(topt,text="Top 10 Multi Nivel",fg="green",bg="black",font=("Trebuchet MS", 17, "bold")).place(x=585,y=20)
        Label(topt,text="Tiempo",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=130,y=50)
        Label(topt,text="Tiempo",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=290,y=50)
        Label(topt,text="Tiempo",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=480,y=50)
        Label(topt,text="Tiempo",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=670,y=50)
        Label(topt,text="Nombre",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=50,y=50)
        Label(topt,text="Nombre",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=215,y=50)
        Label(topt,text="Nombre",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=400,y=50)
        Label(topt,text="Nombre",fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=585,y=50)
        column=80
        for i in TOPF:
            string1=str(i[0])
            string2=str(i[1])
            Label(topt,text=string1,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=50,y=column)
            Label(topt,text=string2,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=130,y=column)
            column=column+30
        column=80
        for i in TOPN:
            string1=str(i[0])
            string2=str(i[1])
            Label(topt,text=string1,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=215,y=column)
            Label(topt,text=string2,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=290,y=column)
            column=column+30
        column=80
        for i in TOPD:
            string1=str(i[0])
            string2=str(i[1])
            Label(topt,text=string1,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=400,y=column)
            Label(topt,text=string2,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=480,y=column)
            column=column+30
        column=80
        for i in TOPM:
            string1=str(i[0])
            string2=str(i[1])
            Label(topt,text=string1,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=585,y=column)
            Label(topt,text=string2,fg="green",bg="black",font=("Trebuchet MS", 10, "bold")).place(x=670,y=column)
            column=column+30
        pdf(TOPF, TOPN, TOPD, TOPM)
    ###########################
    if cargada==False:
        if d2=="Multi Nivel":
            if d=="Facil":
                Label(futo,text="Nombre:",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=392,y=90)
                aceptarN=Button(futo,text="Aceptar",relief=RAISED,bg="red",activebackground="red",command=lambda:definirN())
                aceptarN.place(x=700,y=90)
            else:
                Label(futo,text="Nombre:",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=392,y=90)
                nombres=Label(futo,text=nombre,bg="black",fg="white",font=("Trebuchet MS", 12, "bold"))
                nombres.place(x=480,y=90)
        else:
            Label(futo,text="Nombre:",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=392,y=90)
            aceptarN=Button(futo,text="Aceptar",relief=RAISED,bg="red",activebackground="red",command=lambda:definirN())
            aceptarN.place(x=700,y=90)
    else:
        Label(futo,text="Nombre:",bg="black",fg="white",font=("Trebuchet MS", 12, "bold")).place(x=392,y=90)
        nombres=Label(futo,text=nombre,bg="black",fg="white",font=("Trebuchet MS", 12, "bold"))
        nombres.place(x=480,y=90)
    #Botones del tablero de juego
    Label(futo,text="FUTOSHIKI",bg="red",relief=RAISED,font=("Trebuchet MS", 30, "bold italic")).place(x=397,y=15)
    if d2=="Multi Nivel":
        Label(futo,text=str(d2)+" "+str(d),bg="red",relief=RAISED,font=("Trebuchet MS", 15, "bold italic")).place(x=620,y=25)
    else:
        Label(futo,text=str(d),bg="red",relief=RAISED,font=("Trebuchet MS", 15, "bold italic")).place(x=620,y=25)
    borrar=Button(futo,state="disabled",height=2,width=10,text="Borrar\nJugada",activebackground="turquoise",bg="turquoise",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda: borrarJ())
    borrar.place(x=340,y=700)
    redo=Button(futo,state="disabled",height=2,width=10,text="Rehacer\nJugada",activebackground="green",bg="green",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda: rehacerJ())
    redo.place(x=450,y=700)
    terminar=Button(futo,state="disabled",height=2,width=10,text="Terminar\nJuego",activebackground="red",bg="red",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda: finishG())
    terminar.place(x=268,y=60)
    erase=Button(futo,state="disabled",height=2,width=10,text="Borrar\nJuego",activebackground="light blue",bg="light blue",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda: borrarG())
    erase.place(x=560,y=700)
    topTen=Button(futo,state="disabled",height=2,width=10,text="Top\n10",activebackground="yellow",bg="yellow",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda:top_ten())
    topTen.place(x=670,y=700)
    guardar=Button(futo,state="disabled",height=1,width=15,text="Guardar Partida",activebackground="grey",bg="light grey",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda:guardarP())
    guardar.place(x=817,y=689)
    cargar=Button(futo,height=1,width=15,text="Cargar Partida",activebackground="grey",bg="light grey",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda:cargarP())
    cargar.place(x=817,y=730)  
    start=Button(futo,height=2,width=10,text="Iniciar\nJuego",activebackground="magenta",bg="magenta",relief=RAISED,font=("Trebuchet MS", 12, "bold"),command=lambda: comenzar())
    start.place(x=230,y=700)
    ###########################
    #Funcionalidad: verificar que la opcion que se quiere poner
    #en el tablero sea valida
    def jugada(boton):
        global win
        global opcion
        global jugadas
        global matriz
        global matriz2
        global matriz3
        global d
        global d2
        if opcion=="":
            pass
        else:
            if boton["text"]!="":
                pass
            else:
                check=int(opcion)
                columna=0
                fila=0
                for i in range(len(matriz)):
                    for f in range(len(matriz[i])):
                        if boton==listaB[i][f]:
                            columna=i
                            fila=f
                        else:
                            pass
                repeatF=False
                repeatC=False
                for i in range(len(matriz)):
                    if i==columna:
                        pass
                    elif str(matriz[fila][i])==opcion:
                        repeatF=True
                for i in range(len(matriz)):
                    if i==fila:
                        pass
                    elif str(matriz[i][columna])==opcion:
                        repeatC=True
                checkMF=False
                checkMC=False
                errorv=""
                ###########################
                #Validaciones de las esquinas
                if fila==0 and columna==0:
                    valid=matriz2[0][0]
                    if matriz[0][1]!="":
                        if valid==">":
                            if check<int(matriz[0][1]):
                                checkMF=True
                                errorv="mayor"
                        elif valid=="<":
                            if check>int(matriz[0][1]):
                                checkMF=True
                                errorv="menor"
                    valid=matriz3[0][0]
                    if matriz[1][0]!="":
                        if valid=="^":
                            if check>int(matriz[1][0]):
                                checkMC=True
                                errorv="menor"
                        elif valid=="v":
                            if check<int(matriz[1][0]):
                                checkMC=True
                                errorv="mayor"
                ###########################
                elif fila==0 and columna==4:
                    valid=matriz2[0][3]
                    if matriz[0][3]!="":
                        if valid==">":
                            if check>int(matriz[0][3]):
                                checkMF=True
                                errorv="menor"
                        elif valid=="<":
                            if check<int(matriz[0][3]):
                                checkMF=True
                                errorv="mayor"
                    valid=matriz3[0][4]
                    if matriz[1][4]!="":
                        if valid=="^":
                            if check>int(matriz[1][4]):
                                checkMC=True
                                errorv="menor"
                        elif valid=="v":
                            if check<int(matriz[1][4]):
                                checkMC=True
                                errorv="mayor"
                ###########################
                elif fila==4 and columna==0:
                    valid=matriz2[4][0]
                    if matriz[4][1]!="":
                        if valid==">":
                            if check<int(matriz[4][1]):
                                checkMF=True
                                errorv="mayor"
                        elif valid=="<":
                            if check>int(matriz[4][1]):
                                checkMF=True
                                errorv="menor"
                    valid=matriz3[3][0]
                    if matriz[3][0]!="":
                        if valid=="^":
                            if check<int(matriz[3][0]):
                                checkMC=True
                                errorv="mayor"
                        elif valid=="v":
                            if check>int(matriz[3][0]):
                                checkMC=True
                                errorv="menor"
                ###########################
                elif fila==4 and columna==4:
                    valid=matriz2[4][3]
                    if matriz[4][3]!="":
                        if valid==">":
                            if check>int(matriz[4][3]):
                                checkMF=True
                                errorv="menor"
                        elif valid=="<":
                            if check<int(matriz[4][3]):
                                checkMF=True
                                errorv="mayor"
                    valid=matriz3[3][4]
                    if matriz[3][4]!="":
                        if valid=="^":
                            if check<int(matriz[3][4]):
                                checkMC=True
                                errorv="mayor"
                        elif valid=="v":
                            if check>int(matriz[3][4]):
                                checkMC=True
                                errorv="menor"
                ###########################
                #Validaciones de la primera y ultima fila
                elif fila==0 or fila==4:
                    valid=matriz2[fila][columna]
                    if matriz[fila][columna+1]!="":
                        if valid==">":
                            if check<int(matriz[fila][columna+1]):
                                checkMF=True
                                errorv="mayor"
                        elif valid=="<":
                            if check>int(matriz[fila][columna+1]):
                                checkMF=True
                                errorv="menor"
                    valid=matriz2[fila][columna-1]
                    if matriz[fila][columna-1]!="":
                        if valid==">":
                            if check>int(matriz[fila][columna-1]):
                                checkMF=True
                                errorv="menor"
                        elif valid=="<":
                            if check<int(matriz[fila][columna-1]):
                                checkMF=True
                                errorv="maoyr"
                    if fila==0:
                        valid=matriz3[fila][columna]
                        if matriz[fila+1][columna]!="":
                            if valid=="^":
                                if check>int(matriz[fila+1][columna]):
                                    checkMC=True
                                    errorv="menor"
                            elif valid=="v":
                                if check<int(matriz[fila+1][columna]):
                                    checkMC=True
                                    errorv="mayor"
                    else:
                        valid=matriz3[fila-1][columna]
                        if matriz[fila-1][columna]!="":
                            if valid=="^":
                                if check<int(matriz[fila-1][columna]):
                                    checkMC=True
                                    errorv="mayor"
                            elif valid=="v":
                                if check>int(matriz[fila-1][columna]):
                                    checkMC=True
                                    errorv="menor"
                ###########################
                #Validacion de la primera y ultima columna
                elif columna==0 or columna==4:
                    if columna==0:
                        valid=matriz2[fila][columna]
                        if matriz[fila][columna+1]!="":
                            if valid==">":
                                if check<int(matriz[fila][columna+1]):
                                    checkMF=True
                                    errorv="mayor"
                            elif valid=="<":
                                if check>int(matriz[fila][columna+1]):
                                    checkMF=True
                                    errorv="menor"
                    else:
                        valid=matriz2[fila][columna-1]
                        if matriz[fila][columna-1]!="":
                            if valid==">":
                                if check>int(matriz[fila][columna-1]):
                                    checkMF=True
                                    errorv="mayor"
                            elif valid=="<":
                                if check<int(matriz[fila][columna-1]):
                                    checkMF=True
                                    errorv="menor"
                    valid=matriz3[fila][columna]
                    if matriz[fila+1][columna]!="":
                        if valid=="^":
                            if check>int(matriz[fila+1][columna]):
                                checkMC=True
                                errorv="menor"
                        elif valid=="v":
                            if check<int(matriz[fila+1][columna]):
                                checkMF=True
                                errorv="mayor"
                    valid=matriz3[fila-1][columna]
                    if matriz[fila-1][columna]!="":
                        if valid=="^":
                            if check<int(matriz[fila-1][columna]):
                                checkMC=True
                                errorv="mayor"
                        elif valid=="v":
                            if check>int(matriz[fila-1][columna]):
                                checkMF=True
                                errorv="menor"
                ###########################
                #Validacion del resto del tablero
                else:
                    valid=matriz2[fila][columna]
                    if matriz[fila][columna+1]!="":
                        if valid==">":
                            if check<int(matriz[fila][columna+1]):
                                checkMF=True
                                errorv="mayor"
                        elif valid=="<":
                            if check>int(matriz[fila][columna+1]):
                                checkMF=True
                                errorv="menor"
                    valid=matriz2[fila][columna-1]
                    if matriz[fila][columna-1]!="":
                        if valid==">":
                            if check>int(matriz[fila][columna-1]):
                                checkMF=True
                                errorv="menor"
                        elif valid=="<":
                            if check<int(matriz[fila][columna-1]):
                                checkMF=True
                                errorv="mayor"
                    valid=matriz3[fila][columna]
                    if matriz[fila+1][columna]!="":
                        if valid=="^":
                            if check>int(matriz[fila+1][columna]):
                                checkMC=True
                                errorv="menor"
                        elif valid=="v":
                            if check<int(matriz[fila+1][columna]):
                                checkMF=True
                                errorv="mayor"
                    valid=matriz3[fila-1][columna]
                    if matriz[fila-1][columna]!="":
                        if valid=="^":
                            if check<int(matriz[fila-1][columna]):
                                checkMC=True
                                errorv="mayor"
                        elif valid=="v":
                            if check>int(matriz[fila-1][columna]):
                                checkMF=True
                                errorv="menor"
                ###########################
                #Checkeo de validaciones para poner la opcion en el tablero
                if repeatF==True:
                    messagebox.showinfo("Alto", "Ese valor ya se\nencuentra en la fila")
                elif repeatC==True:
                    messagebox.showinfo("Alto", "Ese valor ya se\nencuentra en la columna")
                elif checkMF==True or checkMC==True:
                    if errorv=="mayor":
                        messagebox.showinfo("Alto", "Ese valor no cumple\ncon la restriccion mayor")
                    else:
                        messagebox.showinfo("Alto", "Ese valor no cumple\ncon la restriccion menor")
                else:
                    matriz[fila][columna]=str(opcion)
                    boton.configure(text=opcion)
                    jugadas=[(fila,columna)]+jugadas
                    vacio=False
                    for i in range(len(matriz)):
                        for f in range(len(matriz)):
                            if matriz[i][f]=="":
                                vacio=True
                    if vacio==False:
                        win=True
                    if win==True:
                        if d2=="Multi Nivel":
                            if d=="Dificil":
                                terminado()
                            else:
                                nextLevel()
                        else:
                            terminado()
    ###########################
    #Creacion de botones
    fila=268
    columna=150
    lista=[]
    listaB=[]
    for i in range(0,5):
        for f in range(0,5):
            Boton=Button(futo,text=matriz[f][i],width=6,height=2,background="grey", activebackground="grey",font=("Trebuchet MS", 12, "bold"))
            Boton.configure(command=lambda button=Boton:jugada(button))
            Boton.place(x=fila,y=columna)
            columna=columna+100
            lista=lista+[Boton]
        listaB=listaB+[lista]
        lista=[]
        columna=150
        fila=fila+100
    fila=337
    columna=165
    #Creacion de las casillas con los valores <,>,^ o v
    for i in range(0,4):
        for f in range(0,5):
            Texto=Label(futo,text=matriz2[f][i],background="black",foreground="white",font=("Trebuchet MS", 15, "bold"))
            Texto.place(x=fila,y=columna)
            columna=columna+100
        columna=165
        fila=fila+100
    fila=291
    columna=210
    for i in range(0,5):
        for f in range(0,4):
            Texto=Label(futo,text=matriz3[f][i],background="black",foreground="white",font=("Trebuchet MS", 15, "bold"))
            Texto.place(x=fila,y=columna)
            columna=columna+100
        columna=210
        fila=fila+100
    cargada=False
    futo.mainloop()
    ###########################
iniciar=Button(inicio,state="disabled",text="Jugar",background="green",activebackground="green",relief=GROOVE,font=("Trebuchet MS", 17, "bold"),command=lambda: juego())
iniciar.place(x=104.4, y=50)
#Inicio del programa principal
inicio.mainloop()
