import tkinter as tk
from tkinter import *
import tkinter.font as font

def open_root():
    root=Tk()
    root.title('Home')
    root.geometry('1000x750')
    
    
    root.mainloop()
    
    def store_page():
        print("the store is now open")
    
    def exit_window():
        root.destroy()
        
    gallery_button=tk.Button(text='Design Rig', bg='blue', fg='red', command=store_page)
    font_style = font.Font(family='Arial', size=15, weight='bold')
    gallery_button['font'] = font_style
    
    gallery_button.config(height=5, width=20)
    
    gallery_button.pack
    exit_button=tk.Button(text='Exit', command=exit_window)
    exit_button.place(x=180,y=200)
    
    

open_root()