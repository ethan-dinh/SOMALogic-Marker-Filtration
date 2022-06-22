
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Label, Toplevel
import threading

from ..loading.loadingWindow import *
from ..backend.uniprot import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

global filename, output_file

class App(threading.Thread):
    """ Allows for multi-threading"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        global filename, output_file
        loadWindow(filename, output_file)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def inputWindow():
    Window()

class Window(Toplevel):

    def browse_button(self):
        global filename
        filename = filedialog.askopenfilename()
        self.display_filename.config(text = filename.split("/")[-1])
        print(filename)

    def id_list(self):
        self.destroy()
        global output_file
        output_file = self.output_name.get
        app = App() 
        return

    def __init__(self, *args, **kwargs):
        
        Toplevel.__init__(self, *args, **kwargs)

        self.filename = ""

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

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.id_list,
            relief="flat"
        )
        button_1.place(
            x=556.9999999999999,
            y=394.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_text(
            39.999999999999886,
            51.00000000000001,
            anchor="nw",
            text="UNIPROT CONVERSION TOOL",
            fill="#FCFCFC",
            font=("Baloo2 Bold", 24 * -1)
        )

        self.canvas.create_text(
            477.9999999999999,
            51.00000000000001,
            anchor="nw",
            text="Enter file details.",
            fill="#505485",
            font=("Baloo2 Bold", 24 * -1)
        )

        self.canvas.create_rectangle(
            39.999999999999886,
            102.0,
            99.99999999999989,
            107.0,
            fill="#FCFCFC",
            outline="")

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(648.5,332.5,image=entry_image_1)
        self.output_name = Entry(
            self.canvas,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            font=("Baloo2 Bold", 24 * -1),
            justify="center",
        )
        self.output_name.place(
            x=487.9999999999999,
            y=302.0,
            width=321.0,
            height=59.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            648.4999999999999,
            190.5,
            image=self.entry_image_2
        )
        self.display_filename = Label(
            self.canvas,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            text = "", 
            anchor="w",
            font=("Baloo2 Bold", 16 * -1),
        )
        self.display_filename.place(
            x=487.9999999999999,
            y=160.0,
            width=321.0,
            height=59.0
        )

        self.canvas.create_text(
            478.9999999999999,
            108.0,
            anchor="nw",
            text="Click Here to import file",
            fill="#3A475E",
            font=("Baloo2 Bold", 24 * -1)
        )

        self.canvas.create_text(
            475.9999999999999,
            260.0,
            anchor="nw",
            text="Output filename",
            fill="#3A475E",
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

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.browse_button,
            relief="flat"
        )
        button_2.place(
            x=770.9999999999999,
            y=175.0,
            width=31.0,
            height=31.0
        )
        self.resizable(False, False)
        self.mainloop()