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

        self.render_member_node('me', row=4, column=3) # <- Self resposável por inicializar exibindo "Eu" centralizado na cascata.

        # Abaixo teremos as funções responsáveis por realizar a parte transicional e inteligente do projeto
        def change_language(self, lang):
            """ Função responsável pela transição simultânea de idioma em todas as tabelas
            presentes na janela da árvore genealógica """

            self.brain.set_language(lang)
            self.update_interface_labels()
            self.refresh_all_displayed_info()

        def update_interface_labels(self):
            """ Função responsável por trasicionar as cores dos botões de PT para EN
            ou vice e versa."""

            self.title_label.config(text=self.brain.get_text('title'))
            if self.brain.current_lang == 'en':
                self.btn_en.config(bg="#38bdf8", fg="#0f172a")
                self.btn_pt.config(bg="#334155", fg="#94a3b8")
            else:
                self.btn_pt.config(bg="#38bdf8", fg="#0f172a")
                self.btn_en.config(bg="#334155", fg="#94a3b8")
        
        def shrink_parent_node(self, member_id):
            """ Função que vai enconlher o card pai para otimizar o espaço visual quando novos cards surgem. """

            if member_id in self.active_widgets:
                widgets = self.active_widgets[member_id]
            if 'bio_label' in widgets and widgets['bio_label'].winfo_exists():
                widgets['bio_label'].pack_forget()
            if 'img_label' in widgets and widgets['img_label'].winfo_exists():
                widgets['img_label'].config(height=2, text="[ Mini Photo ]")

        def render_member_node(self, member_id, row, column, parent_to_shrink=None):
            """ Função designada a gerar o conteúdo dos cards de TODOS os membros da família. """

            if parent_to_shrink:
                self.shrink_parent_node(parent_to_shrink)
                
            node_frame = tk.LabelFrame(self.main_container, text=f" {self.brain.get_text(member_id)} ", 
                                    bg="white", font=self.card_title_font, fg="#0f172a", padx=15, pady=15, relief=tk.GROOVE)
            node_frame.grid(row=row, column=column, padx=20, pady=15, sticky="nsew")
            self.active_frames[member_id] = node_frame
            
            img_label = tk.Label(node_frame, text="[ Photo Here ]", bg="#e2e8f0", width=24, height=6, fg="#475569", font=self.info_font)
            img_label.pack(pady=6)
            
            info_btn = tk.Button(node_frame, text=self.brain.get_text('btn_show_info'), bg="#2563eb", fg="white", font=self.btn_font,
                                activebackground="#1d4ed8", activeforeground="white", relief=tk.FLAT, cursor="hand2", padx=8, pady=4)
            info_btn.config(command=lambda: self.reveal_member_details(member_id, node_frame, row, column, info_btn))
            info_btn.pack(pady=6)
            
            self.active_widgets[member_id] = { # <- Esse objeto irá guardar um colchetes vazio em cada membro da família até a exibição
                'frame': node_frame,
                'info_btn': info_btn,
                'img_label': img_label,
                'details': []
            }

        def reveal_member_details(self, member_id, frame, row, column, btn_to_remove):
            """ Essa função vai obter os caminhos gerados a partir da função anterior e preencher com 
            com as informações do mini banco de dados criado no arquivo 'brain.py' """

            btn_to_remove.pack_forget()
            info = self.brain.get_member_info(member_id)
            
            lbl_name = tk.Label(frame, text=f"Name: {info.get('name')}", font=self.name_font, bg="white", fg="#0f172a", anchor="w")
            lbl_name.pack(fill=tk.X, pady=2)
            
            lbl_age = tk.Label(frame, text=f"Age: {info.get('age')}", font=self.info_font, bg="white", fg="#475569", anchor="w")
            lbl_age.pack(fill=tk.X, pady=2)
            
            lbl_bio = tk.Label(frame, text=info.get('bio'), font=self.bio_font, bg="white", fg="#64748b", wraplength=210, justify=tk.LEFT)
            lbl_bio.pack(fill=tk.X, pady=6)
            
            self.active_widgets[member_id]['bio_label'] = lbl_bio
            self.active_widgets[member_id]['details'].extend([lbl_name, lbl_age])
            
            btn_container = tk.Frame(frame, bg="white")
            btn_container.pack(pady=6)
            
            # Lógica de Fluxo e Direcionamento da Cascata
            if member_id == 'me':
                btn_f = tk.Button(btn_container, text=self.brain.get_text('btn_father'), bg="#0ea5e9", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_f.config(command=lambda: [btn_f.config(state=tk.DISABLED), self.render_member_node('father', row-1, column-1, 'me')])
                btn_f.pack(side=tk.LEFT, padx=4)
                
                btn_m = tk.Button(btn_container, text=self.brain.get_text('btn_mother'), bg="#ec4899", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_m.config(command=lambda: [btn_m.config(state=tk.DISABLED), self.render_member_node('mother', row-1, column+1, 'me')])
                btn_m.pack(side=tk.LEFT, padx=4)
                
            elif member_id == 'father':
                btn_sib = tk.Button(btn_container, text=self.brain.get_text('btn_siblings'), bg="#10b981", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_sib.config(command=lambda: [btn_sib.config(state=tk.DISABLED), self.render_paternal_siblings(row, column-1)])
                btn_sib.pack(pady=4)
                
            elif member_id == 'mother':
                btn_g = tk.Button(btn_container, text=self.brain.get_text('btn_maternal_grandparents'), bg="#8b5cf6", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_g.config(command=lambda: [btn_g.config(state=tk.DISABLED), self.render_member_node('maternal_grandfather', row-1, column, 'mother'), self.render_member_node('maternal_grandmother', row-1, column+1, 'mother')])
                btn_g.pack(side=tk.LEFT, padx=4)
                
                btn_un = tk.Button(btn_container, text=self.brain.get_text('btn_uncle'), bg="#f59e0b", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_un.config(command=lambda: [btn_un.config(state=tk.DISABLED), self.render_member_node('uncle_maternal', row, column+2, 'mother')])
                btn_un.pack(side=tk.LEFT, padx=4)
                
            elif member_id == 'uncle_maternal':
                btn_cou = tk.Button(btn_container, text=self.brain.get_text('btn_cousin'), bg="#06b6d4", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
                btn_cou.config(command=lambda: [btn_cou.config(state=tk.DISABLED), self.render_member_node('cousin_maternal', row+1, column, 'uncle_maternal')])
                btn_cou.pack(pady=4)

        def render_paternal_siblings(self, base_row, start_col):
            """ Renderiza os 4 irmãos por parte de pai alinhados verticalmente à esquerda, como eu
            sei que tenho mas não os conheço, isto se tornará padrão sem alterações. """

            for i in range(4):
                sibling_key = f"paternal_sibling_{i+1}"
                self.render_member_node(sibling_key, row=base_row + (i - 1), column=start_col, parent_to_shrink='father')
                
if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyTreeApp(root)
    root.mainloop()