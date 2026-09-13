import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Frame):
    def __init__(self, parent, usuario, on_logout):
        super().__init__(parent)
        self.usuario = usuario
        self.on_logout = on_logout
        self.servicio = RestauranteServicio()

        # Encabezado
        header_frame = tk.Frame(self)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(header_frame, text=f"Panel Principal - Rol: {usuario.rol}", font=("Arial", 14, "bold")).pack(side=tk.LEFT)
        tk.Button(header_frame, text="Cerrar Sesión", command=self.on_logout, bg="#f44336", fg="white").pack(side=tk.RIGHT)

        # Notebook (Pestañas) para organizar Productos, Usuarios y Ventas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pestaña 1: Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Productos")
        self.crear_seccion_productos()

        # Pestaña 2: Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self.crear_seccion_usuarios()

        # Pestaña 3: Ventas (Pendiente)
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas (Pendiente)")
        tk.Label(self.tab_ventas, text="Módulo de Ventas en desarrollo (Funcionalidad pendiente)", font=("Arial", 12)).pack(pady=40)

    def crear_seccion_productos(self):
        self.tree_prod = ttk.Treeview(self.tab_productos, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tree_prod.heading("ID", text="ID")
        self.tree_prod.heading("Nombre", text="Nombre")
        self.tree_prod.heading("Precio", text="Precio")
        self.tree_prod.heading("Stock", text="Stock")
        self.tree_prod.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_prod.insert("", tk.END, values=(p.id, p.nombre, f"${p.precio:.2f}", p.stock))

    def crear_seccion_usuarios(self):
        self.tree_user = ttk.Treeview(self.tab_usuarios, columns=("Usuario", "Rol"), show="headings")
        self.tree_user.heading("Usuario", text="Usuario")
        self.tree_user.heading("Rol", text="Rol")
        self.tree_user.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree_user.insert("", tk.END, values=(u.username, u.rol))