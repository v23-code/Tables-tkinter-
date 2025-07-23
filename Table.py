import tkinter as tk 
import ttkbootstrap as ttk 

slime = ['green', 'blue', 'yellow']
dollar = ['22.40$', '1.00$', '5.00$']
company = ['FlameSlimeProduce', 'Lemon', 'Jollibee Slime Station']

def open_slime():
    window = ttk.Window("Table List", size=(600, 300), maxsize=(600, 300), minsize=(600, 300))
    table = ttk.Treeview(window, columns=('1', '2', '3'), show='headings')
    table.heading(column=1, text="Slimes")
    table.heading(column=2, text="Company")
    table.heading(column=3, text="Cost")
    table.pack(fill='both', expand=True)
    
    table.insert(parent='', index=0, values=('orange', '2.32$', 'Compressed'))
    for s, c, x in zip(slime, dollar, company):
        table.insert(parent='', index=tk.END, values=(s, c, x))

    def delete(_):
        for value in table.selection():
            table.delete(value)

    table.bind('<Delete>', delete)

    window.mainloop()   

def add_slime():
    def adding_table():
        slime.append(entry_string1.get())
        dollar.append(entry_string2.get())
        company.append(entry_string3.get())
    window = ttk.Window("Table Add", size=(450, 50), maxsize=(450, 50), minsize=(450, 50))
    label = ttk.Label(window, text="COLOR OF SLIME | COST | COMPANY")
    label.pack()
    entry_string1 = tk.StringVar()
    entry = ttk.Entry(window, textvariable=entry_string1)
    entry.pack(side='left')
    entry_string2 = tk.StringVar()
    entry2 = ttk.Entry(window, textvariable=entry_string2)
    entry2.pack(side='left')
    entry_string3 = tk.StringVar()
    entry3 = ttk.Entry(window, textvariable=entry_string3)
    entry3.pack(side='left')
    button_add = ttk.Button(window, text='ADD', command=adding_table)
    button_add.pack(side='left')
    window.mainloop()


window = ttk.Window("Table List", size=(100, 75), maxsize=(100, 75), minsize=(100, 75))
button = ttk.Button(window, text="Open", command=open_slime)
button.pack(pady=6)
button = ttk.Button(window, text="Add", command=add_slime)
button.pack()

window.mainloop()
