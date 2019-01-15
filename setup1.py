from cx_Freeze import setup, Executable
import sys
import os

includes = []
include_files = [r"C:\Users\Suporte-06\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\Suporte-06\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
				 r'icones\icon_direita.png',
				 r'icones\icon_esquerda.png',
				 r'icones\icon_lista.png',
				 r'icones\icon_play.png',
				 r'icones\icon_play_pause.png',
				 r'icones\icon_player.ico']
os.environ['TCL_LIBRARY'] = r'C:\Users\Suporte-06\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Suporte-06\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
base = 'Win32GUI' if sys.platform == 'win32' else None


setup(name='Rom_Player', version='4.0', description='Rom Player',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable(r'Rom_Player.py', base=base)])