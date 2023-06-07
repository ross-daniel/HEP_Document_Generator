import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import os


class MainGUI:
    def load_frame(self):
        choice = tk.IntVar()
        choice.set(0)

        options = [
            ("Mechanical QC Document", 0),
            ("Cable Traveler", 1)
        ]

        label = tk.Label(self.root, text="Choose a Document to Request", font=('arial', 18, 'bold'))
        label.grid(row=0, column=1, padx=10, pady=10)

        for option, _val in options:
            tk.Radiobutton(self.root, text=option, variable=choice, val=_val, font=('arial', 14, 'normal')).grid(row=1+_val, column=1,padx=10,pady=10)

        submit_btn = tk.Button(self.root, text=" Submit ", font=('arial', 18, 'bold'), command=lambda: self.submit(choice.get()))
        submit_btn.grid(row=1+len(options), column=1)

        self.root.mainloop()

    def submit(self, choice):
        if choice == 0:
            self.document_req = "Mechanical QC"
        if choice == 1:
            self.document_req = "Cable Traveler"
        else:
            self.document_req = ""
        self.root.destroy()

    def __init__(self):
        # --------------SETUP VARIABLES AND OBJECTS---------------- #
        # setup root
        self.root = tk.Tk()
        self.root.configure()
        self.root.title('Colorado State University HEP Lab')

        self.height = 480
        self.width = 800

        self.document_req = ""
        self.load_frame()


class CableGUI:

    # sets up the Cable Traveler Request Form
    def load_frame(self):
        # TK Variables
        options = ["Passthroughs", "Uppers", "Lowers"]
        _cable_type = tk.StringVar()
        _cable_type.set("Passthroughs")
        _destination = "./Destination_Default/"

        # load frame and setup widgets
        label = tk.Label(self.root, text="Cable Traveler Request Form", font=('arial', 18, 'bold'))
        label.grid(row=0, column=1, padx=10, pady=10)
        type_menu = tk.OptionMenu(self.root, _cable_type, *options)
        type_menu.grid(row=1, column=0, padx=10, pady=10)

        batch_entry = tk.Entry(self.root)
        batch_entry_label = tk.Label(self.root, text="Batch:", font=('arial', 14, 'normal'))
        batch_entry_label.grid(row=1, column=1, padx=10, pady=10)
        batch_entry.grid(row=1, column=2, padx=10, pady=10)

        path_label = tk.Label(self.root, text="Destination:", font=('arial', 14, 'normal'))
        path_label.grid(row=2, column=0, padx=10, pady=10)
        path_entry = tk.Entry(self.root)
        path_entry.insert(0, _destination)  # default directory
        path_entry.grid(row=2, column=1, padx=10, pady=10)
        path_browse_button = tk.Button(self.root, text="Browse", command=lambda: self.browse_file(path_entry))
        path_browse_button.grid(row=2, column=2, padx=10, pady=10)

        submit_btn = tk.Button(self.root, text="Submit", command=lambda: self.submit(_cable_type.get(), batch_entry.get(), path_entry.get()))
        submit_btn.grid(row=3, column=1, padx=10, pady=10)

        self.root.mainloop()

    def browse_file(self, entry):
        file_path = filedialog.askdirectory()
        if os.path.isfile(file_path):
            self.show_message("Path must end in a Directory, not a File", "Error")
            self.browse_file(entry)
        else:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)

    def submit(self, _cable_type, _batch_num, _destination):
        self.cable_type = _cable_type
        self.batch_num = _batch_num
        self.destination = _destination
        check = self.check_valid()
        if check:
            self.root.destroy()
        else:
            self.show_message("One or more fields have been left blank or contain an invalid entry", "Error")
            self.load_frame()

    # TODO: check if input is valid
    def check_valid(self):
        return True

    # displays a message in the TKinter window
    def show_message(self, message, title):
        messagebox.showinfo(title, message)

    def __init__(self):
        # --------------SETUP VARIABLES AND OBJECTS---------------- #
        # setup root
        self.root = tk.Tk()
        self.root.configure()
        self.root.title('Colorado State University HEP Lab')

        self.height = 480
        self.width = 800

        self.cable_type = ''
        self.batch_num = ''
        self.destination = ''
        # ------------------------- ACTIVATE ---------------------------
        self.load_frame()


class MechGUI:
    def __init__(self):
        self.batch_num = ''
        self.item_name = ''
        self.destination = ''
        print("placeholder")