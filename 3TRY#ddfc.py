import tkinter as tk; from tkinter import font; from tkinter import messagebox
import configparser

# This is my 3rd and might be my final go at this to make it work properly!!11! but yk what they say, 3rd times a charm 


# Window stuff
root = tk.Tk()
root.title("Python-TB")
root.geometry("300x500")
root.resizable(False, False)
root.configure(bg="white")
default_font = font.nametofont("TkDefaultFont")

# Commands (For binds / Buttons)

def KillApp(event=None):
    root.destroy()
    messagebox.showinfo("Killed app succsessfully!", "Have a good day!")

# Functions

def validate_numeric_input(new_value):
    if new_value.isdigit() or new_value  == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter only numeric values.")
        return False
vcmd = (root.register(validate_numeric_input), '%P')

def applysettings(event=None):
    global Colorval, TolerVal, FovVal, DelVal, TapVal
    selected_color_key = ColorSelectVar.get()
    Colorval = ColorOptions.get(selected_color_key, (254, 254, 64))
    selected_Tolerance = ToleranceSelectVar.get()
    TolerVal = TolVals.get(selected_Tolerance, 35)
    FovVal = FOVEntry.get()
    DelVal = DelayEntry.get()
    selected_tap_val = TaptimeVar.get()
    TapVal = TapOptionsVar.get(selected_tap_val, "Catastrophic Error, please choose an option below, look at the github page for more info, or dm [steve7108] on discord if help is needed.")
    
    if not FovVal or not DelVal:
        messagebox.showerror("Error!", "Please fill in all the fields.")
    else:
        # Create a ConfigParser object
        config = configparser.ConfigParser()
        
        # Add the variables to the config object
        config['Settings'] = {
            'Colorval': str(Colorval),
            'TolerVal': str(TolerVal),
            'FovVal': FovVal,
            'DelVal': DelVal,
            'TapVal': str(TapVal)
        }
        
        # Write the config object to a file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        print("Settings saved to config.ini")


# Labels

TitleLable = tk.Label(root, text="Trigger Automation B)", bg="white", font=(default_font, 14))
WarningLabel = tk.Label(root, text="Pressing O will kill the Application.", bg="white", fg="red")
ColorSelectLabel = tk.Label(root, text="Select Enemy Color", anchor="w", justify="left", bg="white")
ToleranceSelLabel = tk.Label(root, text='Select Tolerance', anchor="w", justify='left', bg="white")
FOVEntryLabel = tk.Label(root, text='Enter FOV by pixel', anchor='w', justify='left', bg='white' )
DelayEntryLabel = tk.Label(root, text='Enter delay (converts to ms)', anchor='w', justify="left", bg='white')
TaptimeLabel = tk.Label(root, text='Select Gun', anchor='w', justify='left', bg='white')

# Selecting Color

ColorSelectVar = tk.IntVar()

RedVal = tk.Radiobutton(root, text="Red (0xB82C29)", bg="red", fg="black", variable=ColorSelectVar, value=1)
YelVal = tk.Radiobutton(root, text="Yellow (0xFEFE40)", bg="yellow", fg='black', variable=ColorSelectVar, value=2)
PurVal = tk.Radiobutton(root, text="Purple (0xA145A3)", bg='purple', fg='black', variable=ColorSelectVar, value=3)

ColorOptions = {
    1: (188, 44, 41),
    2: (254, 254, 64),
    3: (161, 69, 163)
}

# Selecting Tolerance

ToleranceSelectVar = tk.StringVar()

ToleranceOptions = [
    "Ultra Low Tolerance (10 Tol.)",
    "Low Tolerance (20 Tol.)",
    "Medium Tolerance (25 Tol.)",
    "High Tolerance (35 Tol.)",
    "Ultra High Tolerance (45 Tol.)",
    "Maximum Tolerance (70 Tol.)"
]

TolVals = {
    "Ultra Low Tolerance (10 Tol.)": 10,
    "Low Tolerance (20 Tol.)": 20,
    "Medium Tolerance (25 Tol.)": 25,
    "High Tolerance (35 Tol.)": 35,
    "Ultra High Tolerance (45 Tol.)": 45,
    "Maximum Tolerance (70 Tol.)": 70
}

ToleranceDropDown = tk.OptionMenu(root, ToleranceSelectVar, *TolVals)

# FOV By Pixel

FOVPixelVar = tk.IntVar()

FOVEntry = tk.Entry(root,relief="sunken",bg="lightgray", validate="key", validatecommand=vcmd)

# Delay by Ms

DelayMsVar = tk.IntVar()

DelayEntry = tk.Entry(root, validate="key", validatecommand=vcmd, bg="lightgray")

# Taptime

TaptimeVar = tk.StringVar()

TapOptions = [
    "Fast | Vandal/ Med. Phantom (171.428ms/r)",
    "100% | Vandal/Phantom (342.857ms/r)",
    "Fast | Guardian (153.846ms/r)",
    "100% | Guardian (307.692ms/r)"
]

TapOptionsVar = {
    "Fast | Vandal/ Med. Phantom (171.428ms/r)": 171.428,
    "100% | Vandal/Phantom (342.857ms/r)": 342.857,
    "Fast | Guardian (153.846ms/r)": 153.846,
    "100% | Guardian (307.692ms/r)": 307.692
}

TapTimeDD = tk.OptionMenu(root, TaptimeVar, *TapOptions)
# Apply Settings Button

ApplyButton = tk.Button(root, text="Apply", command=applysettings, relief="sunken", bg="lightgray")

# Packaging

TitleLable.pack(pady=2)
WarningLabel.pack(pady=2)
ColorSelectLabel.pack(fill="x",pady=2)
RedVal.pack(pady=2)
YelVal.pack(pady=2)
PurVal.pack(pady=2)
ToleranceSelLabel.pack(fill='x',pady=2)
ToleranceDropDown.pack(pady=2)
FOVEntryLabel.pack(fill="x",pady=2)
FOVEntry.pack(pady=2)
DelayEntryLabel.pack(fill="x", pady=2)
DelayEntry.pack(pady=2)
TaptimeLabel.pack(fill='x',pady=2)
TapTimeDD.pack(pady=2)
ApplyButton.pack(pady=15)

# Binds
root.bind("<o>", KillApp)

root.mainloop()
