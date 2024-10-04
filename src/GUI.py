import tkinter as tk
from tkinter import ttk
import json

class ImputForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Evrima")

        big_frame = ttk.Frame(root)
        big_frame.pack(fill="both", expand=True)

        root.tk.call("source", "Azure-ttk-theme-2.1.0/azure.tcl")
        root.tk.call("set_theme", "dark")

        basic_input = ttk.Frame(big_frame)
        basic_input.pack(fill="both", expand=True)

        Basic_Label = ttk.Label(basic_input, text="Basic Information", font=("Arial", 16, "bold"))
        Basic_Label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        First_Name_Label = ttk.Label(basic_input, text="First Name")
        First_Name_Label.grid(row=1, column=0, padx=0, pady=0)
        self.First_Name = ttk.Entry(basic_input)
        self.First_Name.grid(row=2, column=0, padx=5, pady=0)

        Last_Name_Label = ttk.Label(basic_input, text="Last Name")
        Last_Name_Label.grid(row=1, column=1, padx=5, pady=0)
        self.Last_Name = ttk.Entry(basic_input)
        self.Last_Name.grid(row=2, column=1, padx=5, pady=0)

        Phone_Label = ttk.Label(basic_input, text="Phone Number")
        Phone_Label.grid(row=1, column=2, padx=5, pady=0)
        self.Phone = ttk.Entry(basic_input)
        self.Phone.grid(row=2, column=2, padx=5, pady=0)

        Email_Label = ttk.Label(basic_input, text="Email Address")
        Email_Label.grid(row=1, column=3, padx=5, pady=0)
        self.Email = ttk.Entry(basic_input)
        self.Email.grid(row=2, column=3, padx=5, pady=0)

        submit_button = ttk.Button(big_frame, text="Submit", command=self.on_submit)
        submit_button.pack(pady=10)

    def on_submit(self):
        data = {
            "Personal Information": {
                "First Name": self.First_Name.get(),
                "Last Name": self.Last_Name.get()
            },
            "Contact Information": {
                "Phone Number": self.Phone.get(),
                "Email Address": self.Email.get()
            }
        }
        if self.First_Name.get() == "" and self.Last_Name.get() == "":
            print("No name entered saving as no_name.json")
            with open("history/no_name.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
        else:
            with open(f"history/{self.First_Name.get()}_{self.Last_Name.get()}.json", "w") as json_file:
                json.dump(data, json_file, indent=4)