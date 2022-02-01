import sys
import cx_Freeze

base = None

if (sys.platform == 'win32'):
    base = "Win32GUI"


executables = [cx_Freeze.Executable("main.py",
                                    shortcut_name="mesScriptAsseAndDisassembler",
                                    shortcut_dir="mesScriptAsseAndDisassembler")]

cx_Freeze.setup(
        name="mesScriptAsseAndDisassembler",
        version="1.3",
        description="Dual languaged (rus+eng) tool for packing and unpacking mes scripts of Silky Engine.\n"
                    "Двухязычное средство (рус+англ) для распаковки и запаковки скриптов mes Silky Engine.",
        options={"build_exe": {"packages": []}},
        executables=executables
)
