from abc import ABC, abstractmethod

# Abstracción
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nombre):
        self._nombre = nombre

    def obtener_edad(self):
        return self._edad

    def establecer_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa")

# Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Polimorfismo
class Pato(Animal):
    def hacer_sonido(self):
        return "Cuac"

class Gallina(Animal):
    def hacer_sonido(self):
        return "Cloc"

# Uso de las técnicas de programación
if __name__ == "__main__":
    # Ejemplo de abstracción
    figuras = [Circulo(5), Rectangulo(3, 4)]
    for figura in figuras:
        print(f"El área de la figura es: {figura.area()}")

    # Ejemplo de encapsulación
    persona = Persona("Juan", 25)
    print(f"Nombre: {persona.obtener_nombre()}")
    persona.establecer_edad(30)
    print(f"Edad: {persona.obtener_edad()}")
    persona.establecer_edad(-5)  # Esto imprimirá un mensaje de error

    # Ejemplo de herencia y polimorfismo
    animales = [Perro("Rex"), Gato("Luna"), Pato("Donald"), Gallina("Clara")]
    for animal in animales:
        print(f"{animal.nombre} dice {animal.hacer_sonido()}")
