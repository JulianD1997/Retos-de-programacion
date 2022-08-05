"""/*
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
from re import X


class Armstrong:
    def __init__(self,num):
        self.num = num
    def is_armstrong(self):
        sum = 0
        if self.num < 0: return False
        else:
            txt = str(self.num)
            for x in txt:
                sum += int(x)**len(txt)
            return self.num == sum

if __name__ == '__main__':
    x = Armstrong(371)
    x1 = Armstrong(8208)
    x2 = Armstrong(115132219018763992565095597973971522401)
    x3 = Armstrong(115132219018763992565095597973971522402)
    print(x.is_armstrong())
    print(x1.is_armstrong())
    print(x2.is_armstrong())
    print(x3.is_armstrong())