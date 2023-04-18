import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a list of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Create a listbox to display the items
listbox = tk.Listbox(root, selectmode=tk.SINGLE, bd=1, relief=tk.SOLID)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(fill=tk.BOTH, expand=True)

# Run the main loop
root.mainloop()
