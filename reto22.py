"""/*
* Reto #22
* CONJUNTOS
* Fecha publicación enunciado: 01/06/22
* Fecha publicación resolución: 07/06/22
* Dificultad: FÁCIL
*
* Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
* - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
* - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
* - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
*
* Información adicional:
* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
* - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
* - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
*
*/"""
class Element:
    def __init__(self,string_1 , string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def action(self,booleano):
        if booleano:
            re_list = self.comun()
        else:
            re_list = self.no_comun()
        return re_list

    def comun(self):
        list_comun = []
        if len(self.string_1) >= len(self.string_2):
            for i in self.string_1:
                if (i in self.string_2) and (i not in list_comun):
                    list_comun.append(i)
            return list_comun
        else:
            for i in self.string_2:
                if (i in self.string_1) and (i not in list_comun):
                    list_comun.append(i)
            return list_comun

    def no_comun(self):
        list_no_comun = []
        if len(self.string_1) >= len(self.string_2):
            for i in self.string_1:
                if (i not in self.string_2) and (i not in list_no_comun):
                    list_no_comun.append(i)
            return list_no_comun
        else:
            for i in self.string_2:
                if (i not in self.string_1) and (i not in list_no_comun):
                    list_no_comun.append(i)
            return list_no_comun
if __name__ == "__main__":
    elem_1 = Element([1, 2, 3, 3, 4],[2, 2, 3, 3, 3, 4, 6])
    elem_2 = Element([1, 2, 3, 3, 4],[2, 2, 3, 3, 3, 4, 6])
    print(elem_1.action(True))
    print(elem_1.action(False))