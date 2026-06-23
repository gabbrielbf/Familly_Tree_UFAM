# functions/brain.py

class FamilyTreeBrain:
    def __init__(self):
        self.current_lang = 'en'
        
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
                'me': {'name': "Kelvyson Gabriel Bastos", 'age': "23 anos", 'bio': "Estudante de ADS e Inglês. Apaixonado por tecnologia e desenvolvimento de sistemas.", 'image': "foto_minha.jpeg"},
                'father': {'name': "Kelson Lima", 'age': "45 anos", 'bio': "Já foi cantor, hoje trabalha em uma loja de variedades.", 'image': "foto_pai.JPG"},
                'mother': {'name': "Gilmara Bastos", 'age': "41 anos", 'bio': "Tem uma loja de roupas religiosas e variedades.", 'image': "foto_mae.JPG"},
                'maternal_grandfather': {'name': "Gilson Bastos", 'age': "66 anos", 'bio': "Trabalhou no ramo da política, como vereador e hoje está aposentado.", 'image': "foto_avo1.JPG"},
                'maternal_grandmother': {'name': "Lourdes Bastos", 'age': "63 anos", 'bio': "Trabalha vendendo desinfetantes caseiros até hoje.", 'image': "foto_avo2.JPG"},
                'uncle_maternal': {'name': "Gildson Bastos", 'age': "43 anos", 'bio': "Formado em engenharia química mas hoje atua como engenheiro de projeto gerenciando outros engenheiros.", 'image': "foto_minha_e_pai(tio).jpeg"},
                'cousin_maternal': {'name': "Maria Luiza Bastos", 'age': "4 anos", 'bio': "Apenas estuda, no ensino fundamental.", 'image': "foto_prima.jpeg"},
                'paternal_sibling_1': {'name': "Irmão 1", 'age': "X anos", 'bio': "Sem informações.", 'image': None},
                'paternal_sibling_2': {'name': "Irmão 2", 'age': "X anos", 'bio': "Sem informações..", 'image': None},
                'paternal_sibling_3': {'name': "Irmão 3", 'age': "X anos", 'bio': "Sem informações..", 'image': None},
                'paternal_sibling_4': {'name': "Irmão 4", 'age': "X anos", 'bio': "Sem informações..", 'image': None},
                'maternal_sibling_1': {'name': "Anny Maria Bastos", 'age': "9 anos", 'bio': "Apenas estuda, no ensino fundamental.", 'image': "foto_irma1.JPG"},
                'maternal_sibling_2': {'name': "Estephanny Casemiro Bastos", 'age': "16 anos", 'bio': "Estuda no ensino médio e cursa um curso técnico de enfermagem.", 'image': "foto_irma2.JPG"}
            },
            'en': {
                'me': {'name': "Your Name", 'age': "23 years old", 'bio': "ADS and English student. Passionate about technology and development.", 'image': "foto_minha.jpeg"},
                'father': {'name': "Kelson Lima", 'age': "45 years old", 'bio': "He used to be a singer; today, he works in a variety store.", 'image': "foto_pai.JPG"},
                'mother': {'name': "Gilmara Bastos", 'age': "41 years old", 'bio': "She has a shop selling religious clothing and assorted items.", 'image': "foto_mae.JPG"},
                'maternal_grandfather': {'name': "Gilson Bastos", 'age': "66 years old", 'bio': "He worked in politics as a city councilor and is now retired.", 'image': "foto_avo1.JPG"},
                'maternal_grandmother': {'name': "Lourdes Bastos", 'age': "63 years old", 'bio': "She still works selling homemade disinfectants to this day.", 'image': "foto_avo2.JPG"},
                'uncle_maternal': {'name': "Gildson Bastos", 'age': "43 years old", 'bio': "He holds a degree in chemical engineering but currently works as a project engineer, managing other engineers.", 'image': "foto_minha_e_pai(tio).jpeg"},
                'cousin_maternal': {'name': "Maria Luiza Bastos", 'age': "4 years old", 'bio': "Only studies; is in elementary/middle school.", 'image': "foto_prima.jpeg"},
                'paternal_sibling_1': {'name': "Sibling 1", 'age': "X years old", 'bio': "Not content.", 'image': None},
                'paternal_sibling_2': {'name': "Sibling 2", 'age': "X years old", 'bio': "Not content.", 'image': None},
                'paternal_sibling_3': {'name': "Sibling 3", 'age': "X years old", 'bio': "Not content.", 'image': None},
                'paternal_sibling_4': {'name': "Sibling 4", 'age': "X years old", 'bio': "Not content.", 'image': None},
                'maternal_sibling_1': {'name': "Anny Maria Bastos", 'age': "9 years old", 'bio': "Only studies; is in elementary/middle school.", 'image': "foto_irma1.JPG"},
                'maternal_sibling_2': {'name': "Estephanny Casemiro Bastos", 'age': "16 years old", 'bio': "Is in high school and taking a technical nursing course.", 'image': "foto_irma2.JPG"}
            }
        }

    def set_language(self, lang):
        """ Função designada a transição de idioma para compreensão
        do usuário ou telespectador. """

        if lang in ['pt', 'en']:
            self.current_lang = lang

    def get_text(self, key):
        """ Função designada para pegar o texto com o idioma definido através das funções do arquivo 'main',
        esse seria o cérebro da função acima. """

        return self.translations[self.current_lang].get(key, key)

    def get_member_info(self, member_id):
        """ Função designada para encontrar o usuário respectivo dentro
        das listas de dicionários. """

        return self.members_data[self.current_lang].get(member_id, {'name': "N/A", 'age': "N/A", 'bio': ""})