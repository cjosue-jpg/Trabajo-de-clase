class Liquidpaper:
    def __init__(self, color, forma, material, marca):
        self.name = color
        self.forma = forma
        self.material = material
        self.marca = marca
    def mostrar(self):
        print(f"Color: {self.name}, Forma: {self.forma}, Marca: {self.marca}, Material: {self.material}")