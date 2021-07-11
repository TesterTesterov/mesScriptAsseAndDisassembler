import cx_Freeze
import sys
import os
import struct

base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("main.py")]    

cx_Freeze.setup(
        name = "Name",
        options = {"build_exe":{"packages":["os", "struct"]}},
        version="1",
        executables=executables) 