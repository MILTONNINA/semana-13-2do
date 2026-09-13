from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.path_productos = "datos/productos.json"
        self.path_usuarios = "datos/usuarios.json"

    def validar_usuario(self, username, password):
        usuarios = ArchivoServicio.leer_json(self.path_usuarios)
        for u in usuarios:
            if u["username"] == username and u["password"] == password:
                return Usuario(u["username"], u["password"], u["rol"])
        return None

    def obtener_productos(self):
        datos = ArchivoServicio.leer_json(self.path_productos)
        return [Producto(p["id"], p["nombre"], p["precio"], p["stock"]) for p in datos]

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(self.path_usuarios)
        return [Usuario(u["username"], u["password"], u["rol"]) for u in datos]