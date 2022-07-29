import re
"""/*
 * Reto #12
 * ¿ES UN PALÍNDROMO?
 * Fecha publicación enunciado: 21/03/22
 * Fecha publicación resolución: 28/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
def palindromo(txt):

    txt = txt.lower()
    txt = re.sub(r'[áà]','a',txt)
    txt = re.sub(r'[èé]','e',txt)
    txt = re.sub(r'[íì]','i',txt)
    txt = re.sub(r'[òó]','o',txt)
    txt = re.sub(r'[üùú]','u',txt)
    txt = re.sub(r'[\s,\.]','',txt)
    if txt == txt[::-1]:
        return True
    else: 
        return False
if __name__ == '__main__':
    print("Es palindromo","si "if palindromo("Ana lleva al oso la avellana.") else 'No')
    print("Es palindromo","si "if palindromo("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida") else 'No')
    print("Es palindromo","si "if palindromo("¿Qué os ha parecido el reto?") else 'No')