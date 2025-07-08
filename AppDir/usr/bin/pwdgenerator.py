import customtkinter as ctk
import hashlib
import base64
import string

def generate_password():
    master = master_var.get()
    phrase = phrase_var.get()
    length = int(length_slider.get())

    if not master:
        password_var.set("Master password required!")
        return

    # Combine master password and phrase
    combined = master + ":" + phrase

    # Hash the combined input
    hash_bytes = hashlib.pbkdf2_hmac('sha256', combined.encode(), b'salt', 100000)

    # Base64 encode and remove non-alphanumeric chars
    password = base64.urlsafe_b64encode(hash_bytes).decode('utf-8')
    password = ''.join(filter(str.isalnum, password))

    if include_symbols_var.get():
        # Deterministically insert symbols based on hash
        symbols = '!@#$%^&*()'
        symbol_positions = [hash_bytes[i] % len(password) for i in range(2)]
        symbol_choices = [symbols[hash_bytes[i] % len(symbols)] for i in range(2, 4)]
        password_list = list(password)
        for pos, sym in zip(symbol_positions, symbol_choices):
            password_list[pos] = sym
        password = ''.join(password_list)

    # Trim to desired length
    password = password[:length]
    password_var.set(password)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(password_var.get())
    copied_label.configure(text="✅ Copied!")
    copied_label.after(1500, lambda: copied_label.configure(text=""))

def update_length_label(value):
    length_value_label.configure(text=f"{int(float(value))} characters")

# App window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Master Password Generator")
app.geometry("450x470")
app.resizable(False, False)

# Master Password
master_label = ctk.CTkLabel(app, text="Master Password:", font=("Arial", 14))
master_label.pack(pady=5)
master_var = ctk.StringVar()
master_entry = ctk.CTkEntry(app, textvariable=master_var, width=300, show="*")
master_entry.pack(pady=5)

# Custom Phrase
phrase_label = ctk.CTkLabel(app, text="Custom Phrase (optional):", font=("Arial", 14))
phrase_label.pack(pady=5)
phrase_var = ctk.StringVar()
phrase_entry = ctk.CTkEntry(app, textvariable=phrase_var, width=300)
phrase_entry.pack(pady=5)

# Password length slider
length_frame = ctk.CTkFrame(app)
length_frame.pack(pady=10)
length_label = ctk.CTkLabel(length_frame, text="Password Length:", font=("Arial", 14))
length_label.pack(side="left", padx=(0, 10))
length_slider = ctk.CTkSlider(length_frame, from_=15, to=20, number_of_steps=5, width=200, command=update_length_label)
length_slider.set(15)
length_slider.pack(side="left")
length_value_label = ctk.CTkLabel(length_frame, text="15 characters", font=("Arial", 12))
length_value_label.pack(side="left", padx=(10, 0))

# Include Symbols checkbox
include_symbols_var = ctk.BooleanVar(value=False)
ctk.CTkCheckBox(app, text="Include Symbols", variable=include_symbols_var).pack(pady=5)

# Generate button
generate_button = ctk.CTkButton(app, text="Generate Password", corner_radius=8, command=generate_password)
generate_button.pack(pady=15)

# Password display
password_var = ctk.StringVar()
password_entry = ctk.CTkEntry(app, textvariable=password_var, width=300, font=("Arial", 16), justify="center")
password_entry.pack(pady=10)

# Copy button
copy_button = ctk.CTkButton(app, text="Copy to Clipboard", corner_radius=8, command=copy_to_clipboard)
copy_button.pack(pady=5)

# Copied feedback label
copied_label = ctk.CTkLabel(app, text="", font=("Arial", 12), text_color="green")
copied_label.pack()

# Run app
app.mainloop()
