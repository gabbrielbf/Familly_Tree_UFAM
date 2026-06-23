# project/main.py

import tkinter as tk
from tkinter import ttk
import sys
import os
from PIL import Image, ImageTk, ImageOps

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # <- Comando designado para encontrar arquivos e módulos localizados em outras pastas.
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
        self.scrollbar_x = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.main_container = tk.Frame(self.canvas, bg="#f1f5f9")
        
        self.main_container.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.main_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set, xscrollcommand=self.scrollbar_x.set)
        
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.scrollbar.pack(side="right", fill="y")
        
        self.active_widgets = {}
        self.active_frames = {}
        self.me_btn_container = None # Container para gerenciar de forma limpa os botões abaixo da sua caixa

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

    def load_and_resize_image(self, image_name, size=(170, 170)):
        """ Função responsável por carregar a imagem da pasta assets, redimensionar
        usando Pillow e preparar para exibição no Tkinter de forma segura. """

        if not image_name:
            return None
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            img_path = os.path.join(base_dir, "assets", image_name)
            if os.path.exists(img_path):
                # Se for o Zezin, forçamos um tamanho bem maior para destaque na apresentação
                if image_name == "gato_zezin.jpeg":
                    size = (320, 320)
                    
                img = Image.open(img_path)
                
                # Definição padrão de centralização (meio do quadrado)
                center_x = 0.5
                center_y = 0.5
                
                if image_name == "foto_minha.jpeg":
                    img = img.rotate(-90, expand=True)
                
                # Ajustes específicos de enquadramento vertical para evitar cortes de rostos
                elif image_name == "foto_pai.JPG":
                    center_y = 0.1  # Sobe o enquadramento para focar no topo da imagem e exibir o rosto do pai
                elif image_name == "foto_avo1.JPG":
                    center_y = 0.2  # Ajusta verticalmente para não cortar o topo da cabeça do avô
                    
                # Enquadra e corta as bordas sem esticar as pessoas utilizando o alinhamento calibrado
                img = ImageOps.fit(img, size, Image.Resampling.LANCZOS, centering=(center_x, center_y))
                return ImageTk.PhotoImage(img)
        except Exception:
            pass
        return None

    def shrink_parent_node(self, member_id):
        """ Função que vai enconlher o card pai para otimizar o espaço visual quando novos cards surgem. """

        if member_id in self.active_widgets:
            widgets = self.active_widgets[member_id]
            # Removendo o pack_forget da bio_label para garantir que a biografia nunca desapareça ao expandir novos membros

    def check_all_members_expanded(self):
        """ Monitora e verifica se todas as ramificações de familiares foram renderizadas na tela.
        Caso positivo, injeta o botão especial do mascote 'Zezin' ao lado do botão da mãe. """

        required_nodes = [
            'father', 'mother', 'maternal_grandfather', 'maternal_grandmother', 
            'uncle_maternal', 'cousin_maternal',
            'paternal_sibling_1', 'paternal_sibling_2', 'paternal_sibling_3', 'paternal_sibling_4',
            'maternal_sibling_1', 'maternal_sibling_2'
        ]
        
        all_present = all(node in self.active_widgets for node in required_nodes)
        
        if all_present and self.me_btn_container and 'btn_zezin' not in self.active_widgets['me']['flow_buttons']:
            is_pt = getattr(self.brain, 'current_lang', 'pt') == 'pt'
            btn_text = "Ver Mascote" if is_pt else "View Pet"
            
            btn_z = tk.Button(self.me_btn_container, text=btn_text, bg="#10b981", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            # Corrigido de volta para row=5, column=3 para que fique perfeitamente abaixo de "Eu" sem sobrepor a mãe
            btn_z.config(command=lambda: [btn_z.config(state=tk.DISABLED), self.render_member_node('zezin_mascote', row=5, column=3, parent_to_shrink='me')])
            btn_z.pack(side=tk.LEFT, padx=4)
            self.active_widgets['me']['flow_buttons']['btn_zezin'] = btn_z

    def render_member_node(self, member_id, row, column, parent_to_shrink=None):
        """ Função designada a gerar o conteúdo dos cards de TODOS os membros da família. """

        if parent_to_shrink:
            self.shrink_parent_node(parent_to_shrink)
            
        # Tratamento especial de texto dinâmico para a caixa do animal de estimação extra.
        if member_id == 'zezin_mascote':
            is_pt = getattr(self.brain, 'current_lang', 'pt') == 'pt'
            display_title = " Mascote " if is_pt else " Pet "
        else:
            display_title = f" {self.brain.get_text(member_id)} "

        node_frame = tk.LabelFrame(self.main_container, text=display_title, 
                                bg="white", font=self.card_title_font, fg="#0f172a", padx=15, pady=15, relief=tk.GROOVE)
        node_frame.grid(row=row, column=column, padx=20, pady=15, sticky="nsew")
        self.active_frames[member_id] = node_frame
        
        # Recupera as informações estritamente ligadas ao mascote ou puxa do cérebro para familiares
        if member_id == 'zezin_mascote':
            info = {
                'image': 'gato_zezin.jpeg',
                'name': 'Zezin',
                'age': '1 ano' if getattr(self.brain, 'current_lang', 'pt') == 'pt' else '1 year old',
                'bio': 'O gato companheiro da casa, adora dormir ao lado com as pernas arreganhadas.' if getattr(self.brain, 'current_lang', 'pt') == 'pt' else 'The household cat loves sleeping right next to me with its legs up in the air.'
            }
        else:
            info = self.brain.get_brain_info(member_id) if hasattr(self.brain, 'get_brain_info') else self.brain.get_member_info(member_id)
            
        photo = self.load_and_resize_image(info.get('image'))
        
        if photo:
            img_label = tk.Label(node_frame, image=photo, bg="#e2e8f0")
            img_label.image = photo
        else:
            img_label = tk.Label(node_frame, text="[ Photo Here ]", bg="#e2e8f0", width=24, height=6, fg="#475569", font=self.info_font)
            
        img_label.pack(pady=6)
        
        info_btn_text = self.brain.get_text('btn_show_info') if hasattr(self.brain, 'get_text') else "Ver Informações"
        if member_id == 'zezin_mascote' and getattr(self.brain, 'current_lang', 'pt') == 'en':
            info_btn_text = "Show Information"

        info_btn = tk.Button(node_frame, text=info_btn_text, bg="#2563eb", fg="white", font=self.btn_font,
                            activebackground="#1d4ed8", activeforeground="white", relief=tk.FLAT, cursor="hand2", padx=8, pady=4)
        info_btn.config(command=lambda: self.reveal_member_details(member_id, node_frame, row, column, info_btn))
        info_btn.pack(pady=6)
        
        self.active_widgets[member_id] = { # <- Esse objeto irá guardar um colchetes vazio em cada membro da família até a exibição
            'frame': node_frame,
            'info_btn': info_btn,
            'img_label': img_label,
            'details': [],
            'flow_buttons': {}
        }
        
        # Dispara verificação para avaliar se o botão do mascote já está elegível para surgir
        self.check_all_members_expanded()

    def reveal_member_details(self, member_id, frame, row, column, btn_to_remove):
        """ Essa função vai obter os caminhos gerados a partir da função anterior e preencher com 
        com as informações do mini banco de dados criado no arquivo 'brain.py' """

        # Removido pack_forget para que o botão de mostrar informações permaneça visível para todos os cartões
        if member_id == 'zezin_mascote':
            info = {
                'image': 'gato_zezin.jpeg',
                'name': 'Zezin',
                'age': '1 ano' if getattr(self.brain, 'current_lang', 'pt') == 'pt' else '1 year old',
                'bio': 'O gato companheiro da casa, adora dormir ao lado com as pernas arreganhadas.' if getattr(self.brain, 'current_lang', 'pt') == 'pt' else 'The household cat loves sleeping right next to me with its legs up in the air.'
            }
        else:
            info = self.brain.get_brain_info(member_id) if hasattr(self.brain, 'get_brain_info') else self.brain.get_member_info(member_id)
        
        # Sistema redundante de tradução segura para evitar exibição das chaves de texto cruas do arquivo 'brain.py'
        is_pt = getattr(self.brain, 'current_lang', 'pt') == 'pt'
        
        fetched_name = self.brain.get_text('label_name') if hasattr(self.brain, 'get_text') else None
        fetched_age = self.brain.get_text('label_age') if hasattr(self.brain, 'get_text') else None
        
        label_name_text = "Nome" if is_pt else "Name"
        if fetched_name and fetched_name != 'label_name':
            label_name_text = fetched_name
            
        label_age_text = "Idade" if is_pt else "Age"
        if fetched_age and fetched_age != 'label_age':
            label_age_text = fetched_age
        
        # Verifica se as labels já foram criadas para não duplicar elementos na tela ao clicar várias vezes
        if 'name_label' in self.active_widgets[member_id] and self.active_widgets[member_id]['name_label'].winfo_exists():
            self.active_widgets[member_id]['name_label'].config(text=f"{label_name_text}: {info.get('name')}")
            self.active_widgets[member_id]['age_label'].config(text=f"{label_age_text}: {info.get('age')}")
            self.active_widgets[member_id]['bio_label'].config(text=info.get('bio'))
            return

        lbl_name = tk.Label(frame, text=f"{label_name_text}: {info.get('name')}", font=self.name_font, bg="white", fg="#0f172a", anchor="w")
        lbl_name.pack(fill=tk.X, pady=2)
        
        lbl_age = tk.Label(frame, text=f"{label_age_text}: {info.get('age')}", font=self.info_font, bg="white", fg="#475569", anchor="w")
        lbl_age.pack(fill=tk.X, pady=2)
        
        lbl_bio = tk.Label(frame, text=info.get('bio'), font=self.bio_font, bg="white", fg="#64748b", wraplength=210, justify=tk.LEFT)
        lbl_bio.pack(fill=tk.X, pady=6)
        
        self.active_widgets[member_id]['name_label'] = lbl_name
        self.active_widgets[member_id]['age_label'] = lbl_age
        self.active_widgets[member_id]['bio_label'] = lbl_bio
        self.active_widgets[member_id]['details'].extend([lbl_name, lbl_age])
        
        btn_container = tk.Frame(frame, bg="white")
        btn_container.pack(pady=6)
        
        # Armazena a referência global do container da sua caixa para injetar o mascote posteriormente à direita
        if member_id == 'me':
            self.me_btn_container = btn_container
        
        # Lógica de Fluxo e Direcionamento da Cascata
        if member_id == 'me':
            btn_f = tk.Button(btn_container, text=self.brain.get_text('btn_father'), bg="#0ea5e9", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_f.config(command=lambda: [btn_f.config(state=tk.DISABLED), self.render_member_node('father', row, column-1, 'me')])
            btn_f.pack(side=tk.LEFT, padx=4)
            self.active_widgets[member_id]['flow_buttons']['btn_father'] = btn_f
            
            btn_m = tk.Button(btn_container, text=self.brain.get_text('btn_mother'), bg="#ec4899", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_m.config(command=lambda: [btn_m.config(state=tk.DISABLED), self.render_member_node('mother', row, column+1, 'me')])
            btn_m.pack(side=tk.LEFT, padx=4)
            self.active_widgets[member_id]['flow_buttons']['btn_mother'] = btn_m
            
            # Segunda checagem caso o usuário expanda as ramificações e depois clique em mostrar informações de "Me" por último
            self.check_all_members_expanded()
            
        elif member_id == 'father':
            btn_sib = tk.Button(btn_container, text=self.brain.get_text('btn_siblings'), bg="#10b981", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_sib.config(command=lambda: [btn_sib.config(state=tk.DISABLED), self.render_paternal_siblings(row, column-1)])
            btn_sib.pack(pady=4)
            self.active_widgets[member_id]['flow_buttons']['btn_siblings'] = btn_sib
            
        elif member_id == 'mother':
            btn_g = tk.Button(btn_container, text=self.brain.get_text('btn_maternal_grandparents'), bg="#8b5cf6", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_g.config(command=lambda: [btn_g.config(state=tk.DISABLED), self.render_member_node('maternal_grandfather', row-1, column, 'mother'), self.render_member_node('maternal_grandmother', row-1, column+1, 'mother')])
            btn_g.pack(side=tk.LEFT, padx=4)
            self.active_widgets[member_id]['flow_buttons']['btn_maternal_grandparents'] = btn_g
            
            btn_un = tk.Button(btn_container, text=self.brain.get_text('btn_uncle'), bg="#f59e0b", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_un.config(command=lambda: [btn_un.config(state=tk.DISABLED), self.render_member_node('uncle_maternal', row, column+1, 'mother')])
            btn_un.pack(side=tk.LEFT, padx=4)
            self.active_widgets[member_id]['flow_buttons']['btn_uncle'] = btn_un

            btn_msib = tk.Button(btn_container, text=self.brain.get_text('btn_maternal_siblings'), bg="#a855f7", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_msib.config(command=lambda: [btn_msib.config(state=tk.DISABLED), self.render_maternal_siblings(row+1, column)])
            btn_msib.pack(pady=4)
            self.active_widgets[member_id]['flow_buttons']['btn_maternal_siblings'] = btn_msib
            
        elif member_id == 'uncle_maternal':
            btn_cou = tk.Button(btn_container, text=self.brain.get_text('btn_cousin'), bg="#06b6d4", fg="white", font=self.btn_font, relief=tk.FLAT, cursor="hand2")
            btn_cou.config(command=lambda: [btn_cou.config(state=tk.DISABLED), self.render_member_node('cousin_maternal', row+1, column, 'uncle_maternal')])
            btn_cou.pack(pady=4)
            self.active_widgets[member_id]['flow_buttons']['btn_cousin'] = btn_cou

    def render_paternal_siblings(self, base_row, start_col):
        """ Renderiza os 4 irmãos por parte de pai alinhados verticalmente à esquerda, como eu
        sei que tenho mas não os conheço, isto se tornará padrão sem alterações. """

        for i in range(4):
            sibling_key = f"paternal_sibling_{i+1}"
            self.render_member_node(sibling_key, row=base_row + (i - 1), column=start_col, parent_to_shrink='father')

    def render_maternal_siblings(self, base_row, start_col):
        for i in range(2):
            sibling_key = f"maternal_sibling_{i+1}"
            self.render_member_node(sibling_key, row=base_row + i, column=start_col, parent_to_shrink='mother')

    def refresh_all_displayed_info(self):
        """ Isso aqui vai simplismente atualizar todas as informações presentes na tela
        de inglês para português e de português para inglês. """

        for member_id, data in list(self.active_widgets.items()):
            if data['frame'].winfo_exists():
                is_pt = getattr(self.brain, 'current_lang', 'pt') == 'pt'
                
                # Tradução dinâmica e robusta para o card do animal
                if member_id == 'zezin_mascote':
                    data['frame'].configure(text=" Mascote " if is_pt else " Pet ")
                else:
                    data['frame'].configure(text=f" {self.brain.get_text(member_id)} ")
                
                if 'info_btn' in data and data['info_btn'].winfo_exists():
                    info_btn_label = self.brain.get_text('btn_show_info') if hasattr(self.brain, 'get_text') else "Ver Informações"
                    if member_id == 'zezin_mascote' and not is_pt:
                        info_btn_label = "Show Information"
                    data['info_btn'].configure(text=info_btn_label)
                    
                fetched_name = self.brain.get_text('label_name') if hasattr(self.brain, 'get_text') else None
                fetched_age = self.brain.get_text('label_age') if hasattr(self.brain, 'get_text') else None
                
                label_name_text = "Nome" if is_pt else "Name"
                if fetched_name and fetched_name != 'label_name':
                    label_name_text = fetched_name
                    
                label_age_text = "Idade" if is_pt else "Age"
                if fetched_age and fetched_age != 'label_age':
                    label_age_text = fetched_age
                    
                if member_id == 'zezin_mascote':
                    info = {
                        'image': 'gato_zezin.jpeg',
                        'name': 'Zezin',
                        'age': '1 ano' if is_pt else '1 year old',
                        'bio': 'O gato companheiro da casa, adora dormir ao lado com as pernas arreganhadas.' if is_pt else 'The household cat loves sleeping right next to me with its legs up in the air.'
                    }
                else:
                    info = self.brain.get_brain_info(member_id) if hasattr(self.brain, 'get_brain_info') else self.brain.get_member_info(member_id)

                if 'name_label' in data and data['name_label'].winfo_exists():
                    data['name_label'].configure(text=f"{label_name_text}: {info.get('name')}")
                if 'age_label' in data and data['age_label'].winfo_exists():
                    data['age_label'].configure(text=f"{label_age_text}: {info.get('age')}")
                if 'bio_label' in data and data['bio_label'].winfo_exists():
                    data['bio_label'].configure(text=info.get('bio'))
                    
                if 'flow_buttons' in data:
                    for btn_key, btn_obj in data['flow_buttons'].items():
                        if btn_obj.winfo_exists():
                            if btn_key == 'btn_zezin':
                                btn_obj.configure(text="Ver Mascote" if is_pt else "View Pet")
                            else:
                                btn_obj.configure(text=self.brain.get_text(btn_key))

               
if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyTreeApp(root)
    root.mainloop()