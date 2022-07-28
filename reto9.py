from operator import le
import re
"""/*
 * Re: #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

phrase = 'Lo mejor de la vida es gratis'
phrase_1 ='.—.. ———   —— . .——— ——— .—.   —.. .   .—.. .—   ...— .. —.. .—   . ...   ——. .—. .— — .. ...'

def translate_text_morse(phrase):
    alphabet_morse = {
    "A" : ".—", "B" : "—...", "C" : "—.—.",
    "CH" : "————", "D" : "—..", "E" : ".",
    "F" : "..—.", "G" : "——.", "H" : "....",
    "I" : "..", "J" : ".———", "K" : "—.—",
    "L" : ".—..", "M" : "——", "N" : "—.",
    "Ñ" : "——.——", "O" : "———", "P" : ".——.",
    "Q" : "——.—", "R" : ".—.", "S" : "...",
    "T" : "—", "U" : "..—", "V" : "...—",
    "W" : ".——", "X" : "—..—", "Y" : "—.——",
    "Z" : "——..", "0" : "—————", "1" : ".————",
    "2" : "..———", "3" : "...——", "4" : "....—",
    "5" : ".....", "6" : "—....", "7" : "——...",
    "8" : "———..", "9" : "————.", "." : ".—.—.—",
    "," : "——..——", "?" : "..——..", "?" : "..——..",
    "\"" : ".—..—.", "/" : "—..—."
    }
    if re.match(r"[a-zA-Z0-9]+",phrase):
        morse_code = [alphabet_morse.get(ch," ") for ch in phrase.upper()]
        morse_str = " ".join(morse_code)            
        return morse_str
    else :
        txt=""
        phrase = phrase.split(" ")
        for char,code in alphabet_morse.items():
            for i in range(len(phrase)):
                if phrase[i] == code :
                    phrase[i] = char

        for i in range(len(phrase)):
            if phrase[i] == "":
                if phrase[i] == phrase[i+1]:
                    txt += " "
            else:
                txt += phrase[i]
        return txt
if __name__ == "__main__":
    print(f"{phrase} significa :\n{translate_text_morse(phrase)}")
    print(f"{phrase_1} significa :\n{translate_text_morse(phrase_1)}")


