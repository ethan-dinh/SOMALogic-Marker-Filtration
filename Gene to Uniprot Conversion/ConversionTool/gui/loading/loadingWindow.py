from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Label, Toplevel
from ..backend.uniprot import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loadWindow(filename, output_file):
    LoadingWindow(filename, output_file)
    
class LoadingWindow(Toplevel):
    def __init__(self, filename, output_file):
        
        Toplevel.__init__(self)

        self.geometry("862x519")
        self.configure(bg = "#3A475E")

        self.canvas = Canvas(
            self,
            bg = "#3A475E",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            430.9999999999999,
            7.105427357601002e-15,
            861.9999999999999,
            519.0,
            fill="#FCFCFC",
            outline="")

        self.canvas.create_text(
            39.999999999999886,
            51.00000000000001,
            anchor="nw",
            text="UNIPROT CONVERSION TOOL",
            fill="#FCFCFC",
            font=("Baloo2 Bold", 24 * -1)
        )

        self.canvas.create_text(
            490,
            250,
            anchor="nw",
            text="Currently Processing File!",
            fill="#505485",
            font=("Baloo2 Bold", 24 * -1)
        )

        self.canvas.create_text(
            39.999999999999886,
            130.0,
            anchor="nw",
            text="Generate a csv file containing a ",
            fill="#FCFCFC",
            font=("Baloo2 Regular", 24 * -1)
        )

        self.canvas.create_text(
            39.999999999999886,
            169.0,
            anchor="nw",
            text="gene names from GWAS",
            fill="#FCFCFC",
            font=("Baloo2 Regular", 24 * -1)
        )

        self.canvas.create_text(
            39.999999999999886,
            212.0,
            anchor="nw",
            text="database",
            fill="#FCFCFC",
            font=("Baloo2 Regular", 24 * -1)
        )

        self.canvas.create_text(
            39.999999999999886,
            422.0,
            anchor="nw",
            text="Made by Ethan Dinh",
            fill="#FCFCFC",
            font=("Baloo2 Regular", 24 * -1)
        )

        self.resizable(False, False)
        create_IDList(filename, output_file)
        self.mainloop()  