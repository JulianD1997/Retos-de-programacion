import re
"""/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d )]  - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def is_balanced(txt):
    dict_delimiters={
    '}':'{',
    ')':'(',
    ']':'['
    }
    delimiters  = []
    for ch in txt:
        if re.match(r'[{}[\]()]',ch):
            delimiters.append(ch)
    if len(delimiters) % 2 == 0:
        while len(delimiters) != 0 :
            for i in range(len(delimiters)):
                if delimiters[i] in dict_delimiters:
                    if dict_delimiters[delimiters[i]] == delimiters[i-1]:
                        del delimiters[i]
                        del delimiters[i-1]
                        break
                    else :
                        return False
        return True            
    else :
        return False
        
print(is_balanced("{a + b [c] * (2x2){}{}}{}"))
print(is_balanced("{ [ a * ( c + d ) ] - 5 }"))
print(is_balanced("{ a * ( c + d ) ] - 5 }"))
print(is_balanced("{a^4 + (((ax4)}"))
print(is_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(is_balanced("{{{{{{(}}}}}}"))
print(is_balanced("(a"))
        
