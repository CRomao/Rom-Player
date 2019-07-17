import sys
from cx_Freeze import setup, Executable
import pygame
import os
import tkinter
os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
base = None
if sys.platform == 'Win32':
    base = "Win32GUI"

executables = [
    Executable("player_4-0.py", base=base)
]

buildOptions = dict(
    packages = [],
    includes = ["pygame", "tkinter","pyautogui"],
    include_files = ['kansas.mp3','icon_direita.png','icon_esquerda.png','icon_lista.png','icon_play.png','icon_play_pause.png'],
    excludes = []
)

setup(
    name = "Player",
    version = "1.0",
    description = "Player",
    options  = dict(build_exe = buildOptions),
    executables = executables


)
