# 🌳 Family Tree Cascade System

Este é um projeto desenvolvido para fins de estudo e apresentação em aula. A ideia foi criar um sistema dinâmico de árvore genealógica usando **Python** e **Tkinter**, onde os membros da família vão surgindo em cascata conforme o usuário interage.

O sistema também conta com suporte a dois idiomas (Português e Inglês) com transição em tempo real e um sistema de enquadramento inteligente de imagens para evitar que os rostos fiquem cortados.

Para substutuir os dados presentes no projeto atual pelos respectivos dados o usuário como, nome, idade, biorafia e foto; Basta apenas ir no arquivo "brain" e substitui-los no "self.members_data" deixarei umas imagens de meus familíares apenas para teste das funcionalidades do programa, as fotos deles não são para fins comerciais!

---

## 🛠️ Como o projeto funciona?

Para deixar o código limpo e organizado, a lógica foi separada da interface visual:

* **`project/main.py`**: Cuida de toda a interface gráfica (Tkinter), renderização dos cards e cálculo de posicionamento do grid.
* **`functions/brain.py`**: Funciona como o nosso "mini banco de dados" e motor lógico, controlando os textos, as traduções e os dados de cada familiar.
* **`assets/`**: Pasta que armazena as fotos utilizadas no sistema.

---

## 🚀 Como rodar na sua máquina

1. **Clone o repositório:**

```bash
git clone https://github.com/gabbrielbf/Familly_Tree_UFAM.git
cd Familly_Tree_UFAM
