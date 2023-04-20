import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from brands import brands


# Create the main window
root = tk.Tk()
root.geometry("300x600")

# Create global variables for the filter by brand view
brand_label = None
brand_dropdown = None
style_label = None
style_dropdown = None
size_label = None
size_dropdown = None
back_button = None
back_to_filter = None
enter_button = None
filtered_label = None
listbox = None

# Function to create the filter by brand view
def filter_by_brand_view():
    # Destroy the old widgets
    button1.destroy()
    button2.destroy()
    if back_to_filter:
        back_to_filter.destroy()
    if listbox:
        listbox.destroy()

    # Create the new widgets
    global brand_label
    brand_label = tk.Label(root, text="Brand:")
    brand_label.pack()
    brand_options = ["Nike", "Adidas", "Puma", "Reebok"]
    brand_var = tk.StringVar(root)
    brand_var.set(brand_options[0])
    global brand_dropdown
    brand_dropdown = tk.OptionMenu(root, brand_var, *brand_options)
    brand_dropdown.pack()

    global style_label
    style_label = tk.Label(root, text="Style:")
    style_label.pack()
    style_options = ["Running", "Basketball", "Soccer", "Tennis"]
    style_var = tk.StringVar(root)
    style_var.set(style_options[0])
    global style_dropdown
    style_dropdown = tk.OptionMenu(root, style_var, *style_options)
    style_dropdown.pack()

    global size_label
    size_label = tk.Label(root, text="Size:")
    size_label.pack()
    size_options = ["US 7", "US 8", "US 9", "US 10"]
    size_var = tk.StringVar(root)
    size_var.set(size_options[0])
    global size_dropdown
    size_dropdown = tk.OptionMenu(root, size_var, *size_options)
    size_dropdown.pack()

    # Create the back button
    global back_button
    back_button = tk.Button(root, text="Back", command=back_to_main_view)
    back_button.pack(side=tk.LEFT, padx=20, pady=10)

    # Create the enter button
    global enter_button
    enter_button = tk.Button(root, text="Enter", command=create_filtered_view)
    enter_button.pack(side=tk.RIGHT, padx=20, pady=10)

# Function to return to the main view
def back_to_main_view():
    # Destroy the old widgets
    brand_label.destroy()
    brand_dropdown.destroy()
    style_label.destroy()
    style_dropdown.destroy()
    size_label.destroy()
    size_dropdown.destroy()
    back_button.destroy()
    enter_button.destroy()

    # Recreate the main widgets
    create_main_view()


def back_to_filtered_view():
    filter_by_brand_view()


# Function to create the filtered view
def create_filtered_view():
    # Destroy the old widgets
    brand_label.destroy()
    brand_dropdown.destroy()
    style_label.destroy()
    style_dropdown.destroy()
    size_label.destroy()
    back_button.destroy()
    size_dropdown.destroy()
    enter_button.destroy()

    # Create the new widgets
    items = ["item 1", "item 2", "item 3", "item 4", "item 5"]

    # create a Combobox widget and add the items to it
    global listbox
    listbox = tk.Listbox(root)
    for item in items:
        listbox.insert("end", item)
    listbox.pack()
    listbox.bind("<<ListboxSelect>>", on_select)

    global back_to_filter
    back_to_filter = tk.Button(root, text="Back", command=filter_by_brand_view)
    back_to_filter.pack(side=tk.LEFT, padx=20, pady=10)
    # global filtered_label
    # filtered_label = tk.Label(root, text="Filtered Results:")
    # filtered_label.pack(side=tk.CENTER)


# Function to create the main view
def create_main_view():
    # Create button 1
    global button1
    button1 = tk.Button(root, text="Filter By Brand", height=5, width=20, command=filter_by_brand_view)
    button1.pack(fill=tk.BOTH, expand=True, padx=20, pady=50)

    # Create button 2
    global button2
    button2 = tk.Button(root, text="Search For Shoe", height=5, width=20)
    button2.pack(fill=tk.BOTH, expand=True, padx=20, pady=50)

# function to handle the ListboxSelect event
def on_select(event):
    # get the index of the selected item
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        # get the selected item
        item = event.widget.get(index)
        # display a message box with the selected item
        messagebox.showinfo("Selected Item", f"You clicked on {item}")

create_main_view()

root.mainloop()