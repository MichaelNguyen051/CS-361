import tkinter as tk
from FilterOptions.brands import brands
from FilterOptions.climbing_type import climbing_type
from FilterOptions.closure_type import closure_type
from ShoeList.retrieve_shoe_details import retrieve_shoe_list
import webbrowser
from DetailedView.downloadImage import download_shoe_image
import textwrap
from time import sleep
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.geometry("300x600")

# Create global variables for the filter by brand view
brand_label = None
brand_dropdown = None
climbing_style = None
style_dropdown = None
closure_label = None
closure_dropdown = None
back_button = None
back_to_filter = None
enter_button = None
filtered_label = None
listbox = None
brand = None
style = None
closure = None
scrollbar = None
new_brand_entry = None
create_new_brand = None
shoes_retrieved = None


# Function to create the main view
def create_main_view():
    # Create button 1
    global filter_by_button
    filter_by_button = tk.Button(root, text="Filter By Brand", height=5, width=20, command=filter_by_brand_view)
    filter_by_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=50)

    # Create button 2
    global add_brand_button
    add_brand_button = tk.Button(root, text="Add a Brand", height=5, width=20, command=create_new_brand_view)
    add_brand_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=50)


# Function to create the filter by brand view
def filter_by_brand_view():
    # Destroy the old widgets
    filter_by_button.destroy()
    add_brand_button.destroy()
    if back_to_filter:
        back_to_filter.destroy()
    if listbox:
        listbox.destroy()
        scrollbar.destroy()

    # Create the new widgets
    global brand_label
    brand_label = tk.Label(root, text="Brand:")
    brand_label.pack()
    brand_options = brands
    brand_var = tk.StringVar(root)
    brand_var.set(brand_options[0])
    global brand_dropdown
    brand_dropdown = tk.OptionMenu(root, brand_var, *brand_options)
    brand_dropdown.pack()

    global climbing_style
    climbing_style = tk.Label(root, text="Climbing Type (optional):")
    climbing_style.pack()
    style_options = climbing_type
    style_var = tk.StringVar(root)
    style_var.set(style_options[0])
    global style_dropdown
    style_dropdown = tk.OptionMenu(root, style_var, *style_options)
    style_dropdown.pack()

    global closure_label
    closure_label = tk.Label(root, text="Closure System (optional):")
    closure_label.pack()
    closure_options = closure_type
    closure_var = tk.StringVar(root)
    closure_var.set(closure_options[0])
    global closure_dropdown
    closure_dropdown = tk.OptionMenu(root, closure_var, *closure_options)
    closure_dropdown.pack()

    # Create the back button
    back_to_main_button()

    # Create the enter button
    global enter_button
    enter_button = tk.Button(root, text="Enter", command=lambda:
    (get_filters(brand_var, style_var, closure_var), create_filtered_view()))
    enter_button.pack(side=tk.RIGHT, padx=20, pady=10)


def get_filters(brand_selection, style_selection, closure_selection):
    global brand
    global style
    global closure
    no_selection = "select"
    brand = str(brand_selection.get())
    style = str(style_selection.get())
    closure = str(closure_selection.get())
    if style == no_selection:
        style = None
    if closure == no_selection:
        closure = None


# Function to return to the main view
def back_to_main_view():
    # Destroy the old widgets
    if brand_label:
        brand_label.destroy()
        brand_dropdown.destroy()
        climbing_style.destroy()
        style_dropdown.destroy()
        closure_label.destroy()
        closure_dropdown.destroy()
        enter_button.destroy()
    if create_new_brand is not None:
        new_brand_entry.destroy()
        create_new_brand.destroy()
    back_button.destroy()

    # Recreate the main widgets
    create_main_view()


def create_new_brand_view():
    filter_by_button.destroy()
    add_brand_button.destroy()
    global new_brand_entry
    new_brand_entry = tk.Entry(root, width=30)
    new_brand_entry.pack(pady=10)

    # Create a new brand button widget
    global create_new_brand
    create_new_brand = tk.Button(root, text="Add Brand",
                                 command=append_new_brand)
    create_new_brand.pack()

    back_to_main_button()


def append_new_brand():
    global new_brand_entry
    brands.append(str(new_brand_entry.get()))
    back_to_main_view()
    return


# Function to create the filtered view
def create_filtered_view():
    # Destroy the old widgets
    brand_label.destroy()
    brand_dropdown.destroy()
    climbing_style.destroy()
    style_dropdown.destroy()
    closure_label.destroy()
    back_button.destroy()
    closure_dropdown.destroy()
    enter_button.destroy()

    # Create the new widgets
    global shoes_retrieved
    shoes_retrieved = retrieve_shoe_list(brand, style, closure)

    # create a Combobox widget and add the items to it
    global listbox
    listbox = tk.Listbox(root, width=45, height=20)
    global scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    for name in shoes_retrieved:
        listbox.insert("end", name)
    listbox.pack()
    listbox.bind("<<ListboxSelect>>", on_select)

    global back_to_filter
    back_to_filter = tk.Button(root, text="Back", command=filter_by_brand_view)
    back_to_filter.pack(side=tk.LEFT, padx=20, pady=10)


# function to handle the ListboxSelect event
def on_select(event):
    # get the index of the selected item
    selected_item = [listbox.get(idx) for idx in listbox.curselection()]
    shoe = selected_item[0]
    show_video_window(shoe)


def show_video_window(selection):
    # create a new window
    shoe_detail_window = tk.Toplevel(root, width=200, height=200)
    shoe_detail_window.title(f"{selection}")
    global shoes_retrieved
    selected_shoe_details = shoes_retrieved[selection]["Description"]
    # create a Label widget with the image
    shoe_name = str(selection).lower().replace(" ", "+")
    text_link = tk.Button(shoe_detail_window, text="Video of Shoe", pady=5, command=lambda: open_link(shoe_name))
    text_link.grid(column=0, row=0)
    try:
        details = selected_shoe_details
    except AttributeError:
        details = "No details on the shoe could be retrieved at this time."
    wrapped_text = textwrap.fill(details, width=300)
    text_label = tk.Label(shoe_detail_window, text=wrapped_text, wraplength=300)
    text_label.grid(column=0, row=1)


def open_link(shoe_name):
    youtube_link = "www.youtube.com/results?search_query=" + shoe_name
    webbrowser.open(youtube_link)


def back_to_main_button():
    global back_button
    back_button = tk.Button(root, text="Back", command=back_to_main_view)
    back_button.pack(side=tk.LEFT, padx=20, pady=10)


create_main_view()

root.mainloop()
