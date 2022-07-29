"""/*
 * Reto #13
 * FACTORIAL RECURSIVO
 * Fecha publicación enunciado: 28/03/22
 * Fecha publicación resolución: 04/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
def factorial(num):
    if num <= 0:
        return False
    elif num == 1:
        return 1
    else :
        return num * factorial(num-1)
if __name__ == "__main__":
    print(f"\nfactorial de {0}",f"es = a {factorial(0)}" if factorial(0)!= False else "No tiene factorial")
    print(f"\nfactorial de {7}",f"es = a {factorial(7)}" if factorial(7)!= False else "No tiene factorial")
    print(f"\nfactorial de {10}",f"es = a {factorial(10)}" if factorial(10)!= False else "No tiene factorial")
    print(f"\nfactorial de {10}",f"es = a {factorial(1)}" if factorial(1)!= False else "No tiene factorial")
    print(f"\nfactorial de {-1}",f"es = a {factorial(-1)}" if factorial(-1)!= False else "No tiene factorial")