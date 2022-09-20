from tkinter import*
import os

window = Tk()
window.title("Feu tricolor")


canvas = Canvas(window , height=800 , width=700 , bg="grey")
canvas.grid(row=0 , column=0)

#label Feu de circulation
labtitre = Label(window , text="feu de circulation", bg="grey",fg = "yellow",font=('Times-New-Roman',25))
labtitre.place(x=200 , y=20)


#creation de l'oval
red= StringVar()
yellow= StringVar()
green = StringVar()
red = canvas.create_oval(60,80,120,140, fill="black")
yellow = canvas.create_oval(60,160,120,220, fill="black")
green = canvas.create_oval(60,240,120,300, fill="black")


#initialisation rouge
canvas.itemconfigure(red , fill="red")

#label Commande manuelle
labCommande = Label(window , text="Commande manuelle", bg="grey",fg = "white",font=('Times-New-Roman',15))
labCommande.place(x=500 , y=110)


#Creation boutton : precedent, suivant ,reintialiser et passer dans le niveau3
Button(window, text="PRECEDENT" , bg="green",fg = "white", command=lambda: precedent()).place(x=600 , y=150)
Button(window, text="SUIVANT" , bg="blue",fg = "white", command=lambda: suivant()).place(x=600 , y=190)
Button(window, text="REINITIALISER" , bg="tan",fg = "white", command=lambda: reset_values()).place(x=600 , y=230)
Button(window, text="QUITTER" , bg="red",fg = "white", command=lambda: Quitter()).place(x=200 , y=400)

def niveau1_2():
            window.destroy()
            os.popen('python pythonNiveau3.py')
           
Button(window, text="PASSER AU NIVEAU3" , bg="yellow",fg = "black", command=lambda: niveau1_2()).place(x=300 , y=400)




#Creation d'option : automatique ou manuel
j = StringVar()
labOption = Label(window , text=' Option :', bg="grey",fg = "white",font=('Times-New-Roman',15))
labOption.place(x=200 , y=110)
auto = Radiobutton(window , text='Automatique' , bg="grey", variable=j , value='auto' , command=lambda: getValue(j.get()))
auto.place(x=300 , y=120)
manuel = Radiobutton(window, text="Manuelle", bg="grey", variable=j , value="manuel" ,  command=lambda: getValue(j.get()))
manuel.place(x=300 , y=140)



#Creation  choix de vitesse : tres lent ,lent,  normal, rapide ou tres rapide
vitesse= StringVar()
labVitesse = Label(window , text=' Vitesse :', bg="grey",fg = "white",font=('Times-New-Roman',15))
labVitesse.place(x=200 , y=220)
#très lent
trLent = Radiobutton(window , text='très lent' , bg="grey", variable=vitesse , value='trLent' ,font=('Times-New-Roman',10),command=lambda: getValue(vitesse.get()))
trLent.place(x=400 , y=250)
#lent
lent = Radiobutton(window , text='lent', bg="grey" , variable=vitesse , value='Lent' ,font=('Times-New-Roman',10), command=lambda: getValue(vitesse.get()))
lent.place(x=300 , y=250)
#normal
normal = Radiobutton(window , text='normal', bg="grey" , variable=vitesse , value='normal' , font=('Times-New-Roman',10), command=lambda: getValue(vitesse.get()))
normal.place(x=300 , y=290)
#rapide 
rapide = Radiobutton(window , text='rapide' , bg="grey", variable=vitesse , value='rapide' , font=('Times-New-Roman',10),command=lambda: getValue(vitesse.get()))
rapide.place(x=300 , y=270)
#très rapide
trRapide = Radiobutton(window , text='très rapide', bg="grey" , variable=vitesse , value='très rapide' ,font=('Times-New-Roman',10), command=lambda: getValue(vitesse.get()))
trRapide.place(x=400 , y=270)




#fonction suivant
def suivant():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black")
        
    elif canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   

    elif canvas.itemcget(red,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")   



#fonction precedent
def precedent():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black") 
        
 
 #fonction tres rapide       
def tresRapide():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="green")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")     
     
    window.after(800,tresRapide)

#fonction rapide 
def Rapide():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
    
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")       
            
    window.after(300,Rapide)
    
#fonction normal
def normal():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")  
        
    window.after(2000,normal)     
    
#fonction lent    
def Lent():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")  
        
    window.after(5000,Lent)     
    
          
 #fonction tres lent   
def tresLent():
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black")
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")  
        
    window.after(10000,tresLent)     
    
   
 #fonction quitter   
def Quitter():
    window.destroy()
    
#fonction reinitialiser 
def reset_values():
    j.set('0')
    vitesse.set('0')
    red.set('0')
    yellow.set('0')
    green.set('0')
    
 #fonction option automatique et manuel  
def automatique():
    global choix
    if canvas.itemcget(red,'fill') == 'red':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="yellow")
        canvas.itemconfigure(green, fill="black") 
        
    elif  canvas.itemcget(yellow,'fill') == 'yellow':
        canvas.itemconfigure(red, fill="black")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="green")   
  
    elif  canvas.itemcget(green,'fill') == 'green':
        canvas.itemconfigure(red, fill="red")
        canvas.itemconfigure(yellow, fill="black")
        canvas.itemconfigure(green, fill="black")  
        
    choix= window.after(2000,automatique)    
    
    
#fonction d'arret pour passer dans une autre option     
def stop():
    global choix
    window.after_cancel(choix)
    
def getValue(a):
    if a == 'auto':
        automatique()
    elif a == 'manuel':
        stop()
   
        
def getVitesse(vt):
    a = 'wxx'
    getValue(a)
    if vt == 'trlent':
        tresLent()
    elif vt == 'lent':
        Lent()
    elif vt == 'normal':
        normal()
    elif vt == 'rapide':
        Rapide()
    elif vt == 'tresrapide':
        tresRapide()   
        
        

window.mainloop()                                        
         