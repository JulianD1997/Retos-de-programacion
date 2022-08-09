"""/*
* Reto #19
* CONVERSOR TIEMPO
* Fecha publicación enunciado: 09/05/22
* Fecha publicación resolución: 16/05/22
* Dificultad: FACIL
*
* Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
*
* Información adicional:
* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
* - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
* - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
*
*/"""
class Millisecond :
    def __init__(self, day = 0, hour = 0, minute = 0, second = 0):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    def milliseconds(self):
        day_to_hour = self.day * 24
        hour_to_minute = self.hour  * 60 + day_to_hour * 60
        minute_to_second = self.minute * 60 + hour_to_minute * 60
        return f"{self.second * 1000 + minute_to_second * 1000} milliseconds"
if __name__ == '__main__':

    time_1 = Millisecond(0, 0, 0, 10)
    time_2 = Millisecond(2, 5, -45, 10)
    time_3 = Millisecond(2000000000, 5, 45, 10)
    print(time_1.milliseconds())
    print(time_2.milliseconds())
    print(time_3.milliseconds())