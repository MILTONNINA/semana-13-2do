import tkinter as tk
from tkinter import messagebox
from servicios.restaurante_servicio import RestauranteServicio

class LoginView(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.servicio = RestauranteServicio()

        tk.Label(self, text="Restaurante App - Login", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(self, text="Usuario:").pack(pady=5)
        self.txt_usuario = tk.Entry(self, font=("Arial", 12))
        self.txt_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.txt_password = tk.Entry(self, show="*", font=("Arial", 12))
        self.txt_password.pack(pady=5)

        tk.Button(self, text="Iniciar Sesión", command=self.verificar_login, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=20)

    def verificar_login(self):
        user = self.txt_usuario.get()
        pwd = self.txt_password.get()

        if not user or not pwd:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return

        usuario_obj = self.servicio.validar_usuario(user, pwd)
        if usuario_obj:
            messagebox.showinfo("Éxito", f"Bienvenido {usuario_obj.username}")
            self.on_login_success(usuario_obj)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")