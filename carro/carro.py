class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro  # <-- importante asignar siempre self.carro

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carro.keys(): 
            self.carro[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            self.carro[id]["cantidad"] += 1
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
