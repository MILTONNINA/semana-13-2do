class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "rol": self.rol
        }