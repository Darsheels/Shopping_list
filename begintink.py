import tkinter as tk 
from tkinter import messagebox

class MyGuI:

    def __init__(self):
        self.window = tk.Tk()

        self.menubar = tk.Menu(self.window)  #Making a menu for app
        self.fileMenu = tk.Menu(self.menubar , tearoff= 0) #tearoff prevents the das line on top of the application for the menu
        self.fileMenu.add_command(label="Close" , command=self.on_closing) #adds a sub file to the self.filemenu called close which exits out of the whole application 
        self.fileMenu.add_separator() #Adds a seperator line between the two options in the dropdown
        self.fileMenu.add_command(label = 'Close without question' , command= exit )  #Closes without question


        self.menubar.add_cascade(menu=self.fileMenu , label='File') #add cascade adds a drop down to the menu but add command adds a clickable object
        

        self.actionmenu = tk.Menu(self.menubar , tearoff= 0 )
        self.actionmenu.add_command(label = 'Show message' , command = self.show_message)
        
        self.menubar.add_cascade(menu=self.actionmenu , label='Action')
        
        self.window.config(menu=self.menubar)  #finally adds the menu bar to the app 

        self.label = tk.Label(self.window, text = 'Your Message' , font = ('aerial' , 16))
        self.label.pack(padx=10 , pady=10)

        self.textbox = tk.Text(self.window)  
        self.textbox.bind('<KeyPress>' , self.ShortCut)  #adds an event to the textbox and connects the shortcut function 
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar() #this var stores the changes in the checkbutton if clicked it = 1 else its a 0 
        self.check = tk.Checkbutton(self.window , text = 'ShowMessage Box' , font = ('Arial' , 16) , variable=self.check_state) #connects the Var to the check button to add functionality
        self.check.pack(padx=10 , pady=10)

        self.button = tk.Button(self.window ,text='show message ' , font = ('Arial' , 18) , command=self.show_message) #command parameter tells what to run when the button is pressed 
        self.button.pack(padx=10 , pady=10)

        self.clrButton = tk.Button(self.window , text = 'ClearText' , font = ('Arial' , 18) , command = self.clear)
        self.clrButton.pack(padx=10 , pady= 10)
        


        self.window.protocol("WM_DELETE_WINDOW" , self.on_closing)
        self.window.mainloop()  #actually runs the application 

    def show_message(self):   #function check the int variable value and puts constraints               
        print(self.check_state.get()) 

        if self.check_state.get() == 0:
             print(self.textbox.get('1.0' , tk.END))  #gets everything in the textbox from the start to the end
        else:
            messagebox.showinfo(title='Message' , message= self.textbox.get('1.0' , tk.END)) #pops a messagebox with the text you wrote in the text box if the check box is not clicked
    
    def ShortCut(self , event):
        if event.state & 4 and event.keysym == 'Return':    #if control and enter are clicked they will do the same function as if the button was clicked
            self.show_message()
    
    def on_closing(self):
       print('PLS I NEED THIS')
       if messagebox.askyesnocancel(title = 'Quit?' , message='Do you really want to quit?'):  #double check if the user does want to quit the application
        self.window.destroy() 

    def clear(self):
        self.textbox.delete('1.0' , tk.END) #clears everything in the textbox
       


MyGuI()



    


