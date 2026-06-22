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

        self.root.title("Family Tree Cascade System")
        self.root.geometry('1300x850') # <- Definindo o tamanho das tabelas
        self.root.configure(bg="#f1f5f9") # <- Definindo a cor branca como fundo das tabelas de exibição

        """ Predefinições das fontes, cores e modelos dos textos exibidos
        em toda a execução do programa. """

        self.title_font = ("Segoe UI", 18, "bold")
        self.lang_font = ("Segoe UI", 10, "bold")
        self.card_title_font = ("Segoe UI", 12, "bold")
        self.name_font = ("Segoe UI", 11, "bold")
        self.info_font = ("Segoe UI", 10)
        self.bio_font = ("Segoe UI", 10, "italic")
        self.btn_font = ("Segoe UI", 9, "bold")

        """ Barra superior do cabeçario """

        self.top_frame = tk.Frame(self.root, bg="#0f172a", height=80)
        self.top_frame.pack(fill=tk.X, side=tk.TOP)
        self.top_frame.pack_propagate(False)

        self.title_label = tk.Label(self.top_frame, text="", font=self.title_font, fg="#f8fafc", bg="#0f172a")
        self.title_label.pack(side=tk.LEFT, padx=35, pady=20)

        """ Personalização e configuração dos botões de IDIOMA """

        self.lang_frame = tk.Frame(self.top_frame, bg="#0f172a")
        self.lang_frame.pack(side=tk.RIGHT, padx=35, pady=20)

        self.btn_en = tk.Button(self.lang_frame, text="EN", command=lambda: self.change_language('en'), 
                                font=self.lang_font, bg="#334155", fg="#f8fafc", activebackground="#1e293b", 
                                relief=tk.FLAT, cursor="hand2", width=5)
        self.btn_en.pack(side=tk.RIGHT, padx=5) # <- Estes comandos "btn_en" são responsáveis por transicionar todo o conteúdo da página para inglês
                                                # Usaremos a mesma metologia para o código abaixo, no qual inveterá para português "btn_pt".

        self.btn_pt = tk.Button(self.lang_frame, text="PT", command=lambda: self.change_language('pt'), 
                                font=self.lang_font, bg="#334155", fg="#f8fafc", activebackground="#1e293b", 
                                relief=tk.FLAT, cursor="hand2", width=5)
        self.btn_pt.pack(side=tk.RIGHT, padx=5)

        """ Área rolável para conseguir realizar a exibição de cada item da página """

        self.canvas = tk.Canvas(self.root, bg="#f1f5f9", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.main_container = tk.Frame(self.canvas, bg="#f1f5f9")
        
        self.main_container.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.main_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.scrollbar.pack(side="right", fill="y")
        
        self.active_widgets = {}
        self.active_frames = {}
        self.update_interface_labels()

        self.render_member_node('me', row=4, column=3) # <- Self resposável por inicializar exibindo "Eu" centralizado na cascata
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyTreeApp(root)
    root.mainloop()