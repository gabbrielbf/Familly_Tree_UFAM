# functions/brain.py

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
                'maternal_sibling_1': "Irmã (Parte de Mãe) 1",
                'maternal_sibling_2': "Irmã (Parte de Mãe) 2",
                'btn_father': "↑ Ver Pai",
                'btn_mother': "↑ Ver Mãe",
                'btn_maternal_grandparents': "↑ Avós Maternos",
                'btn_uncle': "→ Ver Tio",
                'btn_cousin': "↓ Ver Filha (Prima)",
                'btn_siblings': "← Ver Irmãos por parte de Pai",
                'btn_maternal_siblings': "→ Ver Irmãs por parte de Mãe"
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
                'maternal_sibling_1': "Maternal Sibling 1",
                'maternal_sibling_2': "Maternal Sibling 2",
                'btn_father': "↑ View Father",
                'btn_mother': "↑ View Mother",
                'btn_maternal_grandparents': "↑ Maternal Grandparents",
                'btn_uncle': "→ View Uncle",
                'btn_cousin': "↓ View Daughter (Cousin)",
                'btn_siblings': "← View Paternal Sibling",
                'btn_maternal_siblings': "→ View Maternal Sibling"
            }
        }
        
        self.members_data = {
            'pt': {
                'me': {'name': "Seu Nome", 'age': "X anos", 'bio': "Estudante de ADS e Inglês. Apaixonado por tecnologia e desenvolvimento de sistemas.", 'image': "foto_minha.jpeg"},
                'father': {'name': "Nome do Pai", 'age': "X anos", 'bio': "Biografia curta sobre seu pai aqui.", 'image': "foto_pai.JPG"},
                'mother': {'name': "Nome da Mãe", 'age': "X anos", 'bio': "Biografia curta sobre sua mãe aqui.", 'image': "foto_mae.JPG"},
                'maternal_grandfather': {'name': "Avô Materno", 'age': "X anos", 'bio': "Biografia sobre seu avô materno.", 'image': "foto_avo1.JPG"},
                'maternal_grandmother': {'name': "Avó Materna", 'age': "X anos", 'bio': "Biografia sobre sua avó materna.", 'image': "foto_avo2.JPG"},
                'uncle_maternal': {'name': "Nome do Tio", 'age': "X anos", 'bio': "Informações sobre seu tio materno.", 'image': "foto_minha_e_pai(tio).jpeg"},
                'cousin_maternal': {'name': "Nome da Prima", 'age': "X anos", 'bio': "Informações sobre sua prima, filha do seu tio.", 'image': "foto_prima.jpeg"},
                'paternal_sibling_1': {'name': "Irmão 1", 'age': "X anos", 'bio': "Seu primeiro irmão por parte de pai.", 'image': None},
                'paternal_sibling_2': {'name': "Irmão 2", 'age': "X anos", 'bio': "Seu segundo irmão por parte de pai.", 'image': None},
                'paternal_sibling_3': {'name': "Irmão 3", 'age': "X anos", 'bio': "Seu terceiro irmão por parte de pai.", 'image': None},
                'paternal_sibling_4': {'name': "Irmão 4", 'age': "X anos", 'bio': "Seu quarto irmão por parte de pai.", 'image': None},
                'maternal_sibling_1': {'name': "Irmã 1", 'age': "X anos", 'bio': "Sua primeira irmã por parte de mãe.", 'image': "foto_irma1.JPG"},
                'maternal_sibling_2': {'name': "Irmã 2", 'age': "X anos", 'bio': "Sua segunda irmã por parte de mãe.", 'image': "foto_irma2.JPG"}
            },
            'en': {
                'me': {'name': "Your Name", 'age': "X years old", 'bio': "ADS and English student. Passionate about technology and development.", 'image': "foto_minha.jpeg"},
                'father': {'name': "Father Name", 'age': "X years old", 'bio': "Short biography about your father here.", 'image': "foto_pai.JPG"},
                'mother': {'name': "Mother Name", 'age': "X years old", 'bio': "Short biography about your mother here.", 'image': "foto_mae.JPG"},
                'maternal_grandfather': {'name': "Maternal Grandfather", 'age': "X years old", 'bio': "Biography of your maternal grandfather.", 'image': "foto_avo1.JPG"},
                'maternal_grandmother': {'name': "Maternal Grandmother", 'age': "X years old", 'bio': "Biography of your maternal grandmother.", 'image': "foto_avo2.JPG"},
                'uncle_maternal': {'name': "Uncle Name", 'age': "X years old", 'bio': "Information about your maternal uncle.", 'image': "foto_minha_e_pai(tio).jpeg"},
                'cousin_maternal': {'name': "Cousin Name", 'age': "X years old", 'bio': "Information about your cousin.", 'image': "foto_prima.jpeg"},
                'paternal_sibling_1': {'name': "Sibling 1", 'age': "X years old", 'bio': "Your first sibling from your father's side.", 'image': None},
                'paternal_sibling_2': {'name': "Sibling 2", 'age': "X years old", 'bio': "Your second sibling from your father's side.", 'image': None},
                'paternal_sibling_3': {'name': "Sibling 3", 'age': "X years old", 'bio': "Your third sibling from your father's side.", 'image': None},
                'paternal_sibling_4': {'name': "Sibling 4", 'age': "X years old", 'bio': "Your fourth sibling from your father's side.", 'image': None},
                'maternal_sibling_1': {'name': "Sibling 1", 'age': "X years old", 'bio': "Your first sibling from your mother's side.", 'image': "foto_irma1.JPG"},
                'maternal_sibling_2': {'name': "Sibling 2", 'age': "X years old", 'bio': "Your second sibling from your mother's side.", 'image': "foto_irma2.JPG"}
            }
        }

    def set_language(self, lang):
        """ Função designada a transição de idioma para compreensão
        do usuário ou telespectador. """

        if lang in ['pt', 'en']:
            self.current_lang = lang

    def get_text(self, key):
        """ Função designada para definir o idioma em si, esse seria o cérebro
        da função acima. """

        return self.translations[self.current_lang].get(key, key)

    def get_member_info(self, member_id):
        """ Função designada para encontrar o usuário respectivo dentro
        das listas de dicionários. """

        return self.members_data[self.current_lang].get(member_id, {'name': "N/A", 'age': "N/A", 'bio': ""})