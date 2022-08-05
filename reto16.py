"""/*
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
import re
def capitalize(string):
    txt = ""
    list_string = string.split()
    for x in list_string:
        p = list(x)
        if re.match(r'\W',p[0]):
            asc = (ord(p[1]))-32
            p[1] = chr(asc)
            txt += "".join(p)
            txt += " "
            continue
        elif not re.match(r'[A-Z]',p[0]):
            if p[0] == 'ñ':
                asc = 209
                p[0] = chr(asc)
            else :
                asc = (ord(p[0]))-32
                p[0] = chr(asc)
            p
            txt += "".join(p)
            txt += " "
            continue
        else:
            txt += "".join(p)
            txt += " "
            continue
    print(txt)
if __name__ == "__main__":
    capitalize("¿hola qué tal estás?")
    capitalize("¿hola       qué tal estás?")
    capitalize("El niño ñoño")