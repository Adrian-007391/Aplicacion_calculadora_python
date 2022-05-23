from tkinter import *
# root 
root = Tk()
root.title("Calculator")
# canvas (background azul)
canvas = Canvas(root , bg = "#1b355e", width=300, height= 450)
# barra de display de la operacion
frame = Frame(root , bg = "#cfcdcc")
frame.place(relheight=0.1 , relwidth=0.8, relx =0.1, y = 50)

# funcion para agregar los numeros de los botones a la barra de arriba 
txt = ""
def addtoinput(param):
    global txt 
    txt = txt + param
    for i in frame.winfo_children():
        i.destroy()
    l = Label(frame , text = txt , font=("Arial",20), bg ="#cfcdcc", fg = "#1b355e")
    l.pack()
# botones de los numeros 
x = 0
for j in range(1,4):
    for i in range(1,4):
        num = x+i
        a=Button(canvas , text=str(x+i),command= lambda n=num:addtoinput(str(n)))
        a.place(width=50 , height= 50, relx= (i/5)-0.1 , rely= (0.3+j)/5)
    x=x+3

# botones de los operadores 
operadores = ["+","-","*","/"]

for i in range(0,4):
        num = operadores[i]
        a=Button(canvas , text=num,command= lambda n=num:addtoinput(n))
        a.place(width=50 , height= 50, relx= 0.7 , rely= (i+1.4)/6)

# funcion para resolver la operacion 
def makeoperation():
    global txt
    operacion =eval(txt)
    txt = ""
    addtoinput(str(operacion))

# Boton de igual     

equal = Button(canvas , text="=", command = makeoperation)
equal.place(width=100 , height = 50, relx = 0.2 , rely = 0.8)


canvas.pack()
root.mainloop()
