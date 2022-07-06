"""/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
class Figure():
    def __init__(self,name):
        self.__name = name
    def area(self):
        pass

class Triangle(Figure):
    def __init__(self,name,base,height):
        super().__init__(name)
        self.__base = base
        self.__height = height
    def area(self):
        return (self.__base * self.__height)/2

class Rectangle(Figure):
    def __init__(self,name,base,height):
        super().__init__(name)
        self.__base = base
        self.__height = height
    def area(self):
        return self.__base * self.__height

class Square(Figure):
    def __init__(self,name,base):
        super().__init__(name)
        self.__base = base
    def area(self):
        return self.__base * self.__base

def polygon(name,data):
    if name == 'cuadrado':
        square_1 = Square(name,int(data[0]))
        print(f"El area del cuadro es : {square_1.area()}")
    elif name == 'triangulo':
        triangle_1 = Triangle(name,int(data[0]),int(data[1]))
        print(f"El area del triangulo es : {triangle_1.area()}")
    else:
        rentangle_1 = Rectangle(name,int(data[0]),int(data[1]))
        print(f"El area del rectangulo es : {rentangle_1.area()}")

con = True 
while con :
    name = input("Ingrese el nombre del poligono al cual quiere calcular el area : ").lower()
    data = list(input("Ingrese los datos del poligolo separados por comas : ").split(","))
    polygon(name,data)
    con = False if input("Si desea finalizar ingrese SI : ").upper() == 'SI' else True