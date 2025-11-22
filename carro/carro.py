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
            for key, value in self.carro.items():
                if key == id:
                    value["cantidad"] += 1
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
        
    def eliminar(self, producto):
            id = str(producto.id)
            if id in self.carro:
                del self.carro[id]
                self.guardar_carro()

    def disminuir_cantidad(self, producto):
            id = str(producto.id)
            if id in self.carro.keys():
                for key, value in self.carro.items():
                    if key == id:
                        value["cantidad"] -= 1
                        if value["cantidad"] < 1:
                            self.eliminar(producto)
                            if value["cantidad"] < 1:
                                self.eliminar(producto)
                        break
                self.guardar_carro() 

    def limpiar_carro(self):
            self.session["carro"] = {}
            self.session.modified = True
            
    def total_carro(self):
            total = 0
            for key, value in self.carro.items():
                total += int(value["cantidad"]) * float(value["precio"])
            return total
        
    def obtener_productos(self):
            productos = []
            for key, value in self.carro.items():
                productos.append(value)
            return productos
