"""/*
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
from datetime import datetime
import re

def days_between(date_1,date_2):
    pattern = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
    try:
        if re.match(pattern,date_1) and re.match(pattern,date_2):
            date1 = datetime.strptime(date_1,'%d/%m/%Y')
            date2 = datetime.strptime(date_2,'%d/%m/%Y')
            days_between = date1-date2 if date1 > date2 else date2-date1
            return f'{days_between.days} days'
        else :
            raise ValueError("Incorrect Format")
    except ValueError as e :
        return e
if __name__ == "__main__":
    print(days_between("18/05/2023", "29/05/2022"))
    print(days_between("mouredev", "29/04/2022"))
    print(days_between("18/05/2011", "29/04/2022"))