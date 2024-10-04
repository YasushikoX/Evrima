import tkinter as tk
from tkinter import ttk
import json

def on_submit():
    data = {
        "First Name": First_Name.get(),
        "Last Name": Last_Name.get(),
        "Phone Number": Phone.get(),
        "Email Address": Email.get()
    }
    if First_Name.get() == "" and Last_Name.get() == "":
        print("No name entered saving as no_name.json")
        with open("no_name.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    else:
        with open(f"{First_Name.get()}_{Last_Name.get()}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

root = tk.Tk()

root.title("Evrima")

big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

root.tk.call("source", "Azure-ttk-theme-2.1.0/azure.tcl")
root.tk.call("set_theme", "dark")

basic_imput = ttk.Frame(big_frame)
basic_imput.pack(fill="both", expand=True)

First_Name_Label = ttk.Label(basic_imput, text="First Name")
First_Name_Label.grid(row=1, column=0, padx=0, pady=0)
First_Name = ttk.Entry(basic_imput)
First_Name.grid(row=2, column=0, padx=5, pady=0)

Last_Name_Label = ttk.Label(basic_imput, text="Last Name")
Last_Name_Label.grid(row=1, column=1, padx=5, pady=0)
Last_Name = ttk.Entry(basic_imput)
Last_Name.grid(row=2, column=1, padx=5, pady=0)

Phone_Label = ttk.Label(basic_imput, text="Phone Number")
Phone_Label.grid(row=1, column=2, padx=5, pady=0)
Phone = ttk.Entry(basic_imput)
Phone.grid(row=2, column=2, padx=5, pady=0)

Email_Label = ttk.Label(basic_imput, text="Email Address")
Email_Label.grid(row=1, column=3, padx=5, pady=0)
Email = ttk.Entry(basic_imput)
Email.grid(row=2, column=3, padx=5, pady=0)

submit_button = ttk.Button(big_frame, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()