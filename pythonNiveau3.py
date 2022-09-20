from tkinter import *
import time
import os


noir="black"
rouge1="red"
vert1="green"
jaune1="yellow"

class progressBar(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.labtitre=Label(self,text="CONTROLEUR DE FEU DE CIRCULATION",bg="grey",fg = "yellow",font=('Times-New-Roman',25))
        self.labtitre.place(relx=0.2, rely=0)
        
       #label nom 
        self.labNom=Label(self,text="CONTROLEUR DE ",bg="grey",fg = "yellow",font=('Times-New-Roman',25))
        self.labNom.place(relx=0.2, rely=0)
        
        
        self.labColeur=Label(self,text="COULEUR",bg="grey",fg = "white",font=('Times-New-Roman',10))
        self.labColeur.place(relx=0.5, rely=0.30)
        
        self.labColeur=Label(self,text="VITESSE",bg="grey",fg = "white",font=('Times-New-Roman',10))
        self.labColeur.place(relx=0.61, rely=0.30)
        
        self.labColeur=Label(self,text="DUREE",bg="grey",fg = "white",font=('Times-New-Roman',10))
        self.labColeur.place(relx=0.8, rely=0.30)
        
        self.labColeur=Label(self,text="FEU TRICOLOR",bg="grey",fg = "white",font=('Times-New-Roman',10))
        self.labColeur.place(relx=0.10, rely=0.30)
        
        
        self.coleur = "red"
        self.dure = 0
        
        self.green = Label(self, text="vert",bg="grey" ,font=('Times-New-Roman',15))
        self.yellow = Label(self, text="jaune",bg="grey",font=('Times-New-Roman',15))
        self.red = Label(self, text="rouge",bg="grey",font=('Times-New-Roman',15))
        
        
        self.green.place(relx=0.5, rely=0.35) 
        self.yellow.place(relx=0.5, rely=0.45)
        self.red.place(relx=0.5, rely=0.55)
        
        #scale (controleur)
        self.g = Scale(self, from_=10, to=0, orient="horizontal",bg="green", length=120)
        self.y = Scale(self, from_=10, to=0, orient="horizontal",bg="yellow", length=120)
        self.r = Scale(self, from_=10, to=0, orient="horizontal",bg="red", length=120)
        
        
        self.g.place(relx=0.6, rely=0.35)
        self.y.place(relx=0.6, rely=0.45)
        self.r.place(relx=0.6, rely=0.55)
        
        #label vitesse
        self.lab1 = Label(self, text="vitess:",bg="grey")
        self.lab2 = Label(self, text="vitess",bg="grey")
        self.lab3 = Label(self, text="vitess",bg="grey")
        
        self.lab1.place(relx=0.8, rely=0.35)
        self.lab2.place(relx=0.8, rely=0.45)
        self.lab3.place(relx=0.8, rely=0.55)
    
        self.changer()
        
        
        Button(self, text="QUITTER", bg="red",font = ("Helvatica", 10), command=lambda: app.quit()).place(x=600 , y=500)
        def niveau3():
            self.destroy()
            os.popen('python pythonNiveau1_2.py')
        Button(self, text="PASSER AU NIVEAU 1 et 2", bg="yellow",font = ("Helvatica", 10), command=lambda: niveau3()).place(x=700 , y=500)


    def creer(self,y,couleur,defaut):
        self.toile = Canvas(self, width=150, height=150,bg="grey")  # Même taille que le conteneur
        self.toile.place(relx=0.2, rely=y)

        self.toile.create_oval(60,80,120,140, width=1, fill=couleur, outline=defaut)
        


    def changer(self):
        self.final_g = 10000 - (int(self.g.get()) * 1000)
        self.final_y = (10000 - (int(self.y.get()) * 1000))
        self.final_r = 10000 - (int(self.r.get()) * 1000)

        self.lab1["text"] = "durée :" + str(self.final_g) +"s"
        self.lab2["text"] = "durée :" + str(self.final_y) +"s"
        self.lab3["text"] = "durée :" + str(self.final_r) +"s"

        print("vert",self.final_g, "jaune",self.final_y,"rouge",self.final_r)
        second = time.strftime("%S")
        self.lab = Label(self, text="blabla")
        self.lab.place(relx=0.2, rely=0.4)
        self.lab.config(text=second)

        if (self.coleur == "red"):
            self.coleur = "green"
            self.dure = self.final_g
            print(self.coleur,self.dure)
            self.creer(0.35, self.coleur, self.coleur)
            self.creer(0.55, noir, jaune1)
            self.creer(0.75, noir, rouge1)

        elif (self.coleur == "green"):
            self.coleur = "yellow"
            self.dure = self.final_y
            print(self.coleur,self.dure)
            self.creer(0.35, noir, vert1)
            self.creer(0.55, self.coleur, self.coleur)
            self.creer(0.75, noir, rouge1)


        else:
            self.coleur = "red"
            self.dure = self.final_r
            print(self.coleur,self.dure)
            self.creer(0.35, noir, vert1)
            self.creer(0.55, noir, jaune1)
            self.creer(0.75, self.coleur, rouge1)
        self.lab.after(self.dure,lambda : self.changer())


app = progressBar()
app.geometry("1100x720")
app.configure(bg="grey")
app.mainloop()