#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 13:54:55 2014

@author: ivan lepoutre
"""

# http://zetcode.com/gui/tkinter/introduction/

from Tkinter import Tk, Frame, BOTH



class MyFrame(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):        
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.title("Kruskal Live!")
        self.pack(fill=BOTH, expand=1)
        

def main():
  
    root = Tk()
    root.geometry("750x550+300+300")
    main_frame = MyFrame(root)
    root.mainloop()  


if __name__ == '__main__':
    main()