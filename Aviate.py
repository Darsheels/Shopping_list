import tkinter as tk 
from tkinter import messagebox
from math import radians , sin, cos, asin, degrees

window = tk.Tk()
window.geometry("800x500")
window.title('Aviate')
window.grid_columnconfigure(2 , minsize=100)
window.grid_columnconfigure(3 , minsize=100)
window.grid_columnconfigure(4 , minsize=100)
window.grid_columnconfigure(5 , minsize=100)


class WCA:
    def __init__(self):

      #Title
      self.Title = tk.Label(window , text= 'Wind Correction Angle Calculator (WCA)' , font = ('Aerial' , 16)  , bg='grey' )
      self.Title.grid(row=0, column=0, padx=20, pady=10)

      # -- wind direction      
      self.winddir = tk.Label(window, text="Wind Direction", font=("Arial", 16))
      self.winddir.grid(row=1, column=0, sticky="w", padx=20, pady=10)
      self.entryWD = tk.Entry(window , font = ('Aerial' , 16))
      self.entryWD.grid(row=1, column=1)
      

      # --wind speed
      self.windspd = tk.Label(window ,  text= 'Wind Speed' , font = ('Aerial' , 16))
      self.windspd.grid(row=2, column=0, sticky="w", padx=20, pady=10)
      self.entryWS = tk.Entry(window , font = ('Aerial' , 16))
      self.entryWS.grid(row=2, column=1)

      # --true course
      self.Tcourse = tk.Label(window , text='True Course' , font=('Aerial' , 16))
      self.Tcourse.grid(row=3, column=0, sticky="w", padx=20, pady=10)
      self.entryTC = tk.Entry(window ,font = ('Aerial' , 16))
      self.entryTC.grid(row=3, column=1)
      
      # --True Airspeed
      self.TairS = tk.Label(window , text='True Airspeed' , font = ('Aerial' , 16))
      self.TairS.grid(row=4, column=0, sticky="w", padx=20, pady=10)
      self.EntryTAS = tk.Entry(window , font = ('Aerial' , 16))
      self.EntryTAS.grid(row=4, column=1)

      # --Calc Button
      self.Calc = tk.Button(window , text= 'Calculate' , font = ('Aerial' , 16) , command= self.calc ).grid(row=10, column=1, padx=20, pady=10)
      self.output = tk.Label(window, text="", font=('Aerial', 16), bg='grey')
      self.output.grid(row=11, column=1, pady=10)

      #--menu
      self.menubar = tk.Menu(window)
      self.filemenu = tk.Menu(self.menubar , tearoff=0 )
      self.filemenu.add_command(label='Close', command=self.closing)
      self.filemenu.add_separator() #Adds a seperator line between the two options in the dropdown
      self.filemenu.add_command(label = 'Close without question' , command= exit )
      self.filemenu.add_command(label = 'Calculate' , command= self.calc )
      self.menubar.add_cascade(menu=self.filemenu , label='File')
      window.config(menu=self.menubar)

      


    def calc(self):
    # Get values from entries
      wd = float(self.entryWD.get())      # wind direction
      ws = float(self.entryWS.get())      # wind speed
      tc = float(self.entryTC.get())      # true course
      tas = float(self.EntryTAS.get())    # true airspeed

    # Convert angles to radians
      wind_angle = radians(wd - tc)

    # Wind Correction Angle formula
      wca = degrees(asin((ws / tas) * sin(wind_angle)))

    # Groundspeed formula
      gs = tas * cos(radians(wca)) + ws * cos(wind_angle)

    # Display result
      self.output.config(text=f"WCA: {wca:.1f}°   |   GS: {gs:.1f} kts")

    def closing(self):
       if messagebox.askyesno(title= 'Quit' , message='Do you really want to quit?'):
          window.destroy()
       

WCA()    
window.mainloop()
