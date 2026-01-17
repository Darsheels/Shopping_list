import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title('Test')


check = tk.Checkbutton(window , text='hi' , font=('Aerial' , 16))
check.pack(padx=10 , pady=10)





window.mainloop()