class Complex:
    Re = None
    Im = None
    
    def __init__(self, x, y):
        self.Re = x
        self.Im = y
    
    def display(self):
        print(f"The complex number is = {self.Re} + {self.Im}i")

    def add(self, z):
        return Complex(self.Re+z.Re, self.Im+z.Im)

z1 = Complex(1,2)
z1.display()
z2 = Complex(2,3)
z = z1.add(z2)
z.display()
