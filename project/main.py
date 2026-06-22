# project/main.py

import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions.brain import FamilyTreeBrain # Garante que o Python encontre a pasta das funções