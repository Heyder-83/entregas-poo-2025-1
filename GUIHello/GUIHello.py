import tkinter as tk
from tkinter import messagebox


class Saludo:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Saludo")
        # Label
        self.label = tk.Label(root, text="Ingrese su nombre:")
        self.label.pack()
        # Entry
        self.entry = tk.Entry(root)
        self.entry.pack()
        # Botón de saludo
        self.saludo_btn = tk.Button(root, text="Saludar", command=self.saludar)
        self.saludo_btn.pack()
        # Botón de salir
        self.salir_btn = tk.Button(root, text="Salir", command=root.quit)
        self.salir_btn.pack()

    def saludar(self):
        nombre = self.entry.get()
        mensaje = f"Hola {nombre}"
        messagebox.showinfo("Saludo", mensaje)

# Ventana raíz
if __name__ == "__main__":
    root = tk.Tk()
    app = Saludo(root)
    root.mainloop()
