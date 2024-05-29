import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Selecione pelo menos um conjunto de caracteres")
    else:
        password = "".join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
        pyperclip.copy(password)  # Copia a senha para a área de transferência

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Comprimento da senha
length_label = tk.Label(root, text="Comprimento da Senha:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Opções de caracteres
lowercase_var = tk.IntVar()
lowercase_checkbox = tk.Checkbutton(root, text="Minúsculas", variable=lowercase_var)
lowercase_checkbox.pack()

uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(root, text="Maiúsculas", variable=uppercase_var)
uppercase_checkbox.pack()

digits_var = tk.IntVar()
digits_checkbox = tk.Checkbutton(root, text="Números", variable=digits_var)
digits_checkbox.pack()

special_chars_var = tk.IntVar()
special_chars_checkbox = tk.Checkbutton(root, text="Caracteres Especiais", variable=special_chars_var)
special_chars_checkbox.pack()

# Botão para gerar a senha
generate_button = tk.Button(root, text="Gerar Senha", command=generate_password)
generate_button.pack()

# Botão para copiar a senha
copy_button = tk.Button(root, text="Copiar Senha", command=lambda: pyperclip.copy(result_label.cget("text")))
copy_button.pack()

# Resultado da senha
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
