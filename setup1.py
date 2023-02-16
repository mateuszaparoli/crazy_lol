import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Crazy LoL",
    version="0.1",
    description="Gera escolhas random para LOL, Não tente isso em Ranked",
    options={"build_exe": build_exe_options},
    executables=[Executable("crazy_lol.py", base=base)]
)