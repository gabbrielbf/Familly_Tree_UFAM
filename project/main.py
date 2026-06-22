# project/main.py

import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions.brain import FamilyTreeBrain # Garante que o Python encontre a pasta das funções

class FamilyTreeApp:
    def __init__(self, root):
        self.root = root
        self.brain = FamilyTreeBrain()

        self.root.title('Family Cascade System')
        self.root.geometry('1300x850')
        self.root.configure(bg='#f1f5f9')

        """ Predefinições das fontes, cores e modelos dos textos exibidos
        em toda a execução do programa. """

        self.title_font = ('Segoe UI', 18, 'bold')
        self.lang_font = ('Segoe UI', 10, 'bold')
        self.card_title_font = ('Segoe UI', 12, 'bold')
        self.name_font = ('Segoe UI', 11, 'bold')
        self.info_font = ('Segoe UI', 10)
        self.bio_font = ('Segoe UI', 10, 'italic')
        self.btn_font = ('Segoe UI', 9, 'bold')

        """ Barra superior do cabeçario """