from cx_Freeze import setup, Executable
import sys
import os

includes = []
include_files = [r"C:\Users\Romão\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll",
                 r"C:\Users\Romão\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll",
                 r'kansas.mp3',
				 r'icon_direita.png',
				 r'icon_esquerda.png',
				 r'icon_lista.png',
				 r'icon_play.png',
				 r'icon_play_pause.png',
				 r'icon_player.ico']
os.environ['TCL_LIBRARY'] = r'C:\Users\Romão\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Romão\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
base = 'Win32GUI' if sys.platform == 'win32' else None


setup(name='PRom', version='4.0', description='Player de Músicas',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable(r'player_4-0.py', base=base)])