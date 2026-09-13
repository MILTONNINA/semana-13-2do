import tkinter as tk
from ui.login_view import LoginView
from ui.main_view import MainView

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Sistema Principal")
        self.root.geometry("600x450")
        
        self.current_view = None
        self.mostrar_login()

    def limpiar_ventana(self):
        if self.current_view:
            self.current_view.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()
        self.current_view = LoginView(self.root, self.mostrar_main)
        self.current_view.pack(fill=tk.BOTH, expand=True)

    def mostrar_main(self, usuario):
        self.limpiar_ventana()
        self.current_view = MainView(self.root, usuario, self.mostrar_login)
        self.current_view.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()