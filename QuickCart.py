import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import font

conn = sqlite3.connect('Data\\Store_Userfile.db')
cursor = conn.cursor()

window = tk.Tk()
window.geometry("800x500")
window.title('QuickCart')


var = {}
cb_font = {}

class App:  
   


    def __init__(self):
            #store label


        # Frame to hold store buttons
        self.store_frame = tk.Frame(window)
        self.store_frame.grid(row=1, column=0, sticky="w")

        self.item_frame = tk.Frame(window)
        self.item_frame.grid(row = 1 , column=35 , sticky="e")



        
        store = tk.Label(window , text='Stores' , font= ('Aerial' , 18 , 'bold'))
        store.grid( row=0 ,column=0 , padx = 10 , pady=10)


       


        #Brings create store button to 20th row
        for r in range(20):
            window.grid_rowconfigure(r , minsize=20)

        for r in range(35):
            window.grid_columnconfigure(r , minsize=20)



         #create store button
        self.store_create = tk.Button(window , text= 'Create Store' , font = ('Aerial' , 16, 'bold') , command=self.Create_stores)
        self.store_create.grid(padx=10 , pady=10 , row= 0 , column=34)

        #Store entry place to create
        self.Store_entry = tk.Entry(window , font=('Areial' , 16))
        self.Store_entry.grid(padx=5 , pady= 10 , row= 0 , column= 35)

      
        for r in range(20):
                window.grid_rowconfigure(r , minsize=20)

        for r in range(35):
            window.grid_columnconfigure(r , minsize=20)


        self.refresh_button()
            



    btn = []
    def open_store(self,sid):
        currentButton = None
        for key, value in self.btn:
            
            if key == sid:
              currentButton = value
            else:
              value.config(relief = "raised")

                             
        if hasattr(self, "add_item"):
            self.add_item.destroy()
        if hasattr(self, "item_name"):
            self.item_name.destroy()  
            
        if  currentButton.cget('relief') == "raised" :
            currentButton.config(relief="sunken")
            self.refresh_items(sid)

        else:
            currentButton.config(relief="raised")
            self.refresh_items(0)


  
                
                
    def refresh_items(self , sid):
    
        cursor = conn.cursor()
       
                
        for widget in self.item_frame.winfo_children():
            widget.destroy()
                 
        if sid == 0:
            return   
        item_get = cursor.execute(f"SELECT Name , ShoppingListItemId FROM ShoppingListItem WHERE ShoppingListId = ?" , (sid,  ) )
        Item_store = item_get.fetchall()
                    
                    
        for i , (Name , ShoppingListItemId) in enumerate(Item_store):
            tmpvar = tk.IntVar()
            tmpFont =  font.Font(family="Arial" , size=14)
            cb_font[ShoppingListItemId] = tmpFont
            var[ShoppingListItemId] = tmpvar
            items = tk.Checkbutton(self.item_frame ,  text=Name  , variable=tmpvar , command =lambda slid = ShoppingListItemId:(self.toggle_crossout(slid)) , font = tmpFont )
            items.grid(row = 1+i , column=0 , sticky="e" , padx=20 , pady=10 )
            
            
                
                
                
        self.add_item = tk.Button(window , text='Add_Item' , font=('Aerial' , 16  , 'bold') , command=lambda sid = sid:(self.create_items(sid) , self.toggle_strikethrough))
        self.add_item.grid(row =20, column=34 , padx=10 , pady=10)
                
        self.item_name = tk.Entry(window , font = ('Aerial' , 16))
        self.item_name.grid(row = 20 , column= 35 , padx=5 , pady=10)
            
                
    
    
        
            
            
    def toggle_crossout(self , slid):
        
        var1 = var[slid]
        if var1.get() == 1:
            cb_font[slid].configure(overstrike=1)   # turn on crossout
        else:
            cb_font[slid].configure(overstrike=0)   # turn off crossout


            
            
            
            
            
    def refresh_button(self):
        cursor = conn.cursor()
        for widget in self.store_frame.winfo_children():
              widget.destroy()
        newres = cursor.execute("SELECT ShoppingListId , Name FROM ShoppingList")
        newstore = newres.fetchall()
       
        self.btn = []
        for i , (ShoppingListId , Name) in enumerate(newstore):
                btn  = tk.Button(self.store_frame , text = Name , font =('Aerial' , 16) ,command=lambda sid=ShoppingListId: self.open_store(sid))
                self.btn.append(( ShoppingListId , btn))
                btn.grid(row = 1+i , column=0, sticky="w",padx=20 ,  pady=10)
            





    def create_items(self , sid):
        cursor = conn.cursor()
        Item_name = self.item_name.get().strip()
        if not Item_name:
            messagebox.showerror('Error' , "Item name cannot be empty")
            return
        
        item_name = str(self.item_name.get())
        print(item_name)
        
        cursor.execute(f"INSERT INTO ShoppingListItem(Name , ShoppingListId) VALUES (? , ?)" , (item_name,sid ))
        conn.commit()
        self.refresh_items(sid)



    def Create_stores(self):
        cursor = conn.cursor()
        Store_name = self.Store_entry.get().strip()
        if not Store_name:
            messagebox.showerror("Error", "Store name cannot be empty")
            return
        store_name = str(self.Store_entry.get())
        print(store_name)

        
        cursor.execute("INSERT INTO ShoppingList(Name) VALUES (?)", (Store_name,))
        conn.commit()
        self.refresh_button()

            


    
App()
window.mainloop()