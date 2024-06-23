import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from validate_email_address import validate_email

def is_valid_email_simple(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def is_valid_email_advanced(email):
    return validate_email(email)

def validate_email_address():
    email = entry.get()
    simple_check = is_valid_email_simple(email)
    advanced_check = is_valid_email_advanced(email)
    
    if simple_check and advanced_check:
        messagebox.showinfo("Validation Result", "The email address is valid.")
    else:
        messagebox.showerror("Validation Result", "The email address is invalid.")

# Create the main window with ttkbootstrap style
root = ttk.Window(themename="flatly")
root.title("Email Validator")

# Set the main window size and center it
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create and place the card widget in the center
card = ttk.Frame(root, padding=(20, 10), bootstyle="secondary")
card.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add widgets inside the card
label = ttk.Label(card, text="Enter Email Address:")
label.pack(pady=10)

entry = ttk.Entry(card, width=50)
entry.pack(pady=10)

validate_button = ttk.Button(card, text="Validate", command=validate_email_address, bootstyle=SUCCESS)
validate_button.pack(pady=10)

# Run the application
root.mainloop()