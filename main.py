import tkinter as tk

# ROOT SETUP
root = tk.Tk()
root.geometry("400x800")
root.title('Doggy Dash')

# DEFAULTS
default_bg = "gray"
default_font = ('Arial',15)

# TITLE FRAME SETUP
title_frame = tk.Frame(root, relief=tk.FLAT, borderwidth=10,bg=default_bg)
title_frame.pack()
title = tk.Label(title_frame, text='''Cute little doggies love to dash!''', font= default_font, bg = default_bg)
title.grid()

# INPUT FRAME SETUP
input_frame = tk.Frame(root, relief=tk.FLAT, borderwidth=3,bg=default_bg)
input_frame.pack()

# DETAILS ENTRY

labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

list_of_entries = {}

# Loop over the list of field labels
for i, text in enumerate(labels):
    label = tk.Label(input_frame, text=text)
    entry = tk.Entry(input_frame, width=50)
    list_of_entries["entry"+(i+1)] = entry
    label.grid(row=i, column=0, sticky="e")
    entry.grid(row=i, column=1)
    
# the placement of buttons depends on the length of labels
n = len(labels)

def clear():
    for i in range(len(list_of_entries)):
        current_entry = list_of_entries["entry"+(i+1)]
        current_entry.delete(0,'end')

def submit():
    

# Create the "Submit" button 
btn_submit = tk.Button(input_frame, text="Submit")
btn_submit.grid(row=n, column=1, ipadx=10, pady=5)

# Create the "Clear" button 
btn_clear = tk.Button(input_frame, text="Clear")
btn_clear.grid(row=n+1, column=1, ipadx=10, pady=5)

quitbutton = tk.Button(root, text = "Quit", bg = "red", fg = "white", command = root.destroy)
quitbutton.grid(row=n+1,column=1)

root.mainloop()