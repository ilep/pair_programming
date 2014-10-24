#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 13:54:55 2014

@author: ivan lepoutre
"""


import Tkinter as tk



class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master, background = 'white')
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text= 'Quit', command = self.quit)
        self.quitButton.grid()



app = Application()
app.master.title('Kruskal Algorithm')
app.mainloop()
        
    
    
#from Graph import Node, Edge, Graph
