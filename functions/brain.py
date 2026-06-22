class FamilyTreeBrain:
    def __init__(self):
        self.current_lang = 'pt'
        
        self.translations = {
            'pt': {
                'title': "Minha Árvore Genealógica",
                'btn_show_info': "Ver Informações",
                'me': "Eu",
                'father': "Pai",
                'mother': "Mãe",
                'maternal_grandfather': "Avô Materno",
                'maternal_grandmother': "Avó Materna",
                'uncle_maternal': "Tio (Materno)",
                'cousin_maternal': "Prima",
                'paternal_sibling_1': "Irmão (Parte de Pai) 1",
                'paternal_sibling_2': "Irmão (Parte de Pai) 2",
                'paternal_sibling_3': "Irmão (Parte de Pai) 3",
                'paternal_sibling_4': "Irmão (Parte de Pai) 4",
                'btn_father': "↑ Ver Pai",
                'btn_mother': "↑ Ver Mãe",
                'btn_maternal_grandparents': "↑ Avós Maternos",
                'btn_uncle': "→ Ver Tio",
                'btn_cousin': "↓ Ver Filha (Prima)",
                'btn_siblings': "← Ver Irmãos por parte de Pai"
            },
            'en': {
                'title': "My Family Tree",
                'btn_show_info': "Show Information",
                'me': "Me",
                'father': "Father",
                'mother': "Mother",
                'maternal_grandfather': "Maternal Grandfather",
                'maternal_grandmother': "Maternal Grandmother",
                'uncle_maternal': "Maternal Uncle",
                'cousin_maternal': "Cousin",
                'paternal_sibling_1': "Paternal Sibling 1",
                'paternal_sibling_2': "Paternal Sibling 2",
                'paternal_sibling_3': "Paternal Sibling 3",
                'paternal_sibling_4': "Paternal Sibling 4",
                'btn_father': "↑ View Father",
                'btn_mother': "↑ View Mother",
                'btn_maternal_grandparents': "↑ Maternal Grandparents",
                'btn_uncle': "→ View Uncle",
                'btn_cousin': "↓ View Daughter (Cousin)",
                'btn_siblings': "← View Paternal Sibling"
            }
        }
        
        self.members_data = {
            'pt': {
                'me': {'name': "Seu Nome", 'age': "X anos", 'bio': "Estudante de ADS e Inglês. Apaixonado por tecnologia e desenvolvimento de sistemas."},
                'father': {'name': "Nome do Pai", 'age': "X anos", 'bio': "Biografia curta sobre seu pai aqui."},
                'mother': {'name': "Nome da Mãe", 'age': "X anos", 'bio': "Biografia curta sobre sua mãe aqui."},
                'maternal_grandfather': {'name': "Avô Materno", 'age': "X anos", 'bio': "Biografia sobre seu avô materno."},
                'maternal_grandmother': {'name': "Avó Materna", 'age': "X anos", 'bio': "Biografia sobre sua avó materna."},
                'uncle_maternal': {'name': "Nome do Tio", 'age': "X anos", 'bio': "Informações sobre seu tio materno."},
                'cousin_maternal': {'name': "Nome da Prima", 'age': "X anos", 'bio': "Informações sobre sua prima, filha do seu tio."},
                'paternal_sibling_1': {'name': "Irmão 1", 'age': "X anos", 'bio': "Seu primeiro irmão por parte de pai."},
                'paternal_sibling_2': {'name': "Irmão 2", 'age': "X anos", 'bio': "Seu segundo irmão por parte de pai."},
                'paternal_sibling_3': {'name': "Irmão 3", 'age': "X anos", 'bio': "Seu terceiro irmão por parte de pai."},
                'paternal_sibling_4': {'name': "Irmão 4", 'age': "X anos", 'bio': "Seu quarto irmão por parte de pai."}
            },
            'en': {
                'me': {'name': "Your Name", 'age': "X years old", 'bio': "ADS and English student. Passionate about technology and development."},
                'father': {'name': "Father Name", 'age': "X years old", 'bio': "Short biography about your father here."},
                'mother': {'name': "Mother Name", 'age': "X years old", 'bio': "Short biography about your mother here."},
                'maternal_grandfather': {'name': "Maternal Grandfather", 'age': "X years old", 'bio': "Biography of your maternal grandfather."},
                'maternal_grandmother': {'name': "Maternal Grandmother", 'age': "X years old", 'bio': "Biography of your maternal grandmother."},
                'uncle_maternal': {'name': "Uncle Name", 'age': "X years old", 'bio': "Information about your maternal uncle."},
                'cousin_maternal': {'name': "Cousin Name", 'age': "X years old", 'bio': "Information about your cousin."},
                'paternal_sibling_1': {'name': "Sibling 1", 'age': "X years old", 'bio': "Your first sibling from your father's side."},
                'paternal_sibling_2': {'name': "Sibling 2", 'age': "X years old", 'bio': "Your second sibling from your father's side."},
                'paternal_sibling_3': {'name': "Sibling 3", 'age': "X years old", 'bio': "Your third sibling from your father's side."},
                'paternal_sibling_4': {'name': "Sibling 4", 'age': "X years old", 'bio': "Your fourth sibling from your father's side."}
            }
        }