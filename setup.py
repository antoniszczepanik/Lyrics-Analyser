import cx_Freeze
import sys
import os.path

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Most Popular Lyrics Words.py", base=base, icon="icon.ico")]


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

cx_Freeze.setup(
    name="Most popular lyrics words",
    options={"build_exe": {"packages": ["tkinter", "pylyrics3", "nltk", "time", "idna"], "include_files": ["icon.ico", "functions.py", "ui.py"]}},
    version="0.01",
    description="This app lets you find 10 most popular nouns and adjectives in a specified artists lyrics",
    executables=executables
)
