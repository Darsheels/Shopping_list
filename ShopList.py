import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import math
import random 

conn = sqlite3.connect('Data\\Store_Userfile.db')



window = tk.Tk()
window.geometry("800x500")
window.title('QuickCart')


class Start():

    def __init__(self):
        self.menubar = tk.Menu(window)
        self.filemenu = tk.Menu(self.menubar , tearoff=0 )
        self.filemenu.add_command(label = 'Close' , command= exit )
        self.menubar.add_cascade(menu=self.filemenu , label='File')
        self.filemenu.add_command(label='New'  , command=self.loadedF)
        window.config(menu=self.menubar)



        tk.Label(window , text='').grid(row=0)
        tk.Label(window , text='').grid(row=1)
        tk.Label(window , text='').grid(row=2)
        tk.Label(window , text='').grid(row=3)
        tk.Label(window , text='').grid(row=4)

        self.opening = tk.Label(window , text='Welcome To QuickCart!!' , font = ('Aerial' , 40 , 'bold') )
        self.opening.grid(row= 5 , column= 3 , ipadx=80 , ipady=80)

        

     

    def loadedF(self):

        self.fileop = tk.Toplevel()
        self.fileop.geometry('250x250')
        self.fileop.title('QuickCart')
        self.label = tk.Label(self.fileop , text="Add Stores" , font = ('Aerial' , 30 , 'bold'))
        self.label.grid(row=0 , column=1 , padx=20 ,  pady=20)
        self.Store_entry = tk.Entry(self.fileop , font = ('Aerial' , 16))
        self.Store_entry.grid(row=1 , column=0 , columnspan=2 ,  pady=20)
        self.cre_eat= tk.Button(self.fileop , text="Create Store" , font = ('Aerial' , 16) , command=self.Create_stores)
        self.cre_eat.grid(row=2 , column=1 , padx=10 , pady=10)

        self.appl = tk.Toplevel()
        self.appl.geometry('800x500')
        self.appl.title('Stores')
        
        self.refresh = tk.Button(self.appl , text='refresh'  , font=('Aerial' , 18) , command=self.ref_load)
        self.refresh.grid(row=0 , column=0 , padx=10 , pady=10)
        





    def Create_stores(self):

        Store_name = self.Store_entry.get().strip()
        if not Store_name:
            messagebox.showerror("Error", "Store name cannot be empty")
            return


        self.cursor = conn.cursor()
        self.store_name = str(self.Store_entry.get())
        print(self.store_name)
        self.sql = 'INSERT INTO ShoppingList(Name) VALUES ("' + self.store_name + '")'
        self.cursor.execute(self.sql)
        conn.commit()
        self.loadedPage()

        
        


        
       



    def ref_load(self):

     
        for widget in self.appl.winfo_children(): 
            widget.destroy()

        self.res = self.cursor.execute("SELECT ShoppingListId , Name FROM ShoppingList")
        stores = self.res.fetchall()

        for i , (ShoppingListId , Name) in enumerate(stores):
            btn = tk.Button(self.appl , text = Name , font =('Aerial' , 16) , command=lambda sid=ShoppingListId: self.open_store(sid))

            btn.grid(row = i , column=0, sticky="w",padx=10 ,  pady=5)




Start()
window.mainloop()









#import sqlite3

        
       # connection = sqlite3.connect('Data/Store_Userfile.db')
        #cursor = connection.cursor()
       # query = f"SELECT * FROM stores"
        #cursor.execute(query)
        #stores = cursor.fetchall()

       # column = 0
       # for store in stores:
           
            #column = column + 1

        #self.Wal = tk.Button(window , text='Walmart' , font = ('Aerial' , 16) , command=self.clicked)
        #self.Wal.grid( row=4 , column=0 , ipadx=70 , ipady=40)

        #self.PatelB = tk.Button(window , text='Patel Brothers' , font = ('Aerial' , 16))
        #self.PatelB.grid( row=4 , column=1 , ipadx=70 , ipady=40)

        #self.IndianB = tk.Button(window , text='Indian Bazaar' , font = ('Aerial' , 16))
        #self.IndianB.grid( row=4 , column=2 , ipadx=70 , ipady=40)

        #self.Target = tk.Button(window , text='Target' , font = ('Aerial' , 16))
        #self.Target.grid( row=4 , column=3 , ipadx=70 , ipady=40)

         #self.fBelow = tk.Button(window , text=store[1] , font = ('Aerial' , 16))
        #self.fBelow.grid( row=4 , column=column, ipadx=78 , ipady=40)


        
        #tk.Label(window , text='Stores' , font=('Aerial' , 20 , 'bold')).grid(row=0 , column=2 , padx=20 , pady=10)
        #tk.Label(window , text='').grid(row=0 , column=0)
        #tk.Label(window , text='').grid(row=0 , column=1)
 
        
        #tk.Label(window , text='').grid(row=1)
        #tk.Label(window , text='').grid(row=2)
        #tk.Label(window , text='').grid(row=3)




        