import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Abhijeet\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Abhijeet\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("simple_files_organizer.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Simple Files Organizer",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
)
